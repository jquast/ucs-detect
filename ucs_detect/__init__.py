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
from ucs_detect import measure, terminal
from ucs_detect.error_matcher import ErrorMatcher


def merge_results(base_results, additional_results):
    """
    Merge two test result dictionaries.

    Combines test results by adding n_total, n_errors, and recalculating pct_success,
    combines failed_codepoints lists and averages the combined timing metrics.
    """
    merged = {}
    all_versions = set(base_results.keys()) | set(additional_results.keys())

    for ver in all_versions:
        base = base_results.get(ver, {})
        additional = additional_results.get(ver, {})

        n_total = base.get('n_total', 0) + additional.get('n_total', 0)
        n_errors = base.get('n_errors', 0) + additional.get('n_errors', 0)

        # Combine failed codepoints
        failed_codepoints = (
            base.get('failed_codepoints', []) + additional.get('failed_codepoints', [])
        )

        # Calculate combined timing (weighted average)
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
    # set locale support for '{:n}' formatter, https://stackoverflow.com/a/3909907
    locale.setlocale(locale.LC_ALL, "")
    term = blessed.Terminal(stream=sys.__stderr__ if stream == "stderr" else None)
    writer = functools.partial(
        print, end="", flush=True, file=sys.stderr if stream == "stderr" else None
    )
    return term, writer


def run(stream, limit_codepoints, limit_errors, limit_words, limit_codepoints_wide_pct, include_uncommon_codepoints, save_yaml, no_terminal_test, no_languages_test, timeout, stop_at_error, set_software_name, set_software_version, grapheme_delay_ms=0, **_kwargs):
    """Program entry point."""
    term, writer = init_term(stream)

    # Create error matcher for interactive debugging
    error_matcher = ErrorMatcher(stop_at_error)

    # record and display program arguments
    local_vars = locals().copy()
    session_arguments = {
        k: local_vars[k]
        for k in ("stream", "limit_codepoints", "limit_errors", "limit_words")
    }
    writer(f"ucs-detect: {display_args(session_arguments)})")

    if measure.get_location_with_retry(term, timeout) == (-1, -1):
        raise RuntimeError(f"Not a terminal or Timeout exceeded ({timeout:.1f}s)!")

    writer(f"\nucs-detect: Interactive terminal detected!")

    # Quick unicode sanity check — measure a known wide character (U+231A WATCH)
    unicode_width = measure.measure_width(term, writer, '\u231A', timeout)
    if unicode_width != 2:
        writer(f"\nucs-detect: " + term.bold_red(
            "This terminal does not appear to support Unicode wide characters."
        ))
        writer(f"\nucs-detect: measured width of U+231A WATCH: {unicode_width}\n")
        return {}

    # Detect ambiguous width (1=narrow, 2=wide, -1=unknown)
    ambiguous_width = term.detect_ambiguous_width(timeout=timeout, fallback=-1)
    if ambiguous_width == -1:
        ambig_label = "unknown"
    elif ambiguous_width == 2:
        ambig_label = "wide (2)"
    else:
        ambig_label = "narrow (1)"
    writer(f"\nucs-detect: Ambiguous width: {ambig_label}")

    terminal_results = {}
    if not no_terminal_test:
        terminal_results = terminal.do_terminal_detection()

    if save_yaml:
        print()
        # Use --set-software-name if provided, otherwise prompt
        if set_software_name:
            terminal_software = set_software_name
        elif terminal_results.get("software_name"):
            default_software = terminal_results["software_name"]
            terminal_software = input(f'Enter "Terminal Software" (press return for "{default_software}"): ')
            if not terminal_software.strip():
                terminal_software = default_software
        else:
            terminal_software = input('Enter "Terminal Software": ')

        # Use --set-software-version if provided, otherwise prompt
        if set_software_version:
            terminal_version = set_software_version
        elif terminal_results.get("software_version"):
            default_software_version = terminal_results["software_version"]
            terminal_version = input(f'Enter "Software Version" (press return for "{default_software_version}"): ')
            if not terminal_version.strip():
                terminal_version = default_software_version
        else:
            terminal_version = input('Enter "Software Version": ')

    start_time = time.monotonic()

    # run all tests
    test_kwargs = dict(
        term=term, writer=writer, timeout=timeout,
        limit_codepoints=limit_codepoints, limit_errors=limit_errors,
        stop_at_error=error_matcher, grapheme_delay_ms=grapheme_delay_ms,
    )

    with term.cbreak():

        def _status(label):
            header = f"[ Testing {label} ]"
            writer("\n" + term.magenta(header.center(term.width, '-')) + "\n")

        _status("WIDE")
        wide_results = measure.test_support(
            table=WIDE_CHARACTERS, expected_width=2,
            test_type="wide", limit_pct=limit_codepoints_wide_pct,
            include_uncommon=include_uncommon_codepoints,
            **test_kwargs,
        )

        _status("ZWJ")
        emoji_zwj_results = measure.test_support(
            table=EMOJI_ZWJ_SEQUENCES, expected_width=2,
            test_type="zwj", **test_kwargs,
        )

        _status("VS16")
        emoji_vs16_results = merge_results(
            measure.test_support(
                table=VS16_NARROW_TO_WIDE, expected_width=2,
                test_type="vs16", **test_kwargs,
            ),
            measure.test_support(
                table=tuple((ver, tuple(seq[0] for seq in sequences))
                            for ver, sequences in VS16_NARROW_TO_WIDE),
                expected_width=1, suppress_output=True,
                test_type="vs16n", **test_kwargs,
            ),
        )

        _status("VS15")
        emoji_vs15_results = measure.test_support(
            table=VS15_WIDE_TO_NARROW, expected_width=1,
            test_type="vs15", **test_kwargs,
        )

        language_results = None
        if not no_languages_test:
            _status("Languages")
            language_results = measure.do_languages_test(
                term, writer, timeout, limit_words, limit_errors,
                error_matcher, grapheme_delay_ms=grapheme_delay_ms,
            )

    # display final results
    display_results(
        term, writer, ambig_label,
        terminal_results=terminal_results,
        wide_results=wide_results,
        emoji_zwj_results=emoji_zwj_results,
        emoji_vs16_results=emoji_vs16_results,
        emoji_vs15_results=emoji_vs15_results,
        language_results=language_results,
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


def color_pct(term, pct_val):
    """Apply color to a percentage value based on success thresholds."""
    term_style = (
        term.firebrick1 if pct_val < 33
        else term.darkorange1 if pct_val < 50
        else term.yellow if pct_val < 66
        else term.greenyellow if pct_val < 99
        else term.green2
    )
    return term_style(f"{pct_val:0.1f} %")


def _make_theme():
    """Create magenta/cyan ColorTable theme."""
    from prettytable.colortable import Theme
    return Theme(
        default_color="\x1b[36m",
        vertical_color="\x1b[35m",
        horizontal_color="\x1b[35m",
        junction_color="\x1b[35m",
    )



def _build_terminal_kv_pairs(results):
    """Build list of (key, value) tuples from terminal detection results.

    :param dict results: Terminal detection results dictionary.
    :rtype: list[tuple[str, str]]
    """
    pairs = []
    if not results:
        return pairs

    if results.get('ttype'):
        pairs.append(("Terminal Type", results['ttype']))

    if results.get('software_name'):
        software = results['software_name']
        if results.get('software_version'):
            software += f" {results['software_version']}"
        pairs.append(("Software", software))

    if results.get('number_of_colors') is not None:
        pairs.append(("Colors", f"{results['number_of_colors']:n}"))

    if results.get('width') and results.get('height'):
        pairs.append(("Size (cells)", f"{results['width']} x {results['height']}"))

    if results.get('pixels_width') and results.get('pixels_height'):
        pairs.append(("Size (pixels)",
                       f"{results['pixels_width']} x {results['pixels_height']}"))

    if results.get('cell_width') and results.get('cell_height'):
        pairs.append(("Cell Size (pixels)",
                       f"{results['cell_width']} x {results['cell_height']}"))

    if results.get('screen_ratio'):
        ratio_info = results['screen_ratio']
        if results.get('screen_ratio_name'):
            ratio_info += f" ({results['screen_ratio_name']})"
        pairs.append(("Aspect Ratio", ratio_info))

    if results.get('sixel') is not None:
        pairs.append(("Sixel Graphics", 'Yes' if results['sixel'] else 'No'))

    if results.get('foreground_color_rgb'):
        fg = results['foreground_color_rgb']
        # normalize 16-bit RGB to 8-bit
        r8, g8, b8 = (fg[0] >> 8, fg[1] >> 8, fg[2] >> 8)
        pairs.append(("Foreground",
                       f"({r8:>3}, {g8:>3}, {b8:>3}) #{r8:02x}{g8:02x}{b8:02x}"))

    if results.get('background_color_rgb'):
        bg = results['background_color_rgb']
        r8, g8, b8 = (bg[0] >> 8, bg[1] >> 8, bg[2] >> 8)
        pairs.append(("Background",
                       f"({r8:>3}, {g8:>3}, {b8:>3}) #{r8:02x}{g8:02x}{b8:02x}"))

    if results.get('device_attributes'):
        da = results['device_attributes']
        if da.get('service_class') is not None:
            pairs.append(("Device Class", str(da['service_class'])))
        if da.get('extensions'):
            pairs.append(("Device Extensions",
                           f"{len(da['extensions'])} supported"))

    if results.get('modes'):
        pairs.append(("DEC Modes", f"{len(results['modes']):n}"))

    return pairs


def _build_test_kv_pairs(term, ambig_label, **result_sets):
    """Build list of (key, value) tuples from test results and versions.

    :param term: Blessed terminal instance.
    :param str ambig_label: Ambiguous width label string.
    :rtype: list[tuple[str, str]]
    """
    pairs = []
    wide = result_sets.get("wide_results", {})
    zwj = result_sets.get("emoji_zwj_results", {})
    vs16 = result_sets.get("emoji_vs16_results", {})
    vs15 = result_sets.get("emoji_vs15_results", {})

    for name, data in [("WIDE", wide), ("ZWJ", zwj), ("VS16", vs16), ("VS15", vs15)]:
        if data:
            for label, d in data.items():
                pairs.append((name, color_pct(term, d["pct_success"])))

    pairs.append(("Ambiguous Width", ambig_label))
    pairs.append(("Unicode Version", wcwidth.list_versions()[-1]))
    return pairs


def _make_kv_table(title, pairs):
    """Build a ColorTable from a list of (key, value) tuples.

    :param str title: Table title.
    :param list pairs: List of (key, value) tuples.
    :rtype: prettytable.colortable.ColorTable
    """
    from prettytable.colortable import ColorTable
    table = ColorTable(theme=_make_theme())
    table.title = title
    table.field_names = ["Attribute", "Value"]
    table.align["Attribute"] = "r"
    table.align["Value"] = "l"
    table.header = False
    for key, value in pairs:
        table.add_row([key, value])
    return table


def make_language_table(term, results):
    """Build a ColorTable for language test results."""
    from prettytable.colortable import ColorTable
    success_langs = [
        lang for lang in results if results[lang]["pct_success"] == 100.0
    ]
    failed_langs = [
        lang for lang in results if results[lang]["pct_success"] < 100.0
    ]
    table = ColorTable(theme=_make_theme())
    n_langs = len(success_langs) + len(failed_langs)
    table.title = f"Language Support ({len(success_langs)} of {n_langs} passed)"
    table.field_names = ["Language", "Total", "Failures", "Success"]
    table.align["Language"] = "l"
    table.align["Total"] = "r"
    table.align["Failures"] = "r"
    table.align["Success"] = "r"
    for lang in sorted(failed_langs):
        data = results[lang]
        table.add_row([
            lang,
            f"{data['n_total']:n}",
            f"{data['n_errors']:n}",
            color_pct(term, data["pct_success"]),
        ])
    return table


def display_results(term, writer, ambig_label, terminal_results=None,
                    **result_sets):
    """Display all test results as prettytable key-value tables.

    :param term: Blessed terminal instance.
    :param writer: Output writer function.
    :param str ambig_label: Ambiguous width label.
    :param dict terminal_results: Terminal detection results.
    """
    terminal_pairs = _build_terminal_kv_pairs(terminal_results or {})
    test_pairs = _build_test_kv_pairs(term, ambig_label, **result_sets)

    writer("\n")
    if terminal_pairs:
        writer(str(_make_kv_table("Terminal", terminal_pairs)) + "\n\n")
    if test_pairs:
        writer(str(_make_kv_table("Unicode", test_pairs)) + "\n\n")

    langs = result_sets.get("language_results")
    if langs:
        failed = [l for l in langs if langs[l]["pct_success"] < 100.0]
        if failed:
            writer(str(make_language_table(term, langs)) + "\n")


def do_save_yaml(save_yaml, **kwargs):
    yaml.safe_dump(
        kwargs,
        open(save_yaml, "w", encoding='utf-8'),
        sort_keys=True,
        allow_unicode=True,
        default_flow_style=False
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
        help="limit the total number of codepoints of each version (0=unlimited)",
    )
    args.add_argument(
        "--limit-words",
        type=int,
        default=0,
        help="limit the total number of 'words' tested for each language (0=unlimited)",
    )
    args.add_argument(
        "--limit-errors",
        type=int,
        default=0,
        help="limit the total number of errors for each tested version or language (0=unlimited)",
    )
    args.add_argument(
        "--limit-codepoints-wide-pct",
        type=int,
        default=7,
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
        help=(
            "Include uncommon codepoints in WIDE testing that most fonts lack "
            "glyphs for, such as CJK Extensions B-I and Tangut. These cause "
            "slow font fallback lookups and render as replacement characters "
            "in most terminals."
        ),
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
        "--timeout",
        type=float,
        default=10.0,
        help="Timeout in seconds for terminal cursor position testing",
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
        "--grapheme-delay-ms",
        type=int,
        default=0,
        help="Delay in milliseconds after writing each grapheme before measuring cursor position",
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
    results = vars(args.parse_args())
    if results["save_yaml"]:
        results["save_yaml"] = os.path.expanduser(results["save_yaml"])
    return results


def main():
    sys.exit(run(**parse_args()))


if __name__ == "__main__":
    main()
