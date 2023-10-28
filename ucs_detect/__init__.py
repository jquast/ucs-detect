#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ucs-detect: Reports Unicode version level support of an interactive terminal emulator.

See also,
- https://github.com/jquast/ucs-detect
- https://github.com/jquast/wcwidth
- https://github.com/jquast/blessed

This code comes from experimentation while developing the python 'wcwidth'
library, and its primary purpose is to verify correctness in that library and
evaluating support level of a terminal emulator.

This is achieved by testing the terminal's ability to render a variety of
Unicode characters, and measuring the distance of the cursor after each
character is written to the terminal, using the `Cursor Position Report
<https://vt100.net/docs/vt510-rm/CPR.html>`_ terminal escape sequence.
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

def get_yxpos(term, timeout):
    ypos, xpos = term.get_location(timeout=timeout)
    return (ypos, xpos)

def unicode_escape_string(input_str):
    encoded_str = codecs.encode(input_str, 'unicode-escape').decode('utf-8')
    return encoded_str

def parse_udhr():
    with open(os.path.join(os.path.dirname(__file__), 'udhr_full_subset.txt'), 'r') as fin:
        # read only up to first '-----' marker
        language = None
        while True:
            line = fin.readline()
            if not line:
                break
            if line.startswith('-----'):
                language = fin.readline().strip()
                assert language == 'Arabic, Standard', language
                line = fin.readline()
                break
        text_parts = []
        while True:
            line = fin.readline()
            if not line:
                break
            if line.startswith('----'):
                yield (language, ' '.join(text_parts))
                line_parts = line.split(None, 1)
                if len(line_parts) < 2:
                    # EOF
                    break 
                language = line_parts[1].strip()
                text_parts = []
            else:
                text_parts += line.strip().split() if line.strip() else ''

def partitioner(line, sep=r'[\s，、,\u200b]'):
    """
    A version of re.split that also includes the delimiters in the result
    """
    result = []
    last_end = 0
    for match in re.finditer(sep, line):
        start, end = match.start(), match.end()
        if start > last_end:
            result.append(line[last_end:start])
        result.append(line[start:end])
        last_end = end
    if last_end < len(line):
        result.append(line[last_end:])
    return result


def test_language_support(term, writer, timeout, orig_xpos, top, bottom, unicode_version, largest_xpos):
    # This is more of a "Test zero-width support" exercise,
    # many languages include zero-width characters, at least:
    # Tamil, Tibetan, Syriac, Gujarati, Grantha, Tamil, Myanmar, Adlam,
    # Mongolian, Gurmukhi, Telugu, Tai, Thaana, Tagalog, Arabic, Kannada,
    # Tibetan, Lao, Sinhala, Javanese, Thai, Chakma, Devanagari, Malayalam,
    # Khmer, Bengali ..
    #
    # begin test, group-by language
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)
    start_time = time.monotonic()
    for lang, multiline_text in parse_udhr():
        writer(term.csr(0, term.height) + term.move_yx(top - 1, orig_xpos))
        writer(f'{lang}' + term.clear_eos)
        writer(term.csr(top, bottom) + term.move_yx(top, 0))
        last_ypos = top
        for line in [_line.strip() for _line in multiline_text.splitlines() if _line.strip()]:
            estimated_xpos = 0
            words = partitioner(line)
            for wchars in words:
                wchars_len = wcwidth.wcswidth(wchars, unicode_version=unicode_version)
                assert wchars_len != -1, (wchars, unicode_version)

                # next word is near our saftey margin, word-wrap
                if wchars_len + estimated_xpos > (term.width - largest_xpos):
                    writer('\n')
                    estimated_xpos = 0
                    last_ypos = min(last_ypos + 1, bottom)

                writer(wchars)
                estimated_xpos += wchars_len

                if wchars in (' ', '，', '、' ',', '\u200b'):
                    # small optimization, do not measure length of word-split delimiters
                    continue
                # fetch cursor position
                end_ypos, end_xpos = get_yxpos(term, timeout=timeout)
                if (-1, -1) == (end_ypos, end_xpos):
                    # timeout
                    show_timeout_error(term, writer, timeout, orig_xpos, top, bottom, lang)
                    continue

                # measure distance
                delta_xpos = end_xpos - estimated_xpos
                delta_ypos = end_ypos - last_ypos
                if delta_ypos != 0 or delta_xpos != 0:
                    # add failure_report record, conditionally add delta_ypos and
                    # delta_xpos when unexepcted values,
                    failure_report[lang].append(({"wchars": unicode_escape_string(wchars)}))
                    if delta_ypos != 0:
                        failure_report[lang][-1]["delta_ypos"] = delta_ypos
                    if delta_xpos != 0:
                        failure_report[lang][-1]["measured_by_wcwidth"] = wchars_len
                        failure_report[lang][-1]["measured_by_terminal"] = wchars_len + delta_xpos
                else:
                    success_report[lang] += 1
                # reset estimates to actual
                estimated_xpos = end_xpos
                last_ypos = end_ypos

    # reset scrolling region to default
    # and move cursor to bottom right
    writer(term.set_scrolling_region(0, term.height))
    writer(term.move_yx(term.height, term.width - 1) + '\n')

    report_languages = [
        language
        for language in set(list(failure_report.keys()) + list(success_report.keys()))
        if len(failure_report[language]) or success_report[language]]
    test_total_sum = sum(success_report.values()) + sum([len(v) for v in failure_report.values()])
    writer(f"ucs-detect Languages testing completed {test_total_sum:n} wchars in total, ")
    writer(f"{time.monotonic() - start_time:.2f}s elapsed.")

    return {
            lang: {
                "n_errors": len(failure_report[lang]),
                "n_total": len(failure_report[lang]) + success_report[lang],
                "pct_success": make_success_pct(n_errors=len(failure_report[lang]),
                                                n_total=len(failure_report[lang]) + success_report[lang]),
                "failed": failure_report[lang],
            }
            for lang in report_languages
    }

def show_timeout_error(term, writer, timeout, orig_xpos, top, bottom, lang):
    writer(term.csr(0, term.height) + term.move_yx(top - 1, orig_xpos) + term.clear_eos)
    writer(term.reverse_red(f'Timeout Exceeded ({timeout:.2f}s)'))
    term.inkey(timeout=1)
    writer(term.move_yx(top - 1, orig_xpos) + term.clear_eos)
    writer(f' ({lang})' + term.clear_eos)
    writer(term.csr(top, bottom) + term.move_yx(top, 0) + term.clear_eos())
   

def determine_simple_rtt_ms(term, timeout) -> float:
    """
    Return interactive terminal round-trip time of blessed term.get_location() function.

    Returns real-time trip (RTT) in milleseconds
    """
    # start monotonic timer
    start_time_ns = time.monotonic_ns()
    get_yxpos(term, timeout)
    return (time.monotonic_ns() - start_time_ns) * 1e-6


def display_results_by_version(term, writer, results, best_match):
    writer(f'\n{"Unicode Version":>16s}: {"Total":>6s}, Pct %')
    for ver in results.keys():
        _ver = "*" + ver if ver == best_match else ver
        label_s = f"{_ver:>16s}"
        total_s = f"{results[ver]['n_total']:>6n}"
        pct_val = results[ver]['pct_success']
        term_style = (
            term.firebrick1 if pct_val < 33 else
            term.darkorange1 if pct_val < 50 else
            term.yellow if pct_val < 66 else
            term.greenyellow if pct_val < 99 else
            term.green2)
        pct_s_colored = term_style(term.rjust(f"{pct_val:0.1f}", 6))
        writer(f'\n{label_s}: {total_s}, {pct_s_colored} %')
    maybe_match = "* Best Match" if best_match else "* No Match !"
    writer(f'\n{maybe_match:>16s}')

def display_results_by_language(term, writer, results):
    success_langs = [_lang for _lang in results.keys()
                     if results[_lang]['pct_success'] == 100.0]
    failed_langs = [_lang for _lang in results.keys()
                    if results[_lang]['pct_success'] < 100.0]
    writer(f'\nLanguage Support: {len(success_langs):d} of {len(failed_langs) + len(success_langs):d}')
    writer(f'\n{"Failed Language":>32s}: {"Total":>6s}, Pct %')
    for lang in failed_langs:
        label_s = f"{lang:>32s}"
        total_s = f"{results[lang]['n_total']:>6n}"
        pct_val = results[lang]['pct_success']
        term_style = (
            term.firebrick1 if pct_val < 33 else
            term.darkorange1 if pct_val < 50 else
            term.yellow if pct_val < 66 else
            term.greenyellow if pct_val < 99 else
            term.green2)
        pct_s_colored = term_style(term.rjust(f"{pct_val:0.1f}", 6))
        writer(f'\n{label_s}: {total_s}, {pct_s_colored} %')
   


def test_support(table, term, writer, timeout, quick, limit_codepoints,
                 limit_errors, expected_width, largest_xpos, report_lbound=2):
    # begin test by version, newest to old
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)

    start_time = time.monotonic()
    outer_ypos, outer_xpos = get_yxpos(term, timeout=timeout)
    for ver, wchars in table:
        writer(term.move_yx(outer_ypos, outer_xpos) + f", version={ver}: " + term.clear_eol)
        orig_start_ypos, orig_start_xpos = get_yxpos(term, timeout=timeout)
        start_ypos, start_xpos = orig_start_ypos, orig_start_xpos
        # prime this variable for breaking out of loop when the distant
        # end stops responding and exceeds timeout in get_yxpos() by
        # return value of -1, -1
        end_ypos, end_xpos = 0, 0
        for wchar in wchars[:limit_codepoints if limit_codepoints else None]:
            # write test character or sequence
            wchars_str = chr(wchar) if isinstance(wchar, int) else ''.join(chr(_wc) for _wc in wchar)
            writer(wchars_str)
            
            # measure cursor distance,
            end_ypos, end_xpos = get_yxpos(term, timeout=timeout)
            if (-1, -1) == (end_ypos, end_xpos):
                writer(term.move_yx(outer_ypos, outer_xpos))
                writer(term.reverse_red(f'Timeout Exceeded ({timeout:.2f}s)'))
                if quick:
                    break
                term.inkey(timeout=1)
            delta_xpos = end_xpos - start_xpos
            delta_ypos = end_ypos - start_ypos
            if delta_ypos != 0 or delta_xpos != expected_width:
                # add failure_report record, conditionally add delta_ypos and
                # delta_xpos only when unexepcted values,
                failure_report[ver].append(({"wchar": unicode_escape_string(wchars_str)}))
                if delta_ypos != 0:
                    failure_report[ver][-1]["delta_ypos"] = delta_ypos
                if delta_xpos != expected_width:
                    failure_report[ver][-1]["measured_by_wcwidth"] = expected_width
                    failure_report[ver][-1]["measured_by_terminal"] = expected_width + delta_xpos
                # and break version test early on --limit-errors.
                if limit_errors and len(failure_report[ver]) >= limit_errors:
                    break
            else:
                success_report[ver] += 1
            if end_xpos > (term.width - largest_xpos) or delta_ypos != 0:
                # out-of-bounds, reset (y, x) to home cursor
                start_ypos, start_xpos = orig_start_ypos, orig_start_xpos
                maybe_clear_eol = term.clear_eol
            else:
                start_ypos, start_xpos = end_ypos, end_xpos + delta_xpos
                maybe_clear_eol = ''
            writer(term.move_yx(start_ypos, start_xpos) + maybe_clear_eol)
        if quick:
            # sub-versions like 12.1.0 are tricky, because there is only one single
            # new codepoint, otherwise stop immediately on first 100% success,
            # except for tables of very small codepoints!
            if wchars and not failure_report[ver] and success_report[ver] >= report_lbound:
                break
            if (-1, -1) == (end_ypos, end_xpos):
                # stop immediately on any timeout
                break
    writer(term.move_yx(outer_ypos, outer_xpos))
    report_versions = [v for _, v in sorted([
        (wcwidth._wcversion_value(_ver), _ver)
        for _ver in set(list(failure_report.keys()) + list(success_report.keys()))
        if len(failure_report[_ver]) or success_report[_ver]])
    ]
    for ver in report_versions:
        if len(failure_report[ver]) + success_report[ver] < report_lbound and limit_codepoints > report_lbound:
            # delete test results from unicode tables with very few changes,
            # wide table 12.1.0 release has just 1 change, and
            # emoji table 1.0 has just 1 change.
            del success_report[ver]
            del failure_report[ver]
    test_total_sum = sum(success_report.values()) + sum([len(v) for v in failure_report.values()])
    writer(f": {test_total_sum:n} wchars total, {time.monotonic() - start_time:.2f}s elapsed.")
    writer(term.clear_eol)

    return {
            ver: {
                "n_errors": len(failure_report[ver]),
                "n_total": len(failure_report[ver]) + success_report[ver],
                "pct_success": make_success_pct(n_errors=len(failure_report[ver]),
                                                n_total=len(failure_report[ver]) + success_report[ver]),
                "failed_codepoints": failure_report[ver],
            }
            for ver in report_versions
    }

def make_success_pct(n_errors, n_total):
    # protect from divide-by-zero and convert decimal to whole percentage points
    return ((n_total - n_errors) / n_total if n_total else 0) * 100

def determine_best_match(wide_results: dict, lbound_pct) -> Optional[float]:
    # Iterate through results of test_wide_support(), determine their success pct
    # as n_errors / n_total, create descending sorted list of [success_pct, unicode_version],
    # and chose the 'best' version above lbound_pct, after sorted order of
    # (pct_success, value_version).
    # This is for the case of mixed 95-100% support rates, at time of this writing,
    # iTerm2 supports 100% of wmoji zwj 12.1, 97% in 13.1, *0%* 14.0, and 99% of 15.1,
    # it just has a gap of support for the ZWJ sequence released in version 14, strange,
    # but in this case it is best to suggest a total version of 15.1.
    results = []
    for ver, result in wide_results.items():
        try:
            results.append((result['pct_success'], wcwidth._wcversion_value(ver), ver))
        except ZeroDivisionError:
            results.append((0, wcwidth._wcversion_value(ver), ver))
    if not results:
        return None
    results.sort(reverse=True)

    best_match = results[0]
    for pct_success, value_version, str_version in results:
        if pct_success >= lbound_pct and value_version > best_match[1]:
            best_match = (pct_success, value_version, str_version)
    return best_match[2] if best_match[0] > 0 else None



def main(stream, quick, limit_codepoints, limit_errors, save_yaml):
    """Program entry point."""
    # set locale support for '{:n}' formatter, https://stackoverflow.com/a/3909907
    locale.setlocale(locale.LC_ALL, '')
    term = blessed.Terminal(stream=sys.__stderr__ if stream == "stderr" else None)
    if not quick:
        assert term.width > 79, ('Terminal must be at least 80 columns wide', term.width)
        assert term.height > 23, ('Terminal must be at least 80 columns wide', term.width)
    writer = functools.partial(
        print, end="", flush=True, file=sys.stderr if stream == "stderr" else None
    )
    writer(
        f"ucs-detect: stream={stream} quick={quick}, "
        f"limit_codepoints={limit_codepoints}, limit_errors={limit_errors}"
    )
    if save_yaml:
        terminal_software = input('Enter "Terminal Software": ')
        terminal_version = input('Enter "Software Version": ')

    stime = time.monotonic()
    try:
        # measure real-time trip (RTT) of distant end
        rtt_ms = determine_simple_rtt_ms(term, timeout=3.2)
    except RuntimeError:
        print("ucs-detect: Unicode Version could not be determined!", file=sys.stderr)
        sys.exit(1)
    else:
        # determine timeout as seconds, but multiply by 100 (!), this is because
        # some terminals have a bit of a barf with many wide characters, try to
        # dynamically generate a reasonable timeout period with 0.25 and 3.2 floor/ceil
        timeout = min(max(0.25, (rtt_ms / 1000) * 100), 3.2)
        writer(
            f"\nucs-detect: Interactive terminal detected ! (rtt={rtt_ms:.2f}ms, timeout={int(timeout*1000):d}ms)"
        )

    # test full-wide unicode table
    writer(f"\nucs-detect: " + term.reverse("Testing, DO NOT TOUCH OR RESIZE!"))
    writer(f"\nucs-detect: WIDE testing")
    wide_results = test_support(table=WIDE_CHARACTERS,
                                     term=term, writer=writer, timeout=timeout,
                                     quick=quick, limit_codepoints=limit_codepoints, limit_errors=limit_errors,
                                     expected_width=2, largest_xpos=4)
    unicode_version = determine_best_match(wide_results, lbound_pct=95)

    writer(f"\nucs-detect: ZWJ testing")
    emoji_zwj_results = test_support(table=EMOJI_ZWJ_SEQUENCES,
                                     term=term, writer=writer, timeout=timeout,
                                     quick=quick, limit_codepoints=limit_codepoints,
                                     limit_errors=limit_errors,
                                     expected_width=2, largest_xpos=20)
    emoji_zwj_version = determine_best_match(emoji_zwj_results, lbound_pct=95)

    language_results = None
    if not quick:
        writer(f"\nucs-detect: testing language support: ")
        orig_ypos, orig_xpos = get_yxpos(term, timeout=timeout)
        writer('\n' * 20)
        if orig_ypos != term.height - 1:
            next_ypos, _ = get_yxpos(term, timeout=timeout)
            top = next_ypos - 19
        else:
            top = max(0, term.height - 20)
        bottom = min(top + 20, term.height - 1)
        try:
            writer(term.csr(top, bottom) + term.move_yx(top, 0) + term.clear_eos)
            language_results = test_language_support(term=term, writer=writer, timeout=timeout,
                                                    orig_xpos=orig_xpos,
                                                    top=top, bottom=bottom,
                                                    unicode_version=unicode_version,
                                                    largest_xpos=15)
        finally:
            writer(term.csr(0, term.height))
            writer(term.move_yx(top, 0) + term.clear_eos)

    writer(f'\nDisplaying success results of {term.bold("Unicode Version")} as Total characters and their success rate')
    display_results_by_version(term=term, writer=writer, results=wide_results, best_match=unicode_version)

    writer(f'\nDisplaying success results of {term.bold("Emoji Unicode Version")} as Total characters and their success rate')
    display_results_by_version(term=term, writer=writer, results=emoji_zwj_results, best_match=emoji_zwj_version)

    if language_results:
        writer(f'\nDisplaying success results of wide and zero-width characters by language')
        display_results_by_language(term=term, writer=writer, results=language_results)

    if save_yaml:
        do_save_yaml(save_yaml, term, terminal_software, terminal_version, stime, wide_results, unicode_version, emoji_zwj_results, emoji_zwj_version, language_results)


def do_save_yaml(save_yaml, term, terminal_software, terminal_version, stime, wide_results, unicode_version, emoji_zwj_results, emoji_zwj_version, language_results):
    results = dict(software=terminal_software,
            version=terminal_version,
            seconds_elapsed=time.monotonic() - stime,
            width=term.width,
            height=term.height,
            python_version=platform.python_version(),
            system=platform.system(),
            datetime=datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
            test_results=dict(
                unicode_wide_version=unicode_version,
                unicode_wide_results=wide_results,
                emoji_zwj_version=emoji_zwj_version,
                emoji_zwj_results=emoji_zwj_results,
                language_results=language_results
            )
        )
    yaml.safe_dump(results, open(save_yaml, 'w'))



def parse_args():
    args = argparse.ArgumentParser()
    # in theory, terminals react more suddenly from stderr, it is unbuffered
    args.add_argument(
        "--stream",
        default="stderr",
        choices=("stderr", "stdout"),
        help="output file descriptor to interactve with in testing",
    )
    args.add_argument(
        "--limit-codepoints",
        type=int,
        default=200,
        help="limit the total number of codepoints of each version",
    )
    args.add_argument(
        "--limit-errors",
        type=int,
        default=15,
        help="limit the total number of errors detected at each version",
    )
    args.add_argument(
        "--quick",
        action="store_true",
        default=False,
        help=(
            "Stop test early at the first version that matches 100%%"
        ),
    )
    args.add_argument(
        "--save-yaml",
        help="Save results as yaml to given filepath, prompts user for software name & version",
        default=None,
    )
    results = vars(args.parse_args())
    if results["quick"]:
        results["limit_codepoints"] = results["limit_codepoints"] or 50
        results["limit_errors"] = results["limit_errors"] or 5

    if results['save_yaml']:
        results['save_yaml'] = os.path.expanduser(results['save_yaml'])
    return results


if __name__ == "__main__":
    sys.exit(main(**parse_args()))


# Thoughts: a general purpose, shell-startup embeddable program, if we used a
# file-backed cache, we could prevent setting the terminal into cbreak or
# interrupting shell startup by using pstree to (try? process above $SHELL?) to
# determine the parent application path(s), and, use the mtime of their binaries
# to determine if we should refresh our attempt at unicode. I guess in theory,
# like a dynamically-linked libvte this wouldn't work .. so maybe it would
# refresh every 90 days or something .. ? unicode only releases once or twice a
# year at most, this is really a problem about how often do terminals update
# their support of unicode, it varies by application for sure. There needs to
# also be a timeout, maybe just a second or two total, before the program stops
# early, for badly programmed automatic systems (not really terminals, but like
# login spammers from botnets) that stop responding, etc.
#
# Findings, we can use as little as --limit-codepoints=1 and get moderately
# accurate results with as few as --limit-codepoints=10 ..
# 
# TODO: I selfishly need 'with term.scrolling_region(n, n):' ..
# TODO: and I also need flush input, just for ^C during this process
