"""Terminal Unicode width measurement utilities."""

# std
# std imports
import os
import re
import sys
import time
import bisect
import codecs
import contextlib
import collections
import unicodedata

# 3rd party
import wcwidth

# local
from ucs_detect import terminal

# Unicode ranges where most fonts lack glyphs
UNCOMMON_WIDE_RANGES = (
    (0x16FF0, 0x18CFF),   # Ideographic Symbols, Tangut, Khitan Small Script
    (0x18D00, 0x18DFF),   # Tangut Supplement + Components
    (0x1B000, 0x1B2FF),   # Kana Supplement/Extended
    (0x20000, 0x2A6FF),   # CJK Extension B + unassigned tail
    (0x2A700, 0x2B73F),   # CJK Extension C
    (0x2B740, 0x2B81F),   # CJK Extension D
    (0x2B820, 0x2CEAF),   # CJK Extension E
    (0x2CEB0, 0x2EBEF),   # CJK Extension F
    (0x2EBF0, 0x2F7FF),   # CJK Extension I
    (0x2F800, 0x2FFFF),   # CJK Compat Ideographs Supplement + unassigned
    (0x30000, 0x3134F),   # CJK Extension G
    (0x31350, 0x323AF),   # CJK Extension H
    (0x323B0, 0x3FFFD),   # Future CJK extensions (reserved)
)

_UNCOMMON_STARTS = tuple(s for s, _ in UNCOMMON_WIDE_RANGES)


def _is_uncommon(codepoint):
    """Return True if codepoint is in an uncommon wide range."""
    idx = bisect.bisect_right(_UNCOMMON_STARTS, codepoint) - 1
    if idx < 0:
        return False
    start, end = UNCOMMON_WIDE_RANGES[idx]
    return start <= codepoint <= end


def status_header(term, label):
    """Return a centered status header with magenta-colorized numbers."""
    colored_label = re.sub(r'\d+', lambda m: term.magenta(m.group()), label)
    header_text = f"[ {colored_label} ]"
    plain_text = f"[ {label} ]"
    text_width = wcwidth.wcswidth(plain_text)
    pad_total = max(0, term.width - text_width)
    pad_left = pad_total // 2
    pad_right = pad_total - pad_left
    return ('═' * pad_left
            + header_text
            + '═' * pad_right)


def _write_final_sampling_rate(writer, term, final_pct, initial_pct):
    """Display final sampling rate message when time-budget reduced it."""
    if final_pct != initial_pct and final_pct > 0:
        msg = f"Final sampling rate was {final_pct}% due to category time limit"
        writer("\n" + status_header(term, msg) + "\n")


def extract_unique_graphemes(text):
    """Extract unique grapheme clusters from text, grouped by display width."""
    # 3rd party
    from wcwidth import iter_graphemes

    seen = set()
    by_width = collections.defaultdict(list)
    for grapheme in iter_graphemes(text):
        if grapheme.isspace() or grapheme in seen:
            continue
        seen.add(grapheme)
        w = wcwidth.wcswidth(grapheme)
        if w > 0:
            by_width[w].append(grapheme)
    return {w: sorted(gs) for w, gs in sorted(by_width.items())}


def get_location_with_retry(term, timeout, max_retries=3):
    """Wrap term.get_location() with retries for false timeouts from VM clock skew."""
    for attempt in range(max_retries):
        start = time.monotonic()
        ypos, xpos = term.get_location(timeout=timeout)
        elapsed = time.monotonic() - start

        if (ypos, xpos) != (-1, -1):
            return (ypos, xpos)

        # Drain stale CPR responses before retrying or giving up.
        term.flushinp(timeout=0.05)

        if elapsed < (timeout * 0.1):
            timeout = timeout * 1.5
            continue

        return (-1, -1)

    return (-1, -1)


def measure_width(term, writer, text, timeout):
    """Measure actual rendered width of text using cursor position reports."""
    _, x1 = get_location_with_retry(term, timeout)
    if x1 == -1:
        return None
    writer(text)
    _, x2 = get_location_with_retry(term, timeout)
    if x2 == -1:
        return None
    writer(term.move_x(x1) + ' ' * (x2 - x1) + term.move_x(x1))
    return x2 - x1


def make_printf_hex(wchar):
    """Convert a Unicode string to printf hex escape format."""
    return repr(wchar.encode("utf8"))[2:-1]


def _make_codepoint_table(term, wchars_display):
    """Build a prettytable showing codepoint breakdown of a character sequence."""
    # 3rd party
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = [
        term.magenta("#"),
        term.magenta("Codepoint"),
        term.magenta("Python"),
        term.magenta("Category"),
        term.magenta("wcwidth"),
        term.magenta("Name"),
    ]
    table.align = {
        "#": "r",
        "Codepoint": "l",
        "Python": "l",
        "Category": "l",
        "wcwidth": "r",
        "Name": "l",
    }
    for idx, char in enumerate(wchars_display):
        codepoint_val = ord(char)
        if codepoint_val > 0xFFFF:
            cp_str = f"U+{codepoint_val:08X}"
            py_str = f"\\U{codepoint_val:08x}"
        else:
            cp_str = f"U+{codepoint_val:04X}"
            py_str = f"\\u{codepoint_val:04x}"
        table.add_row([
            idx + 1,
            cp_str,
            py_str,
            unicodedata.category(char),
            wcwidth.wcwidth(char),
            unicodedata.name(char, "(unknown)"),
        ])
    return table


def display_error_and_prompt(
    term, writer, context_name, wchars_display, measured_by_terminal, measured_by_wcwidth
):
    """Display error details and prompt user to continue or disable stopping."""
    writer(f"\n{term.bold(f'Failure in {context_name}:')}\n")

    writer(str(_make_codepoint_table(term, wchars_display)) + "\n")

    text_width = wcwidth.wcswidth(wchars_display)
    interior = max(text_width, len(wchars_display)) + 2
    border = "+" + "-" * interior + "+"
    total_padding = max(0, interior - text_width)
    left_pad = total_padding // 2 + (total_padding & interior & 1)
    right_pad = total_padding - left_pad
    centered = " " * left_pad + wchars_display + " " * right_pad
    writer(f"{border}\n|{centered}|\n{border}\n")

    writer(f"\nmeasured by terminal: {measured_by_terminal}\n")
    writer(f"measured by wcwidth:  {measured_by_wcwidth}\n")

    unicode_escaped = unicode_escape_string(wchars_display)
    printf_hex = make_printf_hex(wchars_display)

    writer("\nShell\n-----\n")
    writer(f"printf '{printf_hex}\\n'\n")

    writer("\nPython\n------\n")
    writer(f'python -c "print(\'{unicode_escaped}\')"\n')

    writer(f"\n{term.bold('press return for next error, or')} "
           f"{term.bold_red('n')} {term.bold('for non-stop:')}")

    key = term.inkey()
    writer("\n")

    return key.lower() != 'n'


def test_language_support(
    lang_graphemes,
    term,
    writer,
    timeout,
    limit_graphemes,
    limit_errors,
    stop_at_error=None,
    cursor_report_delay_ms=0,
    limit_category_time=0,
    limit_graphemes_pct=0,
    silent=False,
    bg_rgb=None,
    **_kwargs,
):
    """Test terminal support for language graphemes."""
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)
    time_report = {}
    tested_graphemes = {}
    lang_start_times = {}
    category_start = time.monotonic()
    category_tested = 0
    category_seen = 0
    final_pct = limit_graphemes_pct
    global_step = 0
    if limit_graphemes_pct and 0 < limit_graphemes_pct < 100:
        global_step = max(1, round(100 / limit_graphemes_pct))

    for expected_width, lang_entries in lang_graphemes:
        for lang, graphemes in lang_entries:
            if lang not in lang_start_times:
                lang_start_times[lang] = time.monotonic()

            novel = [g for g in graphemes if g not in tested_graphemes]
            inherited_ok = sum(
                1 for g in graphemes
                if g in tested_graphemes and tested_graphemes[g][1]
            )
            inherited_fail = sum(
                1 for g in graphemes
                if g in tested_graphemes and not tested_graphemes[g][1]
            )
            success_report[lang] += inherited_ok
            for g in graphemes:
                if g in tested_graphemes and not tested_graphemes[g][1]:
                    prior_lang = tested_graphemes[g][0]
                    failure_report[lang].append(
                        {"wchars": unicode_escape_string(g),
                         "measured_by_wcwidth": expected_width,
                         "inherited_from": prior_lang}
                    )

            if not novel:
                continue

            # recalculate global step from time budget
            if limit_category_time and category_tested >= 20:
                elapsed = time.monotonic() - category_start
                remaining = max(0, limit_category_time - elapsed)
                cps = (category_tested / elapsed
                       if elapsed > 0 else 0)
                max_items = max(1, int(remaining * cps)) if remaining > 0 else 1
                # compute step that would produce max_items from remaining
                # graphemes, but we don't know the total remaining, so use
                # a ratio: if we can do max_items and current step produces
                # too many, increase the step
                if max_items < 10 and global_step < 100:
                    global_step = 100
                    final_pct = 1
                elif cps > 0 and remaining > 0:
                    desired_step = max(1, int(category_tested / (remaining * cps))
                                       ) if remaining * cps > 0 else 100
                    if desired_step != global_step:
                        global_step = max(1, min(100, desired_step))
                        final_pct = max(1, round(100 / global_step))

            cell_inner = expected_width + 3
            num_columns = max(1, (term.width - 1) // cell_inner)

            n_inherited = inherited_ok + inherited_fail
            if n_inherited:
                inherited_msg = f", {n_inherited} shared"
            else:
                inherited_msg = ""
            pct_note = ""
            effective_pct = max(1, round(100 / global_step)) if global_step > 1 else 0
            if effective_pct and 0 < effective_pct < 100:
                pct_note = f", {effective_pct}% sampled"
            if final_pct != limit_graphemes_pct:
                pct_note += ", time-limited"
            n_novel = len(novel)
            n_to_test = len(novel)
            if global_step > 1:
                n_to_test = max(1, n_novel // global_step)
            if limit_graphemes and limit_graphemes < n_to_test:
                n_to_test = limit_graphemes
            label = (
                f"Testing {lang} w={expected_width}"
                f" ({n_to_test}/{n_novel} novel{inherited_msg}{pct_note})"
            )
            if not silent:
                writer("\n" + status_header(term, label) + "\n")

            # Get initial position for silent mode
            if silent:
                outer_ypos, outer_xpos = _get_pos_or_exit(term, writer, timeout)

            grapheme_count = 0
            error_count = 0
            col = 0
            for idx, grapheme in enumerate(novel):
                if limit_graphemes and grapheme_count >= limit_graphemes:
                    break
                if limit_errors and error_count >= limit_errors:
                    break
                first_for_lang = (idx == 0)
                if (global_step > 1
                        and category_seen % global_step != 0
                        and not first_for_lang):
                    category_seen += 1
                    continue
                category_seen += 1

                grapheme_id = f"{lang}-{expected_width}-{idx:02x}"

                if silent:
                    fg = term.color_rgb(*bg_rgb) if bg_rgb else term.black
                    writer(f'\r{fg}{grapheme}')
                    if cursor_report_delay_ms:
                        time.sleep(cursor_report_delay_ms / 1000.0)
                    end_ypos, end_xpos = get_location_with_retry(
                        term, timeout
                    )
                    if (-1, -1) == (end_ypos, end_xpos):
                        writer(f'{term.normal}\r{term.clear_eol}')
                        writer(
                            term.reverse_red(
                                f"Timeout Exceeded ({timeout:.2f}s)"
                            )
                        )
                        break
                    delta_xpos = end_xpos - outer_xpos
                    delta_ypos = end_ypos - outer_ypos
                    writer(f'{term.normal}\r{term.clear_eol}')
                else:
                    if col == 0:
                        writer(term.magenta("║ "))
                    else:
                        writer(term.magenta(" \u00b7 "))

                    start_ypos, start_xpos = _get_pos_or_exit(
                        term, writer, timeout)

                    writer(term.cyan(grapheme))
                    if cursor_report_delay_ms:
                        time.sleep(cursor_report_delay_ms / 1000.0)
                    end_ypos, end_xpos = _get_pos_or_exit(
                        term, writer, timeout)

                    delta_ypos = end_ypos - start_ypos
                    delta_xpos = end_xpos - start_xpos

                if (delta_ypos, delta_xpos) == (0, expected_width):
                    success_report[lang] += 1
                    tested_graphemes[grapheme] = (lang, True)
                else:
                    entry = {
                        "grapheme_id": grapheme_id,
                        "wchars": unicode_escape_string(grapheme),
                        "measured_by_wcwidth": expected_width,
                        "measured_by_terminal": delta_xpos,
                    }
                    if delta_ypos != 0:
                        entry["delta_ypos"] = delta_ypos
                    failure_report[lang].append(entry)
                    error_count += 1
                    tested_graphemes[grapheme] = (lang, False)

                    if not silent:
                        writer(term.move_yx(start_ypos, start_xpos))
                        writer(term.red(grapheme))
                        writer(term.magenta(" ║") + "\n")
                        col = 0

                    if (stop_at_error
                            and stop_at_error.matches_language(lang)):
                        should_continue = display_error_and_prompt(
                            term=term,
                            writer=writer,
                            context_name=(
                                f"language '{lang}' ({grapheme_id})"
                            ),
                            wchars_display=grapheme,
                            measured_by_terminal=delta_xpos,
                            measured_by_wcwidth=expected_width,
                        )
                        if not should_continue:
                            stop_at_error.disable()

                    if limit_errors and error_count >= limit_errors:
                        break
                    continue

                grapheme_count += 1
                category_tested += 1
                if not silent:
                    col += 1
                    if col >= num_columns:
                        writer(term.magenta(" ║") + "\n")
                        col = 0

            if not silent and col > 0:
                writer(term.magenta(" ║") + "\n")

    if not silent:
        _write_final_sampling_rate(writer, term, final_pct, limit_graphemes_pct)

    for lang, start_time in lang_start_times.items():
        time_report[lang] = time.monotonic() - start_time

    report_languages = [
        language
        for language in failure_report.keys() | success_report.keys()
        if failure_report[language] or success_report[language]
    ]

    result_pct = (final_pct if final_pct != limit_graphemes_pct
                  else None)
    return {
        lang: _make_result_entry(
            n_errors=len(failure_report[lang]),
            n_total=len(failure_report[lang]) + success_report[lang],
            elapsed=time_report.get(lang, 0.0),
            extra={"failed": failure_report[lang]},
            sampled_pct=result_pct,
        )
        for lang in report_languages
    }


def wchar_to_str(wchar):
    """Convert a codepoint (int) or sequence (tuple of ints) to a string."""
    if isinstance(wchar, int):
        return chr(wchar)
    return "".join(chr(cp) for cp in wchar)


def exit_and_display_timeout_error(term, writer, timeout, **_kwargs):
    """Display timeout error and exit."""
    term.flushinp(timeout=0.05)
    writer("\n" + term.reverse_red(f"Timeout Exceeded ({timeout:.1f}s)") + "\n")
    sys.exit(1)


def _get_pos_or_exit(term, writer, timeout):
    """Get cursor position, exiting on timeout."""
    ypos, xpos = get_location_with_retry(term, timeout)
    if (ypos, xpos) == (-1, -1):
        exit_and_display_timeout_error(term, writer, timeout)
    return ypos, xpos


def _make_result_entry(n_errors, n_total, elapsed, extra=None,
                       sampled_pct=None):
    """Build a standard result dict for test reporting."""
    entry = {
        "n_errors": n_errors,
        "n_total": n_total,
        "pct_success": make_success_pct(n_errors, n_total),
    }
    if sampled_pct is not None and sampled_pct < 100:
        entry["sampled_pct"] = sampled_pct
    if extra:
        entry.update(extra)
    return entry


def test_support(
    table,
    term,
    writer,
    timeout,
    limit_codepoints,
    limit_errors,
    expected_width,
    suppress_output=False,
    stop_at_error=None,
    test_type=None,
    label=None,
    cursor_report_delay_ms=0,
    limit_pct=0,
    include_uncommon=True,
    limit_category_time=0,
    silent=False,
    bg_rgb=None,
):
    """Test terminal support for a Unicode character table."""
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)
    time_report = {}

    if suppress_output or silent:
        outer_ypos, outer_xpos = _get_pos_or_exit(term, writer, timeout)

    cell_inner = expected_width + 3
    num_columns = max(1, (term.width - 1) // cell_inner)

    category_start = time.monotonic()
    category_tested = 0
    time_limited = False
    final_pct = limit_pct

    with terminal.maybe_grapheme_clustering_mode(term):
        for ver, wchars in table:
            if limit_category_time and category_tested >= 20:
                elapsed = time.monotonic() - category_start
                remaining = limit_category_time - elapsed
                if remaining <= 0:
                    break

            ver_start_time = time.monotonic()
            if not include_uncommon:
                wchars = tuple(
                    w for w in wchars
                    if not _is_uncommon(w if isinstance(w, int) else w[0])
                )
            n_wchars = len(wchars)
            effective_pct = final_pct if time_limited else limit_pct

            if limit_codepoints:
                wchars_slice = wchars[:limit_codepoints]
            elif effective_pct and 0 < effective_pct < 100:
                step = max(1, round(100 / effective_pct))
                wchars_slice = wchars[::step]
            else:
                wchars_slice = wchars

            if limit_category_time and category_tested >= 20:
                elapsed = time.monotonic() - category_start
                remaining = limit_category_time - elapsed
                if remaining > 0:
                    cps = (category_tested / elapsed
                           if elapsed > 0 else 0)
                    max_items = int(remaining * cps)
                    if max_items < len(wchars_slice):
                        if not limit_codepoints and n_wchars > 0:
                            # re-stride to maintain breadth, minimum 1%
                            new_pct = max(1, int(100 * max_items / n_wchars))
                            new_step = max(1, round(100 / new_pct))
                            wchars_slice = wchars[::new_step]
                            effective_pct = new_pct
                            final_pct = new_pct
                        else:
                            wchars_slice = wchars_slice[:max(1, max_items)]
                        time_limited = True
                    elif time_limited and not limit_codepoints and n_wchars > 0:
                        # ahead of schedule, increase sampling rate
                        new_pct = min(100, max(final_pct,
                                               int(100 * max_items / n_wchars)))
                        if new_pct > effective_pct:
                            if new_pct >= 100:
                                wchars_slice = wchars
                            else:
                                new_step = max(1, round(100 / new_pct))
                                wchars_slice = wchars[::new_step]
                            effective_pct = new_pct
                            final_pct = new_pct

            if suppress_output or silent:
                writer(term.move_yx(outer_ypos, outer_xpos) + term.clear_eol)
            else:
                hdr_label = label or (test_type.upper() if test_type else "test")
                pct_note = ""
                if effective_pct and 0 < effective_pct < 100 and not limit_codepoints:
                    pct_note = f", {effective_pct}% sampled"
                if time_limited:
                    pct_note += ", time-limited"
                header = (f"Testing {hdr_label} v={ver}"
                          f" ({len(wchars_slice)}/{n_wchars}{pct_note})")
                writer("\n" + status_header(term, header) + "\n")

            col = 0
            for wchar in wchars_slice:
                category_tested += 1
                wchars_str = wchar_to_str(wchar)

                if suppress_output:
                    writer(wchars_str)
                    if cursor_report_delay_ms:
                        time.sleep(cursor_report_delay_ms / 1000.0)
                    end_ypos, end_xpos = get_location_with_retry(
                        term, timeout
                    )
                    if (-1, -1) == (end_ypos, end_xpos):
                        writer(term.move_yx(outer_ypos, outer_xpos))
                        writer(
                            term.reverse_red(
                                f"Timeout Exceeded ({timeout:.2f}s)"
                            )
                        )
                        break
                    delta_xpos = end_xpos - outer_xpos
                    delta_ypos = end_ypos - outer_ypos
                    writer(
                        term.move_yx(outer_ypos, outer_xpos)
                        + term.clear_eol
                    )
                elif silent:
                    fg = term.color_rgb(*bg_rgb) if bg_rgb else term.black
                    writer(f'\r{fg}{wchars_str}')
                    if cursor_report_delay_ms:
                        time.sleep(cursor_report_delay_ms / 1000.0)
                    end_ypos, end_xpos = get_location_with_retry(
                        term, timeout
                    )
                    if (-1, -1) == (end_ypos, end_xpos):
                        writer(f'{term.normal}\r{term.clear_eol}')
                        writer(
                            term.reverse_red(
                                f"Timeout Exceeded ({timeout:.2f}s)"
                            )
                        )
                        break
                    delta_xpos = end_xpos - outer_xpos
                    delta_ypos = end_ypos - outer_ypos
                    writer(f'{term.normal}\r{term.clear_eol}')
                else:
                    if col == 0:
                        writer(term.magenta("║ "))
                    else:
                        writer(term.magenta(" \u00b7 "))

                    start_ypos, start_xpos = _get_pos_or_exit(
                        term, writer, timeout)

                    writer(term.cyan(wchars_str))
                    if cursor_report_delay_ms:
                        time.sleep(cursor_report_delay_ms / 1000.0)
                    end_ypos, end_xpos = _get_pos_or_exit(
                        term, writer, timeout)

                    delta_ypos = end_ypos - start_ypos
                    delta_xpos = end_xpos - start_xpos

                if (delta_ypos, delta_xpos) == (0, expected_width):
                    success_report[ver] += 1
                else:
                    entry = {"wchar": unicode_escape_string(wchars_str)}
                    if delta_ypos != 0:
                        entry["delta_ypos"] = delta_ypos
                    if delta_xpos != expected_width:
                        entry["measured_by_wcwidth"] = expected_width
                        entry["measured_by_terminal"] = delta_xpos
                    failure_report[ver].append(entry)

                    if not suppress_output and not silent:
                        writer(term.move_yx(start_ypos, start_xpos))
                        writer(term.red(wchars_str))
                        writer(term.magenta(" ║") + "\n")
                        col = 0

                    if (stop_at_error and test_type
                            and stop_at_error.matches_test_type(test_type)):
                        should_continue = display_error_and_prompt(
                            term=term,
                            writer=writer,
                            context_name=(
                                f"{test_type.upper()} test (version {ver})"
                            ),
                            wchars_display=wchars_str,
                            measured_by_terminal=delta_xpos,
                            measured_by_wcwidth=expected_width,
                        )
                        if not should_continue:
                            stop_at_error.disable()

                    if limit_errors and len(failure_report[ver]) >= limit_errors:
                        break
                    continue

                if not suppress_output and not silent:
                    col += 1
                    if col >= num_columns:
                        writer(term.magenta(" ║") + "\n")
                        col = 0

            if not suppress_output and not silent and col > 0:
                writer(term.magenta(" ║") + "\n")

            ver_elapsed = time.monotonic() - ver_start_time
            time_report[ver] = ver_elapsed

            if (limit_category_time
                    and time.monotonic() - category_start
                    >= limit_category_time):
                break

    if time_limited and not suppress_output and not silent:
        _write_final_sampling_rate(writer, term, final_pct, limit_pct)

    report_versions = [
        v
        for _, v in sorted(
            [
                (wcwidth._wcversion_value(_ver), _ver)
                for _ver in failure_report.keys() | success_report.keys()
                if failure_report[_ver] or success_report[_ver]
            ]
        )
    ]
    result_pct = final_pct if time_limited else None
    return {
        ver: _make_result_entry(
            n_errors=len(failure_report[ver]),
            n_total=len(failure_report[ver]) + success_report[ver],
            elapsed=time_report.get(ver, 0.0),
            extra={"failed_codepoints": failure_report[ver]},
            sampled_pct=result_pct,
        )
        for ver in report_versions
    }


def make_success_pct(n_errors, n_total):
    """Calculate success percentage from error and total counts."""
    return ((n_total - n_errors) / n_total if n_total else 0) * 100


def parse_udhr():
    """Parse UDHR text files into language grapheme data."""
    path_udhr = os.path.join(os.path.dirname(__file__), 'udhr')
    for fname in sorted(os.listdir(path_udhr)):
        if not fname.lower().endswith('.txt'):
            continue

        full_path = os.path.join(path_udhr, fname)

        with open(full_path) as fin:
            language = fin.readline().split('-', 1)[1].strip()
            while True:
                line = fin.readline()
                if line.startswith('---'):
                    break
                elif not line:
                    raise RuntimeError(f'No marker found in {fname!r}, expected "---"')

            is_interesting = False
            while True:
                line = fin.readline()
                if not line:
                    break
                stripped = line.strip()
                if stripped:
                    wcs_width = wcwidth.wcswidth(stripped)
                    if wcs_width == -1 or wcs_width != len(stripped):
                        is_interesting = True
                        break

        if not is_interesting:
            continue

        with open(full_path) as fin:
            fin.readline()
            while True:
                line = fin.readline()
                if line.startswith('---'):
                    break

            text_parts = []
            while True:
                line = fin.readline()
                if not line:
                    break
                text_parts += line.strip().split() if line.strip() else ""
            yield language, ' '.join(text_parts)


def unicode_escape_string(input_str):
    """Return the Unicode escape representation of a string."""
    return codecs.encode(input_str, "unicode-escape").decode("utf-8")
