#!/usr/bin/env python3
"""Review collected terminal data against a git revision.

Compares every ``data/*.yaml`` in the working tree with the same file at a git
revision (default ``HEAD``) and reports only differences that describe a
terminal: its identity, its detected capabilities, and its test results.

Resource profiling, window geometry, and run timestamps are excluded because
they change on every run and say nothing about the terminal.

Usage::

    python scripts/review.py
    python scripts/review.py --rev HEAD~1
    python scripts/review.py kitty foot
"""
# std imports
import os
import sys
import argparse
import textwrap
import subprocess
import collections

import yaml

try:
    _LOADER = yaml.CSafeLoader
except AttributeError:
    _LOADER = yaml.SafeLoader

_HERE = os.path.dirname(os.path.abspath(__file__))
_PROJECT = os.path.dirname(_HERE)
_DATA_DIR = os.path.join(_PROJECT, 'data')

#: Keys that describe the run rather than the terminal.
RUN_KEYS = frozenset((
    'datetime',
    'python_version',
    'resource_profile',
    'seconds_elapsed',
    'session_arguments',
    'ucs_detect_version',
    'unicode_version',
    'wcwidth_version',
))

#: Run keys worth summarizing across every terminal; timings are not.
RUN_SUMMARY_KEYS = (
    'python_version',
    'session_arguments',
    'ucs_detect_version',
    'unicode_version',
    'wcwidth_version',
)

#: Top-level keys that describe the window the terminal was measured in.
WINDOW_KEYS = frozenset(('height', 'width'))

#: ``terminal_results`` keys derived from window geometry or font cell size.
WINDOW_RESULT_KEYS = frozenset((
    'cell_height',
    'cell_width',
    'height',
    'pixels_height',
    'pixels_width',
    'screen_ratio',
    'screen_ratio_name',
    'width',
))

#: ``terminal_results`` keys that identify the program rather than a capability.
IDENTITY_RESULT_KEYS = frozenset((
    'software_method',
    'software_name',
    'software_version',
    'ttype',
    'xtversion_raw',
))

LANGUAGE_CATEGORY = 'language_results'
FAILURE_KEYS = ('failed', 'failed_codepoints')

#: Codepoints shown per failure group.
MAX_EXAMPLES = 4

_MISSING = object()


class _Writer(object):
    """Collect output lines with an indentation level."""

    def __init__(self):
        self.lines = []

    def write(self, text='', indent=0):
        """Append *text* indented by two spaces per level."""
        self.lines.append(('  ' * indent + text).rstrip())

    def text(self):
        """Return all lines joined by newlines."""
        return '\n'.join(self.lines)

    def extend(self, lines, indent=0):
        """Append each of *lines*."""
        for line in lines:
            self.write(line, indent)


def _load_worktree(path):
    with open(path, encoding='utf-8') as fin:
        return yaml.load(fin, Loader=_LOADER)


def _load_revision(rev, path):
    """Return the parsed YAML at *rev* for *path*, or None when absent."""
    relpath = os.path.relpath(path, _PROJECT)
    try:
        proc = subprocess.run(
            ['git', 'show', '{}:{}'.format(rev, relpath)],
            cwd=_PROJECT, capture_output=True, check=False)
    except OSError:
        return None
    if proc.returncode:
        return None
    return yaml.load(proc.stdout.decode('utf-8'), Loader=_LOADER)


def _format_value(value):
    if value is _MISSING:
        return '(absent)'
    if isinstance(value, dict):
        return '{{{:,} keys}}'.format(len(value))
    if isinstance(value, list):
        return '[{:,} items]'.format(len(value))
    text = repr(value)
    return text if len(text) <= 60 else text[:57] + '...'


def _format_wchars(escaped):
    """Render a ``\\uXXXX`` escape string as ``U+XXXX`` codepoints."""
    try:
        decoded = escaped.encode('ascii').decode('unicode_escape')
    except (UnicodeDecodeError, AttributeError):
        return str(escaped)
    return ' '.join('U+{:04X}'.format(ord(ch)) for ch in decoded)


def _leaf_changes(old, new, path=()):
    """Yield ``(path, old, new)`` for every changed leaf below *old* and *new*."""
    if isinstance(old, dict) or isinstance(new, dict):
        old_dict = old if isinstance(old, dict) else {}
        new_dict = new if isinstance(new, dict) else {}
        for key in sorted(set(old_dict) | set(new_dict), key=str):
            yield from _leaf_changes(
                old_dict.get(key, _MISSING),
                new_dict.get(key, _MISSING),
                path + (key,))
        return
    if old is _MISSING and new is _MISSING:
        return
    if old is _MISSING or new is _MISSING or old != new:
        yield path, old, new


def _measurement(entry):
    return (entry.get('measured_by_terminal'), entry.get('measured_by_wcwidth'))


def _failure_key(entry, key_name):
    return entry.get(key_name) or entry.get('wchar') or entry.get('wchars')


def _failure_index(entries, key_name):
    return {_failure_key(entry, key_name): entry for entry in entries or ()}


def _compare_failures(old_entries, new_entries, key_name):
    """Return (added, removed, changed) failure entries between two lists."""
    old_index = _failure_index(old_entries, key_name)
    new_index = _failure_index(new_entries, key_name)
    added = [new_index[key] for key in new_index.keys() - old_index.keys()]
    removed = [old_index[key] for key in old_index.keys() - new_index.keys()]
    changed = [
        (old_index[key], new_index[key])
        for key in old_index.keys() & new_index.keys()
        if _measurement(old_index[key]) != _measurement(new_index[key])
    ]
    return added, removed, changed


def _write_measurement_stats(out, old_entry, new_entry, indent):
    for key in sorted(set(old_entry) | set(new_entry)):
        if key in FAILURE_KEYS or key == 'pct_success':
            continue
        old_value = old_entry.get(key, _MISSING)
        new_value = new_entry.get(key, _MISSING)
        if old_value == new_value:
            continue
        if isinstance(old_value, float) or isinstance(new_value, float):
            old_text = '(absent)' if old_value is _MISSING else '{:.2f}'.format(old_value)
            new_text = '(absent)' if new_value is _MISSING else '{:.2f}'.format(new_value)
            out.write('{}: {} -> {}'.format(key, old_text, new_text), indent)
        else:
            out.write('{}: {} -> {}'.format(
                key, _format_value(old_value), _format_value(new_value)), indent)


def _write_new_failures(out, added, key_name, indent, counters):
    counters['added'] += len(added)
    groups = collections.defaultdict(list)
    for entry in added:
        groups[_measurement(entry)].append(entry)
    out.write('new failures: {}'.format(len(added)), indent)
    for measurement, group in sorted(groups.items(), key=lambda item: str(item[0])):
        measured, expected = measurement
        out.write('terminal {}, wcwidth {}: {}'.format(
            measured, expected, len(group)), indent + 1)
        keys = sorted(str(_failure_key(entry, key_name)) for entry in group)
        shown = ', '.join(_format_wchars(key) for key in keys[:MAX_EXAMPLES])
        if len(keys) > MAX_EXAMPLES:
            shown += ', ... ({} more)'.format(len(keys) - MAX_EXAMPLES)
        out.extend(textwrap.wrap(shown, width=96), indent + 2)


def _write_changed_measurements(out, changed, indent, counters):
    counters['changed'] += len(changed)
    out.write('changed measurement: {}'.format(len(changed)), indent)
    for old_entry, new_entry in changed[:MAX_EXAMPLES]:
        key = _failure_key(old_entry, 'wchar')
        out.write('{}: {} -> {}'.format(
            _format_wchars(key),
            _measurement(old_entry)[0],
            _measurement(new_entry)[0]), indent + 1)
    if len(changed) > MAX_EXAMPLES:
        out.write('... ({} more)'.format(len(changed) - MAX_EXAMPLES), indent + 1)


def _write_failure_diff(out, old_entry, new_entry, key_name, indent, counters):
    key = 'grapheme_id' if key_name == 'wchars' else 'wchar'
    added, removed, changed = _compare_failures(
        old_entry.get('failed_codepoints', old_entry.get('failed')),
        new_entry.get('failed_codepoints', new_entry.get('failed')),
        key)
    if added:
        _write_new_failures(out, added, key_name, indent, counters)
    if removed:
        counters['removed'] += len(removed)
        out.write('no longer failing: {}'.format(len(removed)), indent)
    if changed:
        _write_changed_measurements(out, changed, indent, counters)


def _write_version_comparison(out, name, old_versions, new_versions, counters):
    if len(old_versions) == 1 and len(new_versions) == 1:
        old_version, old_entry = next(iter(old_versions.items()))
        new_version, new_entry = next(iter(new_versions.items()))
        label = name
        if old_version != new_version:
            label = '{} ({} -> {})'.format(name, old_version, new_version)
        _write_one_result(out, label, old_entry or {}, new_entry or {},
                          1, counters)
        return
    for version in sorted(set(old_versions) | set(new_versions), key=str):
        old_entry = old_versions.get(version) or {}
        new_entry = new_versions.get(version) or {}
        if not old_entry:
            out.write('{} {}: (added)'.format(name, version), 1)
            continue
        if not new_entry:
            out.write('{} {}: (removed)'.format(name, version), 1)
            continue
        _write_one_result(out, '{} {}'.format(name, version), old_entry,
                          new_entry, 1, counters)


def _write_one_result(out, label, old_entry, new_entry, indent, counters):
    if old_entry == new_entry:
        return
    counters['categories'] += 1
    out.write(label, indent)
    _write_measurement_stats(out, old_entry, new_entry, indent + 1)
    _write_failure_diff(
        out, old_entry, new_entry, 'wchar', indent + 1, counters)


def _write_language_comparison(out, old_langs, new_langs, counters):
    added_langs = set(new_langs) - set(old_langs)
    removed_langs = set(old_langs) - set(new_langs)
    lang_out = _Writer()
    if added_langs:
        lang_out.write('languages added: {}'.format(', '.join(sorted(added_langs))), 2)
    if removed_langs:
        lang_out.write('languages removed: {}'.format(
            ', '.join(sorted(removed_langs))), 2)
    for lang in sorted(set(old_langs) & set(new_langs)):
        old_entry = old_langs[lang] or {}
        new_entry = new_langs[lang] or {}
        if old_entry == new_entry:
            continue
        counters['languages'] += 1
        lang_out.write(lang, 2)
        _write_measurement_stats(lang_out, old_entry, new_entry, 3)
        _write_failure_diff(
            lang_out, old_entry, new_entry, 'wchars', 3, counters)
    if lang_out.lines:
        out.write(LANGUAGE_CATEGORY, 1)
        out.lines.extend(lang_out.lines)


def _write_added_category(out, name, versions, added):
    out.write('{}: ({})'.format(name, 'added' if added else 'removed'), 1)
    for version, entry in sorted(versions.items()):
        if not isinstance(entry, dict):
            out.write('{}: {}'.format(version, _format_value(entry)), 2)
            continue
        out.write('{}: n_total {}, n_errors {}'.format(
            version, entry.get('n_total', '?'), entry.get('n_errors', '?')), 2)


def _write_test_results(out, old_results, new_results, counters):
    for name in sorted(set(old_results) | set(new_results)):
        old_value = old_results.get(name) or {}
        new_value = new_results.get(name) or {}
        if old_value == new_value:
            continue
        if name == LANGUAGE_CATEGORY:
            _write_language_comparison(out, old_value, new_value, counters)
        elif not old_value and not new_value:
            continue
        elif not old_value:
            counters['categories'] += 1
            _write_added_category(out, name, new_value, added=True)
        elif not new_value:
            counters['categories'] += 1
            _write_added_category(out, name, old_value, added=False)
        else:
            _write_version_comparison(out, name, old_value, new_value, counters)


def _write_identity_changes(out, identity):
    out.write('identity', 1)
    for path, old_value, new_value in identity:
        out.write('{}: {} -> {}'.format(
            '.'.join(map(str, path)),
            _format_value(old_value),
            _format_value(new_value)), 2)


def _compare_document(old, new):
    identity = []
    capabilities = []
    for key in sorted(set(old) | set(new), key=str):
        if key in ('test_results', 'terminal_results'):
            continue
        if key in RUN_KEYS or key in WINDOW_KEYS:
            continue
        old_value = old.get(key, _MISSING)
        new_value = new.get(key, _MISSING)
        if old_value == new_value:
            continue
        for path, old_leaf, new_leaf in _leaf_changes(
                old_value, new_value, (key,)):
            identity.append((path, old_leaf, new_leaf))

    for path, old_value, new_value in _leaf_changes(
            old.get('terminal_results') or {},
            new.get('terminal_results') or {}):
        key = path[-1] if path else ''
        if key in WINDOW_RESULT_KEYS or path == ('decrqss_settings', 'decstbm'):
            continue
        item = (('terminal_results',) + path, old_value, new_value)
        if key in IDENTITY_RESULT_KEYS:
            identity.append(item)
        else:
            capabilities.append(item)

    counters = collections.Counter()
    out = _Writer()
    if identity:
        _write_identity_changes(out, identity)
    if capabilities:
        out.write('capabilities', 1)
        for path, old_value, new_value in capabilities:
            out.write('{}: {} -> {}'.format(
                '.'.join(map(str, path)),
                _format_value(old_value),
                _format_value(new_value)), 2)
    if old.get('test_results') != new.get('test_results'):
        test_out = _Writer()
        _write_test_results(test_out, old.get('test_results') or {},
                            new.get('test_results') or {}, counters)
        if test_out.lines:
            out.write('test results', 1)
            out.lines.extend(test_out.lines)

    return out.lines, counters


def _write_run_metadata(out, changes):
    lines = []
    for key in sorted(changes):
        for (old_value, new_value), count in changes[key].most_common():
            suffix = ' ({} files)'.format(count) if count > 1 else ''
            lines.append('{}: {} -> {}{}'.format(
                key, _format_value(old_value), _format_value(new_value), suffix))
    if lines:
        out.write('run environment (not terminal behavior)')
        for line in lines:
            out.write(line, 1)
        out.write()


def main():
    """Compare data files in the working tree with a git revision."""
    parser = argparse.ArgumentParser(
        description='Review data/*.yaml changes against a git revision.')
    parser.add_argument('terminals', nargs='*',
                        help='only review these files or terminal names')
    parser.add_argument('--rev', default='HEAD',
                        help='git revision to compare against (default: HEAD)')
    parser.add_argument('--data-dir', default=_DATA_DIR,
                        help='directory holding the data YAML files')
    args = parser.parse_args()

    names = os.listdir(args.data_dir)
    paths = sorted(
        os.path.join(args.data_dir, name) for name in names
        if name.endswith('.yaml'))
    if args.terminals:
        wanted = set(args.terminals)
        paths = [path for path in paths
                 if os.path.basename(path) in wanted
                 or os.path.splitext(os.path.basename(path))[0] in wanted]
        missing = wanted - {os.path.basename(path) for path in paths} - {
            os.path.splitext(os.path.basename(path))[0] for path in paths}
        if missing:
            parser.error('unknown terminal(s): {}'.format(', '.join(sorted(missing))))

    out = _Writer()
    run_changes = collections.defaultdict(collections.Counter)
    totals = collections.Counter()
    changed_files = 0
    noise_only = 0
    new_files = 0
    test_changed = collections.Counter()

    for path in paths:
        new = _load_worktree(path)
        old = _load_revision(args.rev, path)
        name = os.path.splitext(os.path.basename(path))[0]
        if old is None:
            new_files += 1
            out.write('=== {} (new file) ==='.format(name))
            out.write('  not present at {}'.format(args.rev))
            out.write()
            continue

        for key in RUN_SUMMARY_KEYS:
            for item in _leaf_changes(
                    old.get(key, _MISSING), new.get(key, _MISSING), (key,)):
                path_key, old_value, new_value = item
                run_changes['.'.join(path_key)][(old_value, new_value)] += 1

        lines, counters = _compare_document(old, new)
        if not lines:
            if old != new:
                noise_only += 1
            continue
        changed_files += 1
        out.write('=== {} ==='.format(name))
        out.lines.extend(lines)
        out.write()
        if counters['categories'] or counters['languages']:
            test_changed[name] = counters['categories'] + counters['languages']
        for key in ('added', 'removed', 'changed'):
            totals[key] += counters[key]

    _write_run_metadata(out, run_changes)

    out.write('summary')
    out.write('  {} file{} compared against {}, {} changed, {} new, '
              '{} only resource/window/run'.format(
                  len(paths), '' if len(paths) == 1 else 's',
                  args.rev, changed_files, new_files, noise_only), 1)
    out.write('  new failures: {}, no longer failing: {}, changed measurement: {}'.format(
        totals['added'], totals['removed'], totals['changed']), 1)
    if test_changed:
        out.write('  terminals with test result changes: {}'.format(
            ', '.join(sorted(test_changed))), 1)

    print(out.text())
    return 0


if __name__ == '__main__':
    sys.exit(main())
