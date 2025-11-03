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
from typing import Optional

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


def determine_best_match(
    wide_results: dict, lbound_pct: float, report_lbound: int
) -> Optional[float]:
    # Iterate through results of test_wide_support(), determine their success pct
    # as n_errors / n_total, create descending sorted list of [success_pct, unicode_version],
    # and chose the 'best' version above lbound_pct, after sorted order of
    # (pct_success, value_version).
    #
    # This is for the case of mixed 95-100% support rates, at time of this writing,
    # iTerm2 supports 100% of wmoji zwj 12.1, 97% in 13.1, *0%* 14.0, and 99% of 15.1,
    # it just has a gap of support for the ZWJ sequence released in version 14, strange,
    # but in this case it is best to suggest a total version of 15.1.
    #
    # do not consider test results from unicode tables with very few changes,
    # such as wide table 12.1.0 release has just 1 change, and
    # emoji table 1.0 has just 1 change, by argument 'report_lbound'
    results = []
    for ver, result in wide_results.items():
        if not report_lbound or result["n_total"] >= report_lbound:
            try:
                results.append(
                    (result["pct_success"], wcwidth._wcversion_value(ver), ver)
                )
            except ZeroDivisionError:
                results.append((0, wcwidth._wcversion_value(ver), ver))
    if not results:
        return None
    results.sort(reverse=True)

    best_match = results[0]
    for pct_success, value_version, str_version in results:
        if pct_success >= lbound_pct and value_version > best_match[1]:
            best_match = (pct_success, value_version, str_version)
    return best_match[2] if best_match[0] > lbound_pct else None




def init_term(stream, quick):
    # set locale support for '{:n}' formatter, https://stackoverflow.com/a/3909907
    locale.setlocale(locale.LC_ALL, "")
    term = blessed.Terminal(stream=sys.__stderr__ if stream == "stderr" else None)
    if not quick:
        # require a normally sized terminal for language testing, some languages
        # have very long words and its not worth fighting about it.
        assert term.width > 79, (
            "Terminal must be at least 80 columns wide",
            term.width,
        )
        assert term.height > 23, (
            "Terminal height must be at least 23 lines",
            term.width,
        )
    writer = functools.partial(
        print, end="", flush=True, file=sys.stderr if stream == "stderr" else None
    )
    return term, writer


def run(stream, quick, limit_codepoints, limit_errors, limit_words, save_yaml, shell, unicode_version, no_terminal_test, no_languages_test, timeout, no_emit_osc1337, stop_at_error):
    """Program entry point."""
    term, writer = init_term(stream, quick)

    # Create error matcher for interactive debugging
    error_matcher = ErrorMatcher(stop_at_error)

    # record and display program arguments
    local_vars = locals().copy()
    session_arguments = {
        k: local_vars[k]
        for k in ("stream", "quick", "limit_codepoints", "limit_errors", "limit_words")
    }
    if not shell:
        writer(f"ucs-detect: {display_args(session_arguments)})")

    if measure.get_location_with_retry(term, timeout) == (-1, -1):
        raise RuntimeError(f"Not a terminal or Timeout exceeded ({timeout:.1f}s)!")

    # Use a very long timeout, some terminals have slowdown difficulties with
    # combining characters during language testing
    if not shell:
        writer(f"\nucs-detect: Interactive terminal detected !")

    terminal_results = {}
    if not no_terminal_test:
        terminal_results = terminal.do_terminal_detection()
        if not shell:
            display_terminal_results(term, writer, terminal_results)

    if save_yaml:
        print()
        if terminal_results.get("software_name"):
            default_software = terminal_results["software_name"]
            terminal_software = input(f'Enter "Terminal Software" (press return for "{default_software}"): ')
            if not terminal_software.strip():
                terminal_software = default_software
        else:
            # TODO: fallback environment variable for automation
            terminal_software = input('Enter "Terminal Software": ')
        if terminal_results.get("software_version"):
            default_software_version = terminal_results["software_version"]
            terminal_version = input(f'Enter "Software Version" (press return for "{default_software_version}"): ')
            if not terminal_version.strip():
                terminal_version = default_software_version
        else:
            terminal_version = input('Enter "Software Version": ')

    start_time = time.monotonic()

    # test full-wide unicode table
    if not shell:
        msg_do_not = "Testing in progress. DO NOT TYPE. DO NOT RESIZE WINDOW."
        writer(f"\nucs-detect: " + term.reverse(msg_do_not))
        writer(f"\nucs-detect: WIDE testing")
    wide_results = measure.test_support(
        table=WIDE_CHARACTERS,
        term=term,
        writer=writer,
        timeout=timeout,
        quick=quick,
        limit_codepoints=limit_codepoints,
        limit_errors=limit_errors,
        expected_width=2,
        largest_xpos=4,
        report_lbound=2,
        shell=shell,
        emit_osc1337=not no_emit_osc1337,
        stop_at_error=error_matcher,
        test_type="wide",
    )
    if unicode_version:
        # match by CLI argument, '--unicode-version'
        unicode_version = wcwidth._wcmatch_version(unicode_version)
    else:
        # match version by results of wide character test
        unicode_version = determine_best_match(wide_results, lbound_pct=90, report_lbound=2)
    if shell:
        # when using --shell, this program's only purpose is to make a best
        # estimate of exporting UNICODE_VERSION for use with wcwidth library and
        # exit quickly.
        if not unicode_version:
            print(
                "ucs-detect: Unicode Version could not be determined!", file=sys.stderr
            )
            sys.exit(1)
        print(f"UNICODE_VERSION={unicode_version}; export UNICODE_VERSION")
        sys.exit(0)

    # Test zero-width joiner with "recommended" emoji sequences
    writer(f"\nucs-detect: ZWJ testing")
    emoji_zwj_results = measure.test_support(
        table=EMOJI_ZWJ_SEQUENCES,
        term=term,
        writer=writer,
        timeout=timeout,
        quick=quick,
        limit_codepoints=limit_codepoints,
        limit_errors=limit_errors,
        expected_width=2,
        largest_xpos=20,
        report_lbound=2,
        shell=shell,
        emit_osc1337=not no_emit_osc1337,
        stop_at_error=error_matcher,
        test_type="zwj",
    )
    emoji_zwj_version = determine_best_match(
        emoji_zwj_results, lbound_pct=90, report_lbound=2
    )

    # Test "recommended" Variation-16 emoji sequences
    writer(f"\nucs-detect: VS16 testing")
    emoji_vs16_results = measure.test_support(
        table=VS16_NARROW_TO_WIDE,
        term=term,
        writer=writer,
        timeout=timeout,
        quick=quick,
        limit_codepoints=limit_codepoints,
        limit_errors=limit_errors,
        expected_width=2,
        largest_xpos=5,
        report_lbound=2,
        shell=shell,
        emit_osc1337=not no_emit_osc1337,
        stop_at_error=error_matcher,
        test_type="vs16",
    )

    # Variation-15 emoji sequences
    writer(f"\nucs-detect: VS15 testing")
    emoji_vs15_results = measure.test_support(
        table=VS15_WIDE_TO_NARROW,
        term=term,
        writer=writer,
        timeout=timeout,
        quick=quick,
        limit_codepoints=limit_codepoints,
        limit_errors=limit_errors,
        expected_width=1,
        largest_xpos=5,
        report_lbound=2,
        shell=shell,
        emit_osc1337=not no_emit_osc1337,
        stop_at_error=error_matcher,
        test_type="vs15",
    )

    # test language support
    language_results = None
    if not quick and not no_languages_test:
        language_results = measure.do_languages_test(
            term, writer, timeout, unicode_version, limit_words, limit_errors, error_matcher
        )

    # display results
    writer(
        f'\nDisplaying results of {term.bold("WIDE")} character support as success rate'
    )
    display_results_by_version(
        term=term, writer=writer, results=wide_results, best_match=unicode_version
    )

    writer(
        f'\nDisplaying results {term.bold("ZWJ")} sequence support as success rate'
    )
    display_results_by_version(
        term=term,
        writer=writer,
        results=emoji_zwj_results,
        best_match=emoji_zwj_version,
    )

    writer(
        f'\nDisplaying results of {term.bold("Variation Selector-16")} sequence support and their success rate'
    )
    display_results_by_version(
        term=term,
        writer=writer,
        results=emoji_vs16_results,
        best_match=list(emoji_vs16_results.keys())[0],
    )

    writer(
        f'\nDisplaying results of {term.bold("Variation Selector-15")} sequence support'
    )
    display_results_by_version(
        term=term,
        writer=writer,
        results=emoji_vs15_results,
        best_match=list(emoji_vs15_results.keys())[0],
    )

    if language_results:
        writer(
            f'\nDisplaying results of WIDE and ZERO-WIDTH sequence support by {term.bold("language")}'
        )
        display_results_by_language(term=term, writer=writer, results=language_results)

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
            python_version=platform.python_version(),
            system=platform.system(),
            datetime=date_now,
            wcwidth_version=wcwidth.__version__,
            test_results=dict(
                unicode_wide_version=unicode_version,
                unicode_wide_results=wide_results,
                emoji_zwj_version=emoji_zwj_version,
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


def display_results_by_version(term, writer, results, best_match):
    writer(f'\n{"Unicode Version":>16s}: {"Total":>6s}, Success Pct')
    for ver in results.keys():
        _ver = "*" + ver if ver == best_match else ver
        label_s = f"{_ver:>16s}"
        total_s = f"{results[ver]['n_total']:>6n}"
        pct_val = results[ver]["pct_success"]
        term_style = (
            term.firebrick1
            if pct_val < 33
            else term.darkorange1
            if pct_val < 50
            else term.yellow
            if pct_val < 66
            else term.greenyellow
            if pct_val < 99
            else term.green2
        )
        pct_s_colored = term_style(term.rjust(f"{pct_val:0.1f}", 6))
        writer(f"\n{label_s}: {total_s}, {pct_s_colored} %")
    maybe_match = ''
    if len(results) > 1:
        maybe_match = "* Best Match" if best_match else "* No Match !"
    writer(f"\n{maybe_match:>16s}")


def display_results_by_language(term, writer, results):
    success_langs = [
        _lang for _lang in results.keys() if results[_lang]["pct_success"] == 100.0
    ]
    failed_langs = [
        _lang for _lang in results.keys() if results[_lang]["pct_success"] < 100.0
    ]
    writer(
        f"\nLanguage Support: {len(success_langs):n} of {len(failed_langs) + len(success_langs):n}"
    )
    writer(f'\n{"Failed Language":>32s}: {"Total":>6s}, Success Pct')
    for lang in sorted(failed_langs):
        label_s = f"{lang:>32s}"
        total_s = f"{results[lang]['n_total']:>6n}"
        pct_val = results[lang]["pct_success"]
        term_style = (
            term.firebrick1
            if pct_val < 33
            else term.darkorange1
            if pct_val < 50
            else term.yellow
            if pct_val < 66
            else term.greenyellow
            if pct_val < 99
            else term.green2
        )
        pct_s_colored = term_style(term.rjust(f"{pct_val:0.1f}", 6))
        writer(f"\n{label_s}: {total_s}, {pct_s_colored} %")


def display_terminal_results(term, writer, results):
    """Display terminal detection results in a formatted manner."""
    if not results:
        return

    writer(f'\n{term.bold("Terminal Detection Results")}')

    # Basic terminal info
    if results.get('ttype'):
        writer(f"\n{'Terminal Type':>24s}: {results['ttype']}")

    if results.get('software_name'):
        software = results['software_name']
        if results.get('software_version'):
            software += f" {results['software_version']}"
        writer(f"\n{'Software':>24s}: {software}")

    if results.get('number_of_colors') is not None:
        writer(f"\n{'Colors':>24s}: {results['number_of_colors']:n}")

    # Dimensions
    if results.get('width') and results.get('height'):
        writer(f"\n{'Size (cells)':>24s}: {results['width']} x {results['height']}")

    if results.get('pixels_width') and results.get('pixels_height'):
        writer(f"\n{'Size (pixels)':>24s}: {results['pixels_width']} x {results['pixels_height']}")

    if results.get('cell_width') and results.get('cell_height'):
        writer(f"\n{'Cell Size (pixels)':>24s}: {results['cell_width']} x {results['cell_height']}")

    # Screen ratio
    if results.get('screen_ratio'):
        ratio_info = results['screen_ratio']
        if results.get('screen_ratio_name'):
            ratio_info += f" ({results['screen_ratio_name']})"
        writer(f"\n{'Aspect Ratio':>24s}: {ratio_info}")

    # Graphics support
    if results.get('sixel') is not None:
        sixel_status = 'Yes' if results['sixel'] else 'No'
        writer(f"\n{'Sixel Graphics':>24s}: {sixel_status}")

    # Color information
    if results.get('foreground_color_rgb'):
        fg = results['foreground_color_rgb']
        fg_hex = results.get('foreground_color_hex', '')
        writer(f"\n{'Foreground Color':>24s}: RGB({fg[0]}, {fg[1]}, {fg[2]})")
        if fg_hex:
            writer(f"\n{'':>24s}  {fg_hex}")

    if results.get('background_color_rgb'):
        bg = results['background_color_rgb']
        bg_hex = results.get('background_color_hex', '')
        writer(f"\n{'Background Color':>24s}: RGB({bg[0]}, {bg[1]}, {bg[2]})")
        if bg_hex:
            writer(f"\n{'':>24s}  {bg_hex}")

    # Device attributes
    if results.get('device_attributes'):
        da = results['device_attributes']
        if da.get('service_class') is not None:
            writer(f"\n{'Device Class':>24s}: {da['service_class']}")
        if da.get('extensions'):
            ext_count = len(da['extensions'])
            writer(f"\n{'Device Extensions':>24s}: {ext_count} supported")

    # DEC modes summary
    if results.get('modes'):
        modes_count = len(results['modes'])
        writer(f"\n{'DEC Modes Detected':>24s}: {modes_count:n}")


def do_save_yaml( save_yaml, **kwargs):
    yaml.safe_dump(kwargs, open(save_yaml, "w"), sort_keys=True)


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
        default=200,
        help="limit the total number of codepoints of each version",
    )
    args.add_argument(
        "--limit-words",
        type=int,
        default=200,
        help="limit the total number of 'words' tested for each language",
    )
    args.add_argument(
        "--limit-errors",
        type=int,
        default=50,
        help="limit the total number of errors for each tested version or language",
    )
    args.add_argument(
        "--quick",
        action="store_true",
        default=False,
        help=(
            "Stop test early at the first version that matches 100%%. "
            "also sets --limit-codepoints=50, --limit-errors=5 if not "
            "other specified."
        ),
    )
    args.add_argument(
        "--shell",
        action="store_true",
        default=False,
        help=(
            "Determine and display only UNICODE_VERSION shell variable for export to stdout."
            " stream is also set to stderr. Fe, `eval $(ucs-detect --shell)`"
        ),
    )
    args.add_argument(
        "--save-yaml",
        default=None,
        help="Save test results to given filepath as yaml, will prompt for software name & version",
    )
    args.add_argument(
        "--unicode-version",
        help=("Override unicode version for language testing, otherwise best match by wide character "
              "testing is used")
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
        "--no-emit-osc1337",
        action="store_true",
        default=False,
        help="Do not emit OSC 1337 escape sequence to set Unicode version"
    )
    args.add_argument(
        "--stop-at-error",
        default=None,
        help=(
            "Interactively stop and display details when matching errors occur. "
            "Values: 'zwj', 'wide', 'vs16', 'vs15', 'lang' (all languages), "
            "or specific language name (e.g., 'english', 'korean', 'chinese')"
        )
    )
    results = vars(args.parse_args())
    if results["quick"]:
        results["limit_codepoints"] = results["limit_codepoints"] or 50
        results["limit_errors"] = results["limit_errors"] or 5
    if results["shell"]:
        assert not results["save_yaml"], "Cannot use --shell with --save-yaml"
        assert results["stream"] == "stderr", "Cannot use --shell with --stream=stdout"
        assert not results["unicode_version"], "Do not use with --shell"
        results["no_terminal_test"] = True
    if results["save_yaml"]:
        results["save_yaml"] = os.path.expanduser(results["save_yaml"])
    return results


def main():
    sys.exit(run(**parse_args()))


if __name__ == "__main__":
    main()
