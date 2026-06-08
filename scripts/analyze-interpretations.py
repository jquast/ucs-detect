#!/usr/bin/env python
"""
Analyze ucs-detect terminal data: count unique terminal interpretations per feature category,
broken down by DEC 2027 (Grapheme Clustering) support.

Each terminal's correction set (codepoints/graphemes where terminal width differs from wcwidth)
is hashed using the same method as update-tables.py. Terminals are split into three groups:
- GC=on:  graphene clustering mode supported and enabled
- GC=off: graphene clustering mode not supported or not enabled
- GC=?:   DEC 2027 status not probed

Categorization:
    WIDE, NARROW, SRI, SFZ, VS16, VS15, ZWJ, RI, LANG
"""

from __future__ import annotations

# std imports
import os
import glob
import hashlib
from collections import defaultdict

try:
    # 3rd party
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader

# 3rd party
import yaml

PATH_UP = os.path.relpath(os.path.join(os.path.dirname(__file__), os.path.pardir))
PATH_UCS_DETECT_DATA = os.path.join(PATH_UP, 'data')

SOFTWARE_SHARED_ENGINES = {
    'QTerminal': 'qtermwidget',
    'cool-retro-term': 'qtermwidget',
    'Hyper': 'xterm.js',
    'Tabby': 'xterm.js',
    'st-luke': 'st',
}

VTE_CANONICAL = 'vte'


def canonical_name(software_name: str, software_version: str) -> str:
    if 'VTE' in software_version:
        return VTE_CANONICAL.lower()
    return SOFTWARE_SHARED_ENGINES.get(software_name, software_name).lower()


def parse_wchar_codepoint(wchar: str) -> int:
    decoded = wchar.encode('ascii').decode('unicode_escape')
    if len(decoded) > 1 and decoded[-1] in ('\ufe0f', '\ufe0e'):
        return ord(decoded[0])
    return ord(decoded)


def decode_wchars(wchars: str) -> str:
    return wchars.encode('ascii').decode('unicode_escape')


def load_ucs_detect_yaml():
    items = []
    for yaml_path in sorted(glob.glob(os.path.join(PATH_UCS_DETECT_DATA, '*.yaml'))):
        with open(yaml_path, encoding='utf-8') as f:
            doc = yaml.load(f, Loader=SafeLoader)
        name = doc.get('software_name', '')
        ver = doc.get('software_version', '')
        canonical = canonical_name(name, ver)
        items.append((os.path.basename(yaml_path), canonical, doc))
    return items


SINGLE_CP_CATEGORIES = (
    ('unicode_wide_results', 'WIDE'),
    ('narrow_results', 'NARROW'),
    ('sri_results', 'SRI'),
    ('sfz_results', 'SFZ'),
    ('emoji_vs16_results', 'VS16'),
    ('emoji_vs15_results', 'VS15'),
)

GRAPHEME_CATEGORIES = (
    ('emoji_zwj_results', 'ZWJ'),
    ('ri_results', 'RI'),
)

LANG_CATEGORY_KEY = 'language_results'
LANG_CATEGORY_LABEL = 'LANG'

ALL_LABELS = tuple(label for _, label in SINGLE_CP_CATEGORIES) \
    + tuple(label for _, label in GRAPHEME_CATEGORIES) \
    + (LANG_CATEGORY_LABEL,)


def hash_key(data) -> str:
    return hashlib.sha256(repr(data).encode()).hexdigest()[:8]


def get_gc_status(doc: dict) -> str:
    """Return graphene clustering status: 'on', 'off', or '?'."""
    terminal_results = doc.get('terminal_results')
    if terminal_results is None:
        return '?'
    modes = terminal_results.get('modes')
    if modes is None:
        return '?'
    mode_2027 = modes.get(2027) or modes.get('2027')
    if mode_2027 is None:
        return '?'
    if mode_2027.get('supported') and mode_2027.get('enabled'):
        return 'on'
    return 'off'


def analyze():
    # corrections[canonical][label] = set of correction tuples
    corrections: dict[str, dict[str, set]] = defaultdict(lambda: defaultdict(set))
    all_canonicals: set[str] = set()
    canonical_gc: dict[str, str] = {}

    for _fname, canonical, doc in load_ucs_detect_yaml():
        all_canonicals.add(canonical)
        # Use the first GC status seen for a canonical (should be consistent
        # since same engine), but if 'on' appears, upgrade.
        gc = get_gc_status(doc)
        if canonical not in canonical_gc or gc == 'on':
            canonical_gc[canonical] = gc

        test_results = doc.get('test_results', {})

        for yaml_key, label in SINGLE_CP_CATEGORIES:
            cat_data = test_results.get(yaml_key, {})
            for _ver, ver_data in cat_data.items():
                for entry in ver_data.get('failed_codepoints', []):
                    if 'inherited_from' in entry:
                        continue
                    ucs = parse_wchar_codepoint(entry['wchar'])
                    term_w = entry['measured_by_terminal']
                    wc_w = entry['measured_by_wcwidth']
                    corrections[canonical][label].add((ucs, term_w, wc_w))

        for yaml_key, label in GRAPHEME_CATEGORIES:
            cat_data = test_results.get(yaml_key, {})
            for _ver, ver_data in cat_data.items():
                for entry in ver_data.get('failed_codepoints', []):
                    if 'inherited_from' in entry:
                        continue
                    decoded = decode_wchars(entry['wchar'])
                    term_w = entry['measured_by_terminal']
                    wc_w = entry['measured_by_wcwidth']
                    corrections[canonical][label].add((decoded, term_w, wc_w))

        lang_data = test_results.get(LANG_CATEGORY_KEY) or {}
        for _lang_name, lang_entry in lang_data.items():
            if lang_entry is None:
                continue
            for entry in lang_entry.get('failed', []):
                if 'inherited_from' in entry:
                    continue
                decoded = decode_wchars(entry['wchars'])
                term_w = entry['measured_by_terminal']
                wc_w = entry['measured_by_wcwidth']
                corrections[canonical][LANG_CATEGORY_LABEL].add((decoded, term_w, wc_w))

    # group: GC status -> dict[label -> set of hashes]
    groups: dict[str, dict[str, set[str]]] = {
        gc: {label: set() for label in ALL_LABELS}
        for gc in ('on', 'off', '?')
    }
    group_counts: dict[str, int] = {'on': 0, 'off': 0, '?': 0}

    for canonical in sorted(all_canonicals):
        gc = canonical_gc.get(canonical, '?')
        group_counts[gc] += 1
        for label in ALL_LABELS:
            corr = corrections[canonical].get(label, set())
            hk = hash_key(sorted(corr))
            groups[gc][label].add(hk)

    print('DEC 2027: on=grapheme clustering, off=not supported/disabled, ?=not probed')
    print()
    for gc, label in [('on', 'GC=on'), ('off', 'GC=off'), ('?', 'GC=?')]:
        n = group_counts[gc]
        print(f'  {label} ({n} terminals):')
        for feature in ALL_LABELS:
            n_uniq = len(groups[gc][feature])
            print(f'    {feature:7s}  {n_uniq} unique')
        print()


if __name__ == '__main__':
    analyze()
