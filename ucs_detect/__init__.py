#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ucs-detect: Reports Unicode version level support of an interactive terminal emulator.

See also,
- https://github.com/jquast/ucs-detect
- https://github.com/jquast/wcwidth
- https://github.com/jquast/blessed

A lot of this code comes from experimentation while developing 'wcwidth' library.
"""
# std imports
import sys
import time
import locale
import argparse
import functools
import random
import collections
from typing import Optional

# 3rd party
import blessed
import wcwidth

# local
from ucs_detect.table_zwj import EMOJI_ZWJ_SEQUENCES
from ucs_detect.table_wide import WIDE_CHARACTERS

def get_yxpos(term, timeout):
    ypos, xpos = term.get_location(timeout=timeout)
    if -1 in (ypos, xpos):
        raise RuntimeError("Terminal is not interactive")
    return (ypos, xpos)


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
    if best_match:
        writer(f'\n{"* Best Match":>16s}')
    else:
        writer(f'\n{"* No Match !":>16s}')

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
            writer(chr(wchar) if isinstance(wchar, int)
                   else ''.join(chr(_wc) for _wc in wchar))
            
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
                if isinstance(wchar, tuple):
                    failure_report[ver].append(({"wchars": wchar}))
                else:
                    failure_report[ver].append(({"wchar": wchar}))
                if delta_ypos != 0:
                    failure_report[ver][-1]["delta_ypos"] = delta_ypos
                if delta_xpos != expected_width:
                    failure_report[ver][-1]["delta_xpos"] = delta_xpos
                # and break version test early on --limit-errors.
                if limit_errors and len(failure_report[ver]) >= limit_errors:
                    break
            else:
                success_report[ver] += 1
            if end_xpos > (term.width - largest_xpos) or delta_ypos != 0:
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
            if success_report[ver] or len(failure_report[ver])
    }

def make_success_pct(n_errors, n_total):
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


def main(stream, quick, limit_codepoints, limit_errors, shuffle):
    """Program entry point."""
    # set locale support for '{:n}' formatter, https://stackoverflow.com/a/3909907
    locale.setlocale(locale.LC_ALL, '')
    term = blessed.Terminal(stream=sys.__stderr__ if stream == "stderr" else None)
    writer = functools.partial(
        print, end="", flush=True, file=sys.stderr if stream == "stderr" else None
    )
    writer(
        f"ucs-detect: stream={stream} quick={quick}, "
        f"limit_codepoints={limit_codepoints}, limit_errors={limit_errors}"
    )

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
        timeout = max(min(0.25, (rtt_ms / 1000) * 100), 3.2)
        writer(
            f"\nucs-detect: Interactive terminal detected ! (rtt_ms={rtt_ms:.1f}ms, timeout={timeout:0.2f}s)"
        )

    # test full-wide unicode table
    writer(f"\nucs-detect: " + term.reverse("Testing, DO NOT TOUCH OR RESIZE!"))
    wide_results = test_support(table=WIDE_CHARACTERS,
                                     term=term, writer=writer, timeout=timeout,
                                     quick=quick, limit_codepoints=limit_codepoints, limit_errors=limit_errors,
                                     expected_width=2, largest_xpos=4)
    unicode_version = determine_best_match(wide_results, lbound_pct=95)

    writer(f"\nucs-detect: " + term.reverse("Testing, DO NOT TOUCH OR RESIZE!"))
    emoji_zwj_results = test_support(table=EMOJI_ZWJ_SEQUENCES,
                                     term=term, writer=writer, timeout=timeout,
                                     quick=quick, limit_codepoints=limit_codepoints, limit_errors=limit_errors,
                                     expected_width=2, largest_xpos=20)
    emoji_zwj_version = determine_best_match(emoji_zwj_results, lbound_pct=95)

    writer(f'\nDisplaying success results of {term.bold("Unicode Version")} as Total characters and their success rate')
    display_results_by_version(term=term, writer=writer, results=wide_results, best_match=unicode_version)

    writer(f'\nDisplaying success results of {term.bold("Emoji Unicode Version")} as Total characters and their success rate')
    display_results_by_version(term=term, writer=writer, results=emoji_zwj_results, best_match=emoji_zwj_version)

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
        "--shuffle",
        action="store_true",
        default=False,
        help="randomize order of codepoints tested",
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
    results = vars(args.parse_args())
    if results["quick"]:
        results["limit_codepoints"] = results["limit_codepoints"] or 50
        results["limit_errors"] = results["limit_errors"] or 5
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