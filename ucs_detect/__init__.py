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
import re
import sys
import time
import codecs
import locale
import argparse
import functools
import platform
import datetime
import collections
from typing import Optional

# 3rd party
import blessed
import wcwidth
import yaml

# local
from ucs_detect.table_zwj import EMOJI_ZWJ_SEQUENCES
from ucs_detect.table_wide import WIDE_CHARACTERS
from ucs_detect.table_vs16 import VS16_NARROW_TO_WIDE

# to accommodate varying screen sizes, we measure by each word,
# but some languages do not use ASCII space, we make some
# effort to use any their word boundaries.
WORD_SPLIT_DELIMITERS = (" ", "，", "、", ",", "\u200b", "。", "\uA9C0")

if (sys.version_info.major, sys.version_info.minor) > (3, 10):
    DATE_NOW = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M:%S UTC")
else:
    DATE_NOW = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

def unicode_escape_string(input_str):
    encoded_str = codecs.encode(input_str, "unicode-escape").decode("utf-8")
    return encoded_str


def parse_udhr():
    path_udhr = os.path.join(os.path.dirname(__file__), 'udhr')
    for fname in os.listdir(path_udhr):
        with open(os.path.join(path_udhr, fname)) as fin:
            # read only up to first '-----' marker
            language = fin.readline().split('-', 1)[1].strip()
            while True:
                line = fin.readline()
                if line == '---\n':
                    break
            text_parts = []
            while True:
                line = fin.readline()
                if not line:
                    break
                text_parts += line.strip().split() if line.strip() else ""
            yield language, ' '.join(text_parts)


def word_splitter(line):
    """
    A version of re.split that also includes the delimiters in the result
    """
    result = []
    last_end = 0
    sep = rf"[\s{''.join(WORD_SPLIT_DELIMITERS[1:])}]"
    for match in re.finditer(sep, line):
        start, end = match.start(), match.end()
        if start > last_end:
            result.append(line[last_end:start])
        result.append(line[start:end])
        last_end = end
    if last_end < len(line):
        result.append(line[last_end:])
    return result


def test_language_support(
    term,
    writer,
    timeout,
    orig_xpos,
    top,
    bottom,
    unicode_version,
    largest_xpos,
    limit_words,
    limit_errors,
):
    # This is more of a "Test zero-width support" exercise,
    # many languages include zero-width characters, at least:
    # Tamil, Tibetan, Syriac, Gujarati, Grantha, Tamil, Myanmar, Adlam,
    # Mongolian, Gurmukhi, Telugu, Tai, Thaana, Tagalog, Arabic, Kannada,
    # Tibetan, Lao, Sinhala, Javanese, Thai, Chakma, Devanagari, Malayalam,
    # Khmer, Bengali ..
    #
    # begin test, successgroup-by language
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)
    start_time = time.monotonic()
    for lang, multiline_text in parse_udhr():
        writer(term.csr(0, term.height) + term.move_yx(top - 1, orig_xpos))
        writer(f"{lang}" + term.clear_eos)
        writer(term.csr(top, bottom) + term.move_yx(top, 0))
        last_ypos = top
        for line in [
            _line.strip() for _line in multiline_text.splitlines() if _line.strip()
        ]:
            estimated_xpos = 0
            words = word_splitter(line)
            for wchars in words:
                if (
                    success_report[lang] >= limit_words
                    or len(failure_report[lang]) >= limit_errors
                ):
                    break
                expected_width = wcwidth.wcswidth(
                    wchars, unicode_version=(unicode_version or "auto")
                )
                assert expected_width != -1, (wchars, unicode_version)
                if expected_width >= term.width:
                    # filter: do not test long phrases that span margin
                    continue

                # next word goes beyond saftey margin, word-wrap
                if expected_width + estimated_xpos > (term.width - largest_xpos):
                    writer("\n")
                    estimated_xpos = 0
                    last_ypos = min(last_ypos + 1, bottom)

                writer(wchars)
                start_xpos = estimated_xpos
                estimated_xpos += expected_width

                if wchars in WORD_SPLIT_DELIMITERS:
                    # small optimization, do not measure length of word-split delimiters
                    continue

                # fetch cursor position
                end_ypos, end_xpos = term.get_location(timeout=timeout)
                if (-1, -1) == (end_ypos, end_xpos):
                    # exit on timeout
                    display_timeout_error(
                        term, writer, timeout, orig_xpos, top, bottom, lang
                    )
                    sys.exit(1)

                # measure distance
                delta_xpos = end_xpos - start_xpos
                delta_ypos = end_ypos - last_ypos
                if (0, expected_width) == (delta_ypos, delta_xpos):
                    success_report[lang] += 1
                else:
                    # add failure_report record, conditionally add delta_ypos and
                    # delta_xpos when unexepcted values,
                    failure_report[lang].append(
                        ({"wchars": unicode_escape_string(wchars)})
                    )
                    if delta_ypos != 0:
                        failure_report[lang][-1]["delta_ypos"] = delta_ypos
                    failure_report[lang][-1]["measured_by_wcwidth"] = expected_width
                    failure_report[lang][-1]["measured_by_terminal"] = delta_xpos
                # reset estimates to actual
                estimated_xpos = end_xpos
                last_ypos = end_ypos

    # reset scrolling region to default
    # and move cursor to bottom right
    writer(term.set_scrolling_region(0, term.height))
    writer(term.move_yx(term.height, term.width - 1) + "\n")

    report_languages = [
        language
        for language in set(list(failure_report.keys()) + list(success_report.keys()))
        if len(failure_report[language]) or success_report[language]
    ]
    test_total_sum = sum(success_report.values()) + sum(
        [len(v) for v in failure_report.values()]
    )
    writer(
        f"ucs-detect Languages testing completed {test_total_sum:n} wchars in total, "
    )
    writer(f"{time.monotonic() - start_time:.2f}s elapsed.")

    return {
        lang: {
            "n_errors": len(failure_report[lang]),
            "n_total": len(failure_report[lang]) + success_report[lang],
            "pct_success": make_success_pct(
                n_errors=len(failure_report[lang]),
                n_total=len(failure_report[lang]) + success_report[lang],
            ),
            "failed": failure_report[lang],
        }
        for lang in report_languages
    }


def determine_simple_rtt_ms(term, timeout) -> float:
    """
    Return interactive terminal round-trip time of blessed term.get_location() function.

    Returns real-time trip (RTT) in milleseconds
    """
    # start monotonic timer
    start_time_ns = time.monotonic_ns()
    term.get_location(timeout=timeout)
    return (time.monotonic_ns() - start_time_ns) * 1e-6


def display_timeout_error(term, writer, timeout, orig_xpos, top, bottom, lang):
    writer(term.csr(0, term.height) + term.move_yx(top - 1, orig_xpos) + term.clear_eos)
    writer(term.reverse_red(f"Timeout Exceeded ({timeout:.2f}s)"))
#    term.inkey(timeout=10)
#    writer(term.move_yx(top - 1, orig_xpos) + term.clear_eos)
#    writer(f" ({lang})" + term.clear_eos)
#    writer(term.csr(top, bottom) + term.move_yx(top, 0) + term.clear_eos())


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


def test_support(
    table,
    term,
    writer,
    timeout,
    quick,
    limit_codepoints,
    limit_errors,
    expected_width,
    largest_xpos,
    report_lbound,
    shell,
):
    # begin test by version, newest to old
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)

    start_time = time.monotonic()
    outer_ypos, outer_xpos = term.get_location(timeout=timeout)
    for ver, wchars in table:
        maybe_str = f", version={ver}: " if not shell else ""
        writer(term.move_yx(outer_ypos, outer_xpos) + maybe_str + term.clear_eol)
        orig_start_ypos, orig_start_xpos = term.get_location(timeout=timeout)
        start_ypos, start_xpos = orig_start_ypos, orig_start_xpos
        # prime this variable for breaking out of loop when the distant
        # end stops responding and exceeds timeout in get-location() by
        # return value of -1, -1
        end_ypos, end_xpos = 0, 0
        for wchar in wchars[: limit_codepoints if limit_codepoints else None]:
            # write test character or sequence
            wchars_str = (
                chr(wchar)
                if isinstance(wchar, int)
                else "".join(chr(_wc) for _wc in wchar)
            )
            writer(wchars_str)

            # measure cursor distance,
            end_ypos, end_xpos = term.get_location(timeout=timeout)
            if (-1, -1) == (end_ypos, end_xpos):
                writer(term.move_yx(outer_ypos, outer_xpos))
                writer(term.reverse_red(f"Timeout Exceeded ({timeout:.2f}s)"))
                if quick or shell:
                    break
                term.inkey(timeout=1)
            delta_xpos = end_xpos - start_xpos
            delta_ypos = end_ypos - start_ypos
            if (delta_ypos, delta_xpos) == (0, expected_width):
                success_report[ver] += 1
            else:
                # add failure_report record, conditionally add delta_ypos and
                # delta_xpos only when unexepcted values,
                failure_report[ver].append(
                    ({"wchar": unicode_escape_string(wchars_str)})
                )
                if delta_ypos != 0:
                    failure_report[ver][-1]["delta_ypos"] = delta_ypos
                if delta_xpos != expected_width:
                    failure_report[ver][-1]["measured_by_wcwidth"] = expected_width
                    failure_report[ver][-1]["measured_by_terminal"] = delta_xpos
                # and break version test early on --limit-errors.
                if limit_errors and len(failure_report[ver]) >= limit_errors:
                    break

            start_ypos, start_xpos = end_ypos, end_xpos + delta_xpos
            maybe_clear_eol = ""
            if end_xpos > (term.width - largest_xpos) or delta_ypos != 0:
                # out-of-bounds, reset (y, x) to home position
                start_ypos, start_xpos = orig_start_ypos, orig_start_xpos
                maybe_clear_eol = term.clear_eol
            writer(term.move_yx(start_ypos, start_xpos) + maybe_clear_eol)

        if quick:
            # sub-versions like 12.1.0 are tricky, because there is only one single
            # new codepoint, otherwise stop immediately on first 100% success,
            # except for tables of very small codepoints!
            if (
                wchars
                and not failure_report[ver]
                and success_report[ver] >= report_lbound
            ):
                break
            if (-1, -1) == (end_ypos, end_xpos):
                # stop immediately on any timeout
                break

    writer(term.move_yx(outer_ypos, outer_xpos))
    if shell:
        writer(term.normal + term.clear_eol)

    # create sorted list of versions that have any results, to determine
    # primary key of returned result
    report_versions = [
        v
        for _, v in sorted(
            [
                (wcwidth._wcversion_value(_ver), _ver)
                for _ver in set(
                    list(failure_report.keys()) + list(success_report.keys())
                )
                if len(failure_report[_ver]) or success_report[_ver]
            ]
        )
    ]
    test_total_sum = sum(success_report.values()) + sum(
        [len(v) for v in failure_report.values()]
    )
    if not shell:
        writer(
            f": {test_total_sum:n} wchars total, {time.monotonic() - start_time:.2f}s elapsed."
        )
        writer(term.clear_eol)

    return {
        ver: {
            "n_errors": len(failure_report[ver]),
            "n_total": len(failure_report[ver]) + success_report[ver],
            "pct_success": make_success_pct(
                n_errors=len(failure_report[ver]),
                n_total=len(failure_report[ver]) + success_report[ver],
            ),
            "failed_codepoints": failure_report[ver],
        }
        for ver in report_versions
    }


def make_success_pct(n_errors, n_total):
    # protect from divide-by-zero and convert decimal to whole percentage points
    return ((n_total - n_errors) / n_total if n_total else 0) * 100


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


def run(stream, quick, limit_codepoints, limit_errors, limit_words, save_yaml, shell, unicode_version):
    """Program entry point."""
    term, writer = init_term(stream, quick)

    # record and display program arguments
    local_vars = locals().copy()
    session_arguments = {
        k: local_vars[k]
        for k in ("stream", "quick", "limit_codepoints", "limit_errors", "limit_words")
    }
    if not shell:
        writer(f"ucs-detect: {display_args(session_arguments)})")

    if save_yaml:
        terminal_software = input('\nEnter "Terminal Software": ')
        terminal_version = input('Enter "Software Version": ')

    stime = time.monotonic()
    try:
        # measure real-time trip (RTT) of distant end three times and
        # use the largest value
        rtt_ms = max(
            [
                determine_simple_rtt_ms(term, timeout=3.2),
                determine_simple_rtt_ms(term, timeout=3.2),
                determine_simple_rtt_ms(term, timeout=3.2),
            ]
        )
    except RuntimeError:
        print("ucs-detect: Unicode Version could not be determined!", file=sys.stderr)
        sys.exit(1)
    else:
        # once calibrated, use a very long timeout, some terminals have slowdown
        # difficulties with combining characters during language testing
        timeout = 10
        if not shell:
            writer(f"\nucs-detect: Interactive terminal detected ! (rtt={rtt_ms:.2f}ms, timeout={int(timeout):n}s)")

    # test full-wide unicode table
    if not shell:
        writer(
            f"\nucs-detect: "
            + term.reverse("Testing in progress. DO NOT TYPE. DO NOT RESIZE WINDOW.")
        )
        writer(f"\nucs-detect: WIDE testing")
    wide_results = test_support(
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
    )
    if unicode_version:
        # match by CLI argument, '--unicode-version'
        unicode_version = _wcmatch_version(unicode_version)
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
    emoji_zwj_results = test_support(
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
    )
    emoji_zwj_version = determine_best_match(
        emoji_zwj_results, lbound_pct=90, report_lbound=2
    )

    # Test "recommended" Variation-16 emoji sequences
    writer(f"\nucs-detect: VS16 testing")
    emoji_vs16_results = test_support(
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
    )

    # test language support
    language_results = None
    if not quick:
        language_results = do_languages_test(
            term, writer, timeout, unicode_version, limit_words, limit_errors
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

    if language_results:
        writer(
            f'\nDisplaying results of WIDE and ZERO-WIDTH sequence support by {term.bold("language")}'
        )
        display_results_by_language(term=term, writer=writer, results=language_results)

    if save_yaml:
        do_save_yaml(
            save_yaml,
            session_arguments=session_arguments,
            software=terminal_software,
            version=terminal_version,
            seconds_elapsed=time.monotonic() - stime,
            width=term.width,
            height=term.height,
            python_version=platform.python_version(),
            system=platform.system(),
            datetime=DATE_NOW,
            wcwidth_version=wcwidth.__version__,
            test_results=dict(
                unicode_wide_version=unicode_version,
                unicode_wide_results=wide_results,
                emoji_zwj_version=emoji_zwj_version,
                emoji_zwj_results=emoji_zwj_results,
                emoji_vs16_results=emoji_vs16_results,
                language_results=language_results,
            ),
        )
    writer('\n')


def do_languages_test(
    term, writer, timeout, unicode_version, limit_words, limit_errors
):
    writer(f"\nucs-detect: testing language support: ")
    orig_ypos, orig_xpos = term.get_location(timeout=timeout)
    writer("\n" * 20)
    if orig_ypos != term.height - 1:
        next_ypos, _ = term.get_location(timeout=timeout)
        top = max(0, next_ypos - 19)
    else:
        top = max(0, term.height - 20)
    bottom = min(top + 20, term.height - 1)
    start_time = time.monotonic()
    try:
        writer(term.csr(top, bottom) + term.move_yx(top, 0) + term.clear_eos)
        language_results = test_language_support(
            term=term,
            writer=writer,
            timeout=timeout,
            orig_xpos=orig_xpos,
            top=top,
            bottom=bottom,
            unicode_version=unicode_version,
            largest_xpos=15,
            limit_words=limit_words,
            limit_errors=limit_errors,
        )
    finally:
        # reset scrolling region
        writer(term.csr(0, term.height))
    writer(term.move_yx(top, 0) + term.clear_eos)
    writer(term.move_yx(top - 1, orig_xpos))
    writer(f"{len(language_results):n} total, ")
    writer(f"{time.monotonic() - start_time:.2f}s elapsed.")
    return language_results


def do_save_yaml( save_yaml, **kwargs):
    yaml.safe_dump(kwargs, open(save_yaml, "w"), sort_keys=True)


def parse_args():
    args = argparse.ArgumentParser()
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
        help="Save test results to given filepath as yaml, will prompt for software name & version",
        default=None,
    )
    args.add_argument(
        "--unicode-version",
        help=("Override unicode version for language testing, otherwise best match by wide character "
              "testing is used")
    )
    results = vars(args.parse_args())
    if results["quick"]:
        results["limit_codepoints"] = results["limit_codepoints"] or 50
        results["limit_errors"] = results["limit_errors"] or 5
    if results["shell"]:
        assert not results["save_yaml"], "Cannot use --shell with --save-yaml"
        assert results["stream"] == "stderr", "Cannot use --shell with --stream=stdout"
        assert not results["unicode_version"], "Do not use with --shell"
    if results["save_yaml"]:
        results["save_yaml"] = os.path.expanduser(results["save_yaml"])
    return results


def main():
    sys.exit(run(**parse_args()))


if __name__ == "__main__":
    main()
