#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ucs-detect: Test and report Unicode support level of a terminal emulator.

See also,
- https://github.com/jquast/wcwidth
- https://github.com/jquast/blessed

This code comes from experimentation while developing the python 'wcwidth'
library. The primary purpose is to verify correctness in that library and
evaluating the unicode version and support level of a terminal emulator.

This is achieved by testing the terminal's ability to render a variety of
Unicode characters, and measuring the distance of the cursor after each
character is written to the terminal, using the `Cursor Position Report
<https://vt100.net/docs/vt510-rm/CPR.html>`_ terminal escape sequence
using :meth:`blessed.Terminal.get_location`.
"""
# std imports
import os
import sys
import time
import locale
import argparse
import functools
import platform
import datetime

# 3rd party
import blessed
import wcwidth
import yaml

# local
from ucs_detect.table_zwj import EMOJI_ZWJ_SEQUENCES
from ucs_detect.table_wide import WIDE_CHARACTERS
from ucs_detect.table_vs16 import VS16_NARROW_TO_WIDE
from ucs_detect.table_vs15 import VS15_WIDE_TO_NARROW
from ucs_detect.table_lang import LANG_GRAPHEMES
from ucs_detect import measure, terminal
from ucs_detect.error_matcher import ErrorMatcher



def merge_results(base_results, additional_results):
    """Merge two test result dictionaries."""
    merged = {}
    all_versions = set(base_results.keys()) | set(additional_results.keys())

    for ver in all_versions:
        base = base_results.get(ver, {})
        additional = additional_results.get(ver, {})

        n_total = base.get('n_total', 0) + additional.get('n_total', 0)
        n_errors = base.get('n_errors', 0) + additional.get('n_errors', 0)

        failed_codepoints = (
            base.get('failed_codepoints', []) + additional.get('failed_codepoints', [])
        )

        base_time = base.get('seconds_elapsed', 0.0)
        additional_time = additional.get('seconds_elapsed', 0.0)
        total_time = base_time + additional_time

        merged[ver] = {
            'n_total': n_total,
            'n_errors': n_errors,
            'pct_success': ((n_total - n_errors) / n_total * 100) if n_total else 0,
            'seconds_elapsed': total_time,
            'codepoints_per_second': (n_total / total_time) if total_time > 0 else 0.0,
            'failed_codepoints': failed_codepoints,
        }

    return merged


def init_term(stream):
    locale.setlocale(locale.LC_ALL, "")
    from ucs_detect.terminal import make_terminal
    stream_arg = sys.__stderr__ if stream == "stderr" else None
    term = make_terminal(stream=stream_arg)
    writer = functools.partial(
        print, end="", flush=True, file=sys.stderr if stream == "stderr" else None
    )
    return term, writer


def run(stream, limit_codepoints, limit_errors, limit_graphemes, limit_graphemes_pct, limit_codepoints_wide_pct, include_uncommon_codepoints, save_yaml, no_terminal_test, no_languages_test, timeout_cps, timeout_query, stop_at_error, set_software_name, set_software_version, limit_category_time=0, cursor_report_delay_ms=0, detect_all_dec_modes=False, test_only="all", **_kwargs):
    """Program entry point."""

    def _should_run(*categories):
        return test_only == "all" or test_only in categories

    term, writer = init_term(stream)

    error_matcher = ErrorMatcher(stop_at_error)

    local_vars = locals().copy()
    session_arguments = {
        k: local_vars[k]
        for k in ("stream", "limit_codepoints", "limit_errors", "limit_graphemes",
                  "limit_graphemes_pct", "limit_category_time")
    }
    writer(f"ucs-detect: {display_args(session_arguments)})")

    cps_tracker = measure.CPSTracker()

    with cps_tracker.timing() as done_ok:
        if measure.get_location_with_retry(term, timeout_cps) == (-1, -1):
            raise RuntimeError(
                f"Not a terminal or Timeout exceeded"
                f" ({timeout_cps:.1f}s)!")
        done_ok()

    writer("\nucs-detect: Interactive terminal detected!")

    with cps_tracker.timing(2) as done_ok:
        unicode_width = measure.measure_width(
            term, writer, '\u231A', timeout_cps)
        if unicode_width is not None:
            done_ok()
    has_unicode = (unicode_width == 2)
    if not has_unicode:
        writer("\nucs-detect: " + term.bold_red(
            "This terminal does not appear to support"
            " Unicode wide characters."
        ))
        writer(f"\nucs-detect: measured width of"
               f" U+231A WATCH: {unicode_width}")

    ambig_label = None
    ambiguous_width = -1
    if has_unicode:
        with cps_tracker.timing() as done_ok:
            ambiguous_width = term.detect_ambiguous_width(
                timeout=timeout_cps, fallback=-1)
            if ambiguous_width != -1:
                done_ok()
        if ambiguous_width == -1:
            ambig_label = "unknown"
        elif ambiguous_width == 2:
            ambig_label = "wide (2)"
        else:
            ambig_label = "narrow (1)"
        writer(f"\nucs-detect: Ambiguous width: {ambig_label}")

    terminal_results = {}
    if _should_run("terminal"):
        if not no_terminal_test or test_only == "terminal":
            terminal_results = terminal.do_terminal_detection(
                all_modes=detect_all_dec_modes,
                cursor_report_delay_ms=cursor_report_delay_ms,
                timeout=timeout_query,
                cps_tracker=cps_tracker,
            )

    if save_yaml:
        print()
        if set_software_name:
            terminal_software = set_software_name
        elif terminal_results.get("software_name", "").strip():
            default_software = terminal_results["software_name"].strip()
            terminal_software = input(f'Enter "Terminal Software" (press return for "{default_software}"): ')
            if not terminal_software.strip():
                terminal_software = default_software
        else:
            terminal_software = input('Enter "Terminal Software": ')

        if set_software_version:
            terminal_version = set_software_version
        elif terminal_results.get("software_version", "").strip():
            default_software_version = terminal_results["software_version"].strip()
            terminal_version = input(f'Enter "Software Version" (press return for "{default_software_version}"): ')
            if not terminal_version.strip():
                terminal_version = default_software_version
        else:
            terminal_version = input('Enter "Software Version": ')

    start_time = time.monotonic()

    wide_results = {}
    emoji_zwj_results = {}
    emoji_vs16_results = {}
    emoji_vs15_results = {}
    language_results = None

    if has_unicode:
        test_kwargs = dict(
            term=term, writer=writer, timeout=timeout_cps,
            limit_codepoints=limit_codepoints, limit_errors=limit_errors,
            limit_category_time=limit_category_time,
            stop_at_error=error_matcher,
            cursor_report_delay_ms=cursor_report_delay_ms,
            cps_tracker=cps_tracker,
        )

        with term.cbreak():

            if _should_run("unicode", "wide"):
                wide_results = measure.test_support(
                    table=WIDE_CHARACTERS, expected_width=2,
                    test_type="wide", label="WIDE",
                    limit_pct=limit_codepoints_wide_pct,
                    include_uncommon=include_uncommon_codepoints,
                    **test_kwargs,
                )

            if _should_run("unicode", "zwj"):
                emoji_zwj_results = measure.test_support(
                    table=EMOJI_ZWJ_SEQUENCES, expected_width=2,
                    test_type="zwj", label="ZWJ", **test_kwargs,
                )

            if _should_run("unicode", "vs16"):
                vs16_time = (limit_category_time / 2
                             if limit_category_time else 0)
                emoji_vs16_results = merge_results(
                    measure.test_support(
                        table=VS16_NARROW_TO_WIDE, expected_width=2,
                        test_type="vs16",
                        label="Variation Selector-16",
                        **{**test_kwargs,
                           'limit_category_time': vs16_time},
                    ),
                    measure.test_support(
                        table=tuple(
                            (ver, tuple(seq[0] for seq in sequences))
                            for ver, sequences in VS16_NARROW_TO_WIDE),
                        expected_width=1, suppress_output=True,
                        test_type="vs16n",
                        **{**test_kwargs,
                           'limit_category_time': vs16_time},
                    ),
                )

            if _should_run("unicode", "vs15"):
                emoji_vs15_results = measure.test_support(
                    table=VS15_WIDE_TO_NARROW, expected_width=1,
                    test_type="vs15",
                    label="Variation Selector-15",
                    **test_kwargs,
                )

            if _should_run("lang") and not no_languages_test:
                language_results = measure.test_language_support(
                    LANG_GRAPHEMES, term, writer, timeout_cps,
                    limit_graphemes, limit_errors, error_matcher,
                    limit_category_time=limit_category_time,
                    limit_graphemes_pct=limit_graphemes_pct,
                    cps_tracker=cps_tracker,
                    cursor_report_delay_ms=cursor_report_delay_ms,
                )

    elapsed = time.monotonic() - start_time

    # prefer user-entered software name/version over automatic detection
    if save_yaml:
        if terminal_software:
            terminal_results['software_name'] = terminal_software
        if terminal_version:
            terminal_results['software_version'] = terminal_version

    display_results(
        term, writer, ambig_label,
        terminal_results=terminal_results,
        wide_results=wide_results,
        emoji_zwj_results=emoji_zwj_results,
        emoji_vs16_results=emoji_vs16_results,
        emoji_vs15_results=emoji_vs15_results,
        language_results=language_results,
        elapsed=elapsed,
        has_unicode=has_unicode,
    )

    if save_yaml:
        if (sys.version_info.major, sys.version_info.minor) > (3, 10):
            date_now = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M:%S UTC")
        else:
            date_now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        do_save_yaml(
            save_yaml,
            session_arguments=session_arguments,
            software_name=terminal_software,
            software_version=terminal_version,
            seconds_elapsed=time.monotonic() - start_time,
            width=term.width,
            height=term.height,
            ambiguous_width=ambiguous_width,
            python_version=platform.python_version(),
            system=platform.system(),
            datetime=date_now,
            wcwidth_version=wcwidth.__version__,
            test_results=dict(
                unicode_wide_results=wide_results,
                emoji_zwj_results=emoji_zwj_results,
                emoji_vs16_results=emoji_vs16_results,
                emoji_vs15_results=emoji_vs15_results,
                language_results=language_results,
            ),
            terminal_results=terminal_results,
        )
    writer('\n')


def display_args(arguments):
    return ", ".join(f"{k}={v}" for k, v in arguments.items())


def _pct_style(term, pct_val):
    """Return terminal style callable for a percentage value."""
    return (
        term.firebrick1 if pct_val < 33
        else term.darkorange1 if pct_val < 50
        else term.yellow if pct_val < 66
        else term.greenyellow if pct_val < 99
        else term.green2
    )


def color_pct(term, pct_val):
    """Apply color to a percentage value based on success thresholds."""
    return _pct_style(term, pct_val)(f"{pct_val:0.1f} %")


def _use_color_table(term):
    """Return True if terminal supports enough colors for ColorTable."""
    return term.does_styling and term.number_of_colors >= 16


def _make_table(term):
    """Create a ColorTable with cyan theme, or plain PrettyTable for basic terminals."""
    if _use_color_table(term):
        from prettytable.colortable import ColorTable, Theme
        return ColorTable(theme=Theme(
            default_color=term.cyan,
            vertical_color="",
            horizontal_color="",
            junction_color="",
        ))
    from prettytable import PrettyTable
    return PrettyTable()


def _set_double_border(table, has_unicode=True):
    """Apply CP437 double-line border characters, or ASCII fallback."""
    if not has_unicode:
        return
    table.horizontal_char = '═'
    table.vertical_char = '║'
    table.junction_char = '╬'
    table.top_junction_char = '╦'
    table.bottom_junction_char = '╩'
    table.left_junction_char = '╠'
    table.right_junction_char = '╣'
    table.top_left_junction_char = '╔'
    table.top_right_junction_char = '╗'
    table.bottom_left_junction_char = '╚'
    table.bottom_right_junction_char = '╝'


def _color_yes_no(term, value, suffix=""):
    """Apply green/red coloring to boolean-like values."""
    if value:
        return term.green2("Yes") + suffix
    return term.firebrick1("No")


def _build_terminal_kv_pairs(term, results):
    """Build (key, value) tuples for terminal dimensions and graphics."""
    pairs = []
    if not results:
        return pairs

    if ttype := results.get('ttype'):
        pairs.append(("Terminal Type", ttype))

    if software := results.get('software_name'):
        if ver := results.get('software_version'):
            software += f" {ver}"
        if len(software) > 15:
            software = software[:14] + '…'
        pairs.append(("Software", software))

    if (n_colors := results.get('number_of_colors')) is not None:
        if n_colors >= 16777216:
            color_str = term.green2("24-bit")
        elif n_colors <= 256:
            color_str = term.firebrick1(f"{n_colors:n}")
        else:
            color_str = term.yellow(f"{n_colors:n}")
        pairs.append(("Colors", color_str))

    if results.get('width') and results.get('height'):
        pairs.append(("Size (cells)", f"{results['width']} x {results['height']}"))

    if results.get('pixels_width') and results.get('pixels_height'):
        pairs.append(("Size (pixels)",
                       f"{results['pixels_width']} x {results['pixels_height']}"))

    if results.get('cell_width') and results.get('cell_height'):
        pairs.append(("Cell Size (pixels)",
                       f"{results['cell_width']} x {results['cell_height']}"))

    if ratio_info := results.get('screen_ratio'):
        if ratio_name := results.get('screen_ratio_name'):
            ratio_info += f" ({ratio_name})"
        pairs.append(("Aspect Ratio", ratio_info))

    if (tab_w := results.get('tab_stop_width')) is not None:
        pairs.append(("Tab Stop Width", str(tab_w)))

    if fg := results.get('foreground_color_rgb'):
        r8, g8, b8 = (fg[0] >> 8, fg[1] >> 8, fg[2] >> 8)
        swatch = term.color_rgb(r8, g8, b8)('█')
        pairs.append(("Foreground",
                       f"#{r8:02x}{g8:02x}{b8:02x} [{swatch}]"))

    if bg := results.get('background_color_rgb'):
        r8, g8, b8 = (bg[0] >> 8, bg[1] >> 8, bg[2] >> 8)
        swatch = term.color_rgb(r8, g8, b8)('█')
        pairs.append(("Background",
                       f"#{r8:02x}{g8:02x}{b8:02x} [{swatch}]"))

    has_kitty_gfx = results.get('kitty_graphics', False)
    has_iterm2_gfx = results.get('iterm2_features', {}).get('supported', False)
    has_sixel = results.get('sixel', False)
    if has_kitty_gfx or has_iterm2_gfx:
        protocols = []
        if has_kitty_gfx:
            protocols.append("Kitty")
        if has_iterm2_gfx:
            protocols.append("iTerm2")
        if has_sixel:
            protocols.append("Sixel")
        pairs.append(("Graphics?", term.green2(", ".join(protocols))))
    elif has_sixel:
        pairs.append(("Graphics?", term.yellow("Sixel")))
    elif any(k in results for k in ('sixel', 'kitty_graphics', 'iterm2_features')):
        pairs.append(("Graphics?", term.firebrick1("No")))

    if da := results.get('device_attributes'):
        if (sc := da.get('service_class')) is not None:
            service_class_names = {
                1: "VT100",
                2: "VT200",
                18: "VT330",
                41: "VT420",
                61: "VT500",
                62: "VT500",
                64: "VT500",
                65: "VT500",
            }
            label = service_class_names.get(sc, f"Class {sc}")
            pairs.append(("Device Class", label))

    return pairs


def _build_capabilities_kv_pairs(term, results):
    """Build (key, value) tuples for terminal capabilities."""
    pairs = []
    if not results:
        return pairs

    if modes := results.get('modes'):
        notable_modes = [
            (2004, "Bracketed Paste?"),
            (2026, "Synchronized Output?"),
            (1004, "Focus Events?"),
            (1006, "Mouse SGR?"),
        ]
        for mode_num, mode_label in notable_modes:
            mode_key = str(mode_num) if str(mode_num) in modes else mode_num
            if mode_key in modes:
                m = modes[mode_key]
                pairs.append((mode_label,
                               _color_yes_no(term, m.get('supported'))))
            else:
                pairs.append((mode_label, term.yellow("N/A")))

    if results.get('kitty_keyboard') is not None:
        pairs.append(("Kitty Keyboard?", _color_yes_no(term, True)))
    elif results.get('modes'):
        pairs.append(("Kitty Keyboard?", _color_yes_no(term, False)))

    iterm2 = results.get('iterm2_features', {})
    if iterm2.get('supported'):
        features = iterm2.get('features', {})
        pairs.append(("iTerm2 Features?",
                       _color_yes_no(term, True, f" ({len(features)})")))
    elif 'iterm2_features' in results:
        pairs.append(("iTerm2 Features?", _color_yes_no(term, False)))

    ts = results.get('text_sizing', {})
    if ts.get('width') or ts.get('scale'):
        parts = []
        if ts.get('width'):
            parts.append('width')
        if ts.get('scale'):
            parts.append('scale')
        pairs.append(("Kitty Text Sizing?", term.green2('+'.join(parts))))
    elif 'text_sizing' in results:
        pairs.append(("Kitty Text Sizing?", _color_yes_no(term, False)))

    xtgettcap = results.get('xtgettcap', {})
    if not xtgettcap.get('supported') and 'xtgettcap' in results:
        pairs.append(("XTGETTCAP?", _color_yes_no(term, False)))

    notif = results.get('kitty_notifications')
    if isinstance(notif, dict) and notif.get('supported'):
        pairs.append(("Kitty Notifications?", _color_yes_no(term, True)))
    elif 'kitty_notifications' in results:
        pairs.append(("Kitty Notifications?", _color_yes_no(term, False)))

    if 'kitty_clipboard_protocol' in results:
        pairs.append(("Kitty Clipboard?",
                       _color_yes_no(term, results['kitty_clipboard_protocol'])))

    pointer = results.get('kitty_pointer_shapes')
    if isinstance(pointer, dict) and pointer.get('supported'):
        current = pointer.get('current', '')
        label = term.green2("Yes")
        if current:
            label += f" ({current})"
        pairs.append(("Kitty Pointer Shapes?", label))
    elif 'kitty_pointer_shapes' in results:
        pairs.append(("Kitty Pointer Shapes?", _color_yes_no(term, False)))

    pairs.sort(key=lambda p: p[0].lower())
    return pairs



def _build_test_kv_pairs(term, ambig_label, **result_sets):
    """Build (key, value) tuples from test results."""
    has_unicode = result_sets.get("has_unicode", True)
    pairs = []

    wide = result_sets.get("wide_results", {})
    zwj = result_sets.get("emoji_zwj_results", {})
    vs16 = result_sets.get("emoji_vs16_results", {})
    vs15 = result_sets.get("emoji_vs15_results", {})

    for name, data in [("WIDE", wide), ("ZWJ", zwj), ("VS16", vs16), ("VS15", vs15)]:
        if data:
            for label, d in data.items():
                pct_val = d["pct_success"]
                pct = color_pct(term, pct_val)
                if sp := d.get("sampled_pct"):
                    pct += f" ({sp}% sampled)"
                pairs.append((name, pct))

    langs = result_sets.get("language_results")
    if langs:
        n_langs = len(langs)
        n_pass = sum(1 for l in langs if langs[l]["pct_success"] == 100.0)
        lang_pct = n_pass / n_langs * 100 if n_langs else 0
        lang_val = color_pct(term, lang_pct)
        first_lang = next(iter(langs.values()), {})
        if sp := first_lang.get("sampled_pct"):
            lang_val += f" ({sp}% sampled)"
        pairs.append(("Languages", lang_val))

    if ambig_label is not None:
        pairs.insert(0, ("Ambiguous Width", ambig_label))

    modes = result_sets.get("modes", {})
    mode_2027 = modes.get(2027, modes.get("2027"))
    if mode_2027 is not None:
        gc_value = _color_yes_no(term, mode_2027.get('supported'))
        pairs.insert(1, ("Mode 2027 (graphemes)", gc_value))
    elif modes:
        pairs.insert(1, ("Mode 2027 (graphemes)", term.yellow("N/A")))


    return pairs


def _make_kv_table(term, title, pairs, has_unicode=True):
    """Build a table from (key, value) tuples."""
    table = _make_table(term)
    _set_double_border(table, has_unicode)
    table.title = term.magenta(title)
    table.field_names = ["Attribute", "Value"]
    table.align["Attribute"] = "r"
    table.align["Value"] = "l"
    table.header = False
    table.max_table_width = max(40, term.width - 1)
    for key, value in pairs:
        if key is None:
            table.add_row(["", value])
        else:
            table.add_row([key, value])
    return table


def _truncate_value(val_str, max_len=25):
    """Truncate a string with ellipsis if it exceeds max_len."""
    if len(val_str) > max_len:
        return val_str[:max_len - 1] + '…'
    return val_str


def make_xtgettcap_lines(term, capabilities, has_unicode=True):
    """Build multi-column XTGETTCAP output lines that tile to fit terminal width."""
    import math
    from ucs_detect.table_xtgettcap import XTGETTCAP_CAPABILITIES

    cap_info = {name: desc for name, desc in XTGETTCAP_CAPABILITIES}
    sorted_caps = [(name, capabilities[name]) for name in sorted(capabilities)]
    n_caps = len(sorted_caps)

    if n_caps == 0:
        return []

    # build one full table to get consistent column widths
    full_table = _make_table(term)
    _set_double_border(full_table, has_unicode)
    full_table.title = term.magenta(f"XTGETTCAP ({n_caps} capabilities)")
    full_table.field_names = [
        term.magenta("Cap"),
        term.magenta("Description"),
        term.magenta("Value"),
    ]
    full_table.align["Cap"] = "l"
    full_table.align["Description"] = "l"
    full_table.align["Value"] = "l"
    full_table.max_table_width = max(40, term.width - 1)
    for capname, value in sorted_caps:
        desc = cap_info.get(capname, capname)
        full_table.add_row([capname, desc, _truncate_value(repr(value))])

    # render and split into lines
    all_rendered = str(full_table).split("\n")
    # all_rendered: [top_border, title, title_border, header, header_border,
    #                row0, row1, ..., bottom_border]
    # find where data rows start (after header separator)
    tbl_width = len(all_rendered[0])
    n_columns = max(1, (term.width - 1) // (tbl_width + 1))

    if n_columns <= 1:
        return all_rendered

    # split: title+header lines, data rows, bottom border
    header_lines = all_rendered[:5]
    data_lines = all_rendered[5:-1]
    bottom_border = all_rendered[-1]

    rows_per_col = math.ceil(len(data_lines) / n_columns)
    chunks = []
    for i in range(n_columns):
        chunk = data_lines[i * rows_per_col:(i + 1) * rows_per_col]
        if not chunk:
            break
        chunks.append(chunk)

    # pad shorter chunks with empty rows
    max_rows = len(chunks[0])
    vbar = "║" if has_unicode else "|"
    empty_row = vbar + " " * (tbl_width - 2) + vbar
    for chunk in chunks:
        while len(chunk) < max_rows:
            chunk.append(empty_row)

    # first chunk gets title+header, others get header padded to same height
    # header_lines: [top_border, title, title_sep, header, header_sep]
    # header_no_title needs blank spacers for title rows
    blank_spacer = " " * tbl_width
    header_no_title = [
        blank_spacer,                # align with top_border (title row 1)
        blank_spacer,                # align with title row
        header_lines[0],             # top border
        header_lines[3],             # header
        header_lines[4],             # header separator
    ]
    output = []

    # title+header for first, padded header for rest
    for row_idx in range(len(header_lines)):
        parts = [header_lines[row_idx]]
        for chunk_idx in range(1, len(chunks)):
            parts.append(header_no_title[row_idx])
        output.append(" ".join(parts))

    # data rows side by side
    for row_idx in range(max_rows):
        parts = [chunks[i][row_idx] for i in range(len(chunks))]
        output.append(" ".join(parts))

    # bottom border
    output.append(" ".join([bottom_border] * len(chunks)))

    return output


def _make_one_language_table(term, title, failed_langs, results, has_unicode):
    """Build a single language table from a list of failed language names."""
    table = _make_table(term)
    _set_double_border(table, has_unicode)
    table.title = term.magenta(title)
    table.field_names = [
        term.magenta("Language"),
        term.magenta("Total"),
        term.magenta("Failures"),
        term.magenta("Success"),
    ]
    table.align["Language"] = "l"
    table.align["Total"] = "r"
    table.align["Failures"] = "r"
    table.align["Success"] = "r"
    for lang in failed_langs:
        data = results[lang]
        table.add_row([
            lang,
            f"{data['n_total']:n}",
            f"{data['n_errors']:n}",
            color_pct(term, data["pct_success"]),
        ])
    return table


def make_language_tables(term, results, has_unicode=True):
    """Build language table string(s), splitting into columns when >12 failures."""
    import math
    success_langs = [
        lang for lang in results if results[lang]["pct_success"] == 100.0
    ]
    failed_langs = sorted(
        lang for lang in results if results[lang]["pct_success"] < 100.0
    )
    n_langs = len(success_langs) + len(failed_langs)
    title = f"Language Support ({len(success_langs)} of {n_langs} passed)"
    n_failed = len(failed_langs)
    max_w = max(40, term.width - 1)

    if n_failed <= 12:
        tbl = _make_one_language_table(
            term, title, failed_langs, results, has_unicode)
        tbl.max_table_width = max_w
        return [str(tbl)]

    # build one table to measure its width, then determine column count
    probe = _make_one_language_table(
        term, title, failed_langs, results, has_unicode)
    probe.max_table_width = max_w
    probe_width = len(str(probe).split("\n")[0])
    n_cols = max(1, (term.width - 1) // (probe_width + 1))
    rows_per_col = math.ceil(n_failed / n_cols)
    table_strings = []
    for i in range(n_cols):
        chunk = failed_langs[i * rows_per_col:(i + 1) * rows_per_col]
        if not chunk:
            break
        col_title = title if i == 0 else f"({i + 1})"
        tbl = _make_one_language_table(
            term, col_title, chunk, results, has_unicode)
        tbl.max_table_width = max_w
        table_strings.append(str(tbl))
    return table_strings



def _collect_side_by_side_lines(term, table_strings):
    """Collect side-by-side table output as a list of lines."""
    tables = [s for s in table_strings if s]
    if not tables:
        return []
    all_lines = []
    row = []
    row_width = 0
    for tbl in tables:
        lines = tbl.split("\n")
        tbl_width = len(lines[0])
        needed = (row_width + 1 + tbl_width) if row else tbl_width
        if row and needed >= term.width:
            all_lines.extend(_collect_table_row_lines(row))
            row = []
            row_width = 0
        row.append((lines, tbl_width))
        row_width = (row_width + 1 + tbl_width) if len(row) > 1 else tbl_width
    if row:
        all_lines.extend(_collect_table_row_lines(row))
    return all_lines


def _collect_table_row_lines(row):
    """Collect one horizontal row of side-by-side tables as lines."""
    result = []
    max_height = max(len(lines) for lines, _ in row)
    for i in range(max_height):
        parts = []
        for lines, width in row:
            line = lines[i] if i < len(lines) else ""
            parts.append(f"{line:<{width}}")
        result.append(" ".join(parts))
    result.append("")
    return result


def _write_line(term, writer, line):
    """Write a line, truncating to terminal width and omitting trailing newline when needed."""
    if term.width and term.length(line) >= term.width:
        line = term.truncate(line, term.width - 1)
    writer(line)
    if not term.width or term.length(line) < term.width:
        writer("\n")


def _paginated_write(term, writer, all_lines):
    """Write lines to terminal."""
    writer("\n")
    if not term.does_styling or not term.height:
        for line in all_lines:
            writer(line + "\n")
    else:
        for line in all_lines:
            _write_line(term, writer, line)


def display_results(term, writer, ambig_label, terminal_results=None,
                    elapsed=None, has_unicode=True, **result_sets):
    """Display all test results as prettytable key-value tables."""
    result_sets["elapsed"] = elapsed
    result_sets["has_unicode"] = has_unicode
    results = terminal_results or {}
    terminal_pairs = _build_terminal_kv_pairs(term, results)
    caps_pairs = _build_capabilities_kv_pairs(term, results)
    result_sets["modes"] = results.get("modes", {})
    test_pairs = _build_test_kv_pairs(term, ambig_label, **result_sets)

    all_lines = []

    xtgettcap = (results.get('xtgettcap') or {}).get('capabilities', {})
    if xtgettcap:
        all_lines.extend(make_xtgettcap_lines(term, xtgettcap, has_unicode))
        all_lines.append("")

    maxwidth = max(40, term.width - 1) // 2

    # primary table: terminal info + unicode tests, with a capability count
    primary_pairs = []
    if terminal_pairs:
        primary_pairs.extend(terminal_pairs)
    if caps_pairs:
        n_yes = sum(1 for _, v in caps_pairs if 'Yes' in v)
        n_total = len(caps_pairs)
        pct = (n_yes / n_total * 100) if n_total else 0
        colored = _pct_style(term, pct)(f"{n_yes} of {n_total}")
        cap_summary = term.link('#capabilities', colored)
        primary_pairs.append(("Capabilities", cap_summary))
    if test_pairs:
        primary_pairs.append((None, wcwidth.center(
            term.magenta("Unicode"), maxwidth, '-')))
        primary_pairs.extend(test_pairs)

    # secondary table: detailed capabilities
    secondary_pairs = []
    if caps_pairs:
        secondary_pairs.extend(caps_pairs)

    table_strings = []
    if primary_pairs:
        table_strings.append(
            str(_make_kv_table(term, "Terminal Capabilities",
                               primary_pairs, has_unicode)))
    if secondary_pairs:
        table_strings.append(
            str(_make_kv_table(term, "Terminal Capabilities (2)",
                               secondary_pairs, has_unicode)))

    all_lines.extend(_collect_side_by_side_lines(term, table_strings))

    langs = result_sets.get("language_results")
    if langs:
        failed = [l for l in langs if langs[l]["pct_success"] < 100.0]
        if failed:
            lang_table_strings = make_language_tables(term, langs, has_unicode)
            all_lines.extend(
                _collect_side_by_side_lines(term, lang_table_strings))

    _paginated_write(term, writer, all_lines)
    writer(term.normal)


def do_save_yaml(save_yaml, **kwargs):
    # Ensure software_version is always stored as a string in YAML,
    # otherwise yaml.safe_dump serializes "3.5" as a float.
    if 'software_version' in kwargs:
        kwargs['software_version'] = str(kwargs['software_version'])
    with open(save_yaml, "w", encoding='utf-8') as fout:
        yaml.safe_dump(
            kwargs, fout,
            sort_keys=True,
            allow_unicode=True,
            default_flow_style=False,
        )


def parse_args():
    args = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args.add_argument(
        "--stream",
        default="stderr",
        choices=("stderr", "stdout"),
        help="file descriptor to interact with during testing",
    )
    args.add_argument(
        "--limit-codepoints",
        type=int,
        default=0,
        help="limit the total number of codepoints per category (0=unlimited)",
    )
    args.add_argument(
        "--limit-graphemes",
        type=int,
        default=0,
        dest="limit_graphemes",
        help="limit the total number of graphemes tested for each language (0=unlimited)",
    )
    args.add_argument(
        "--limit-graphemes-pct",
        type=int,
        default=0,
        help=(
            "sample percentage of graphemes to test per language (1-100, 0=unlimited). "
            "A stride-based sample of 1-in-every-N is tested"
        ),
    )
    args.add_argument(
        "--limit-errors",
        type=int,
        default=0,
        help="limit the total number of errors for each tested version or language (0=unlimited)",
    )
    args.add_argument(
        "--limit-category-time",
        type=float,
        default=0,
        help="time budget in seconds per test category, auto-adjusts sampling (0=unlimited)",
    )
    args.add_argument(
        "--limit-codepoints-wide-pct",
        type=int,
        default=0,
        help=(
            "sample percentage of WIDE codepoints to test (1-100, 0=unlimited). "
            "Due to the large number of WIDE codepoints (~183k), a stride-based "
            "sample of 1-in-every-N is tested by default"
        ),
    )
    args.add_argument(
        "--include-uncommon-codepoints",
        action="store_true",
        default=False,
        help=("Include uncommon codepoints in WIDE testing."),
    )
    args.add_argument(
        "--save-yaml",
        default=None,
        help="Save test results to given filepath as yaml, will prompt for software name & version",
    )
    args.add_argument(
        "--no-terminal-test",
        action="store_true",
        default=False,
        help="Do not perform any additional terminal fingerprinting"
    )
    args.add_argument(
        "--no-languages-test",
        action="store_true",
        default=False,
        help="Do not perform language support testing"
    )
    args.add_argument(
        "--timeout-cps",
        type=float,
        default=1.0,
        help="Timeout in seconds for cursor position reports during testing",
    )
    args.add_argument(
        "--timeout-query",
        type=float,
        default=0.2,
        help="Timeout in seconds for terminal capability queries",
    )
    args.add_argument(
        "--stop-at-error",
        default=None,
        help=(
            "Interactively stop and display details when matching errors occur. "
            "Values: 'all' (any error), 'zwj', 'wide', 'vs16', 'vs16n', 'vs15', "
            "'lang' (all languages), or specific language name (e.g., 'english')"
        )
    )
    args.add_argument(
        "--test-only",
        default="all",
        choices=("all", "unicode", "terminal", "wide", "zwj", "vs16", "vs15", "lang"),
        help="Run only the specified test category",
    )
    args.add_argument(
        "--cursor-report-delay-ms",
        type=int,
        default=0,
        help="Delay in milliseconds before reading cursor position report",
    )
    args.add_argument(
        "--detect-all-dec-modes",
        action="store_true",
        default=False,
        help="Query all known DEC private modes (slow, default queries only notable modes)",
    )
    args.add_argument(
        "--set-software-name",
        default=None,
        help="Set software name for YAML output (skips interactive prompt)"
    )
    args.add_argument(
        "--set-software-version",
        default=None,
        help="Set software version for YAML output (skips interactive prompt)"
    )
    args.add_argument(
        "--rerun",
        default=None,
        metavar="YAML_FILE",
        help="Re-run ucs-detect using arguments from a saved YAML file"
    )
    results = vars(args.parse_args())
    if results["rerun"]:
        results = _apply_rerun_yaml(results)
    if results["save_yaml"]:
        results["save_yaml"] = os.path.expanduser(results["save_yaml"])
    return results


def _apply_rerun_yaml(results):
    """Merge session arguments from a saved YAML file into *results*."""
    yaml_path = os.path.expanduser(results["rerun"])
    with open(yaml_path, encoding='utf-8') as fin:
        data = yaml.safe_load(fin)

    session_args = data.get('session_arguments', {})
    yaml_to_cli = {
        'stream': 'stream',
        'limit_codepoints': 'limit_codepoints',
        'limit_graphemes': 'limit_graphemes',
        'limit_graphemes_pct': 'limit_graphemes_pct',
        'limit_words': 'limit_graphemes',
        'limit_errors': 'limit_errors',
        'limit_category_time': 'limit_category_time',
        'timeout': 'timeout_cps',
        'stop_at_error': 'stop_at_error',
    }
    yaml_bool_flags = {
        'no_terminal_test': 'no_terminal_test',
        'no_languages_test': 'no_languages_test',
    }

    for yaml_key, cli_key in yaml_to_cli.items():
        if yaml_key in session_args and session_args[yaml_key] is not None:
            results[cli_key] = session_args[yaml_key]
    for yaml_key, cli_key in yaml_bool_flags.items():
        if session_args.get(yaml_key):
            results[cli_key] = True

    if not results.get('save_yaml'):
        results['save_yaml'] = yaml_path
    if not results.get('set_software_name') and data.get('software_name'):
        results['set_software_name'] = data['software_name']
    if not results.get('set_software_version') and data.get('software_version'):
        results['set_software_version'] = data['software_version']

    return results


def main():
    sys.exit(run(**parse_args()))


if __name__ == "__main__":
    main()
