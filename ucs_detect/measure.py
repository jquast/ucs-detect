# std
import os
import re
import sys
import time
import bisect
import codecs
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


def extract_unique_graphemes(text):
    """Extract unique grapheme clusters from text, grouped by display width."""
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
    """Wrapper around term.get_location() that retries on false timeouts from VM clock skew."""
    for attempt in range(max_retries):
        start = time.monotonic()
        ypos, xpos = term.get_location(timeout=timeout)
        elapsed = time.monotonic() - start

        if (ypos, xpos) != (-1, -1):
            return (ypos, xpos)

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
    from prettytable.colortable import ColorTable, Theme
    theme = Theme(
        default_color=term.cyan,
        vertical_color=term.bold_black,
        horizontal_color=term.bold_black,
        junction_color=term.bold_black,
    )
    table = ColorTable(theme=theme)
    table.field_names = [
        term.magenta("#"),
        term.magenta("Codepoint"),
        term.magenta("Python"),
        term.magenta("Category"),
        term.magenta("wcwidth"),
        term.magenta("Name"),
    ]
    table.align["#"] = "r"
    table.align["Codepoint"] = "l"
    table.align["Python"] = "l"
    table.align["Category"] = "l"
    table.align["wcwidth"] = "r"
    table.align["Name"] = "l"
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

    interior = wcwidth.width(wchars_display) + 2
    border = "+" + "-" * interior + "+"
    writer(f"{border}\n|{wcwidth.center(wchars_display, interior)}|\n{border}\n")

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
    **_kwargs,
):
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)
    time_report = {}
    tested_graphemes = {}
    lang_start_times = {}
    category_start = time.monotonic()
    category_tested = 0
    category_budget_exceeded = False

    for expected_width, lang_entries in lang_graphemes:
        if category_budget_exceeded:
            break
        for lang, graphemes in lang_entries:
            if (limit_category_time and category_tested >= 20
                    and time.monotonic() - category_start >= limit_category_time):
                category_budget_exceeded = True
                break
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

            cell_inner = expected_width + 3
            num_columns = max(1, (term.width - 1) // cell_inner)

            n_inherited = inherited_ok + inherited_fail
            if n_inherited:
                inherited_msg = f", {n_inherited} shared"
            else:
                inherited_msg = ""
            label = (
                f"Testing {lang} w={expected_width}"
                f" ({len(novel)} novel{inherited_msg})"
            )
            writer("\n" + status_header(term, label) + "\n")

            effective_limit = limit_graphemes
            if limit_category_time and category_tested >= 20:
                elapsed = time.monotonic() - category_start
                remaining = limit_category_time - elapsed
                if remaining > 0:
                    cps = category_tested / elapsed
                    estimated = int(remaining * cps)
                    if effective_limit:
                        effective_limit = min(effective_limit, estimated)
                    else:
                        effective_limit = estimated

            grapheme_count = 0
            error_count = 0
            col = 0
            for idx, grapheme in enumerate(novel):
                if effective_limit and grapheme_count >= effective_limit:
                    break
                if limit_errors and error_count >= limit_errors:
                    break

                grapheme_id = f"{lang}-{expected_width}-{idx:02x}"

                if col == 0:
                    writer(term.magenta("║ "))
                else:
                    writer(term.magenta(" \u00b7 "))

                start_ypos, start_xpos = _get_pos_or_exit(term, writer, timeout)

                writer(term.cyan(grapheme))
                if cursor_report_delay_ms:
                    time.sleep(cursor_report_delay_ms / 1000.0)
                end_ypos, end_xpos = _get_pos_or_exit(term, writer, timeout)

                delta_ypos = end_ypos - start_ypos
                delta_xpos = end_xpos - start_xpos

                if (delta_ypos, delta_xpos) == (0, expected_width):
                    success_report[lang] += 1
                    tested_graphemes[grapheme] = (lang, True)
                else:
                    failure_report[lang].append(
                        {"grapheme_id": grapheme_id,
                         "wchars": unicode_escape_string(grapheme)}
                    )
                    if delta_ypos != 0:
                        failure_report[lang][-1]["delta_ypos"] = delta_ypos
                    failure_report[lang][-1][
                        "measured_by_wcwidth"
                    ] = expected_width
                    failure_report[lang][-1][
                        "measured_by_terminal"
                    ] = delta_xpos
                    error_count += 1
                    tested_graphemes[grapheme] = (lang, False)

                    writer(term.move_yx(start_ypos, start_xpos))
                    writer(term.red(grapheme))
                    writer(term.magenta(" ║") + "\n")
                    col = 0

                    if stop_at_error and stop_at_error.matches_language(lang):
                        should_continue = display_error_and_prompt(
                            term=term,
                            writer=writer,
                            context_name=f"language '{lang}' ({grapheme_id})",
                            wchars_display=grapheme,
                            measured_by_terminal=delta_xpos,
                            measured_by_wcwidth=expected_width,
                        )
                        if not should_continue:
                            stop_at_error.disable()

                    grapheme_count += 1
                    category_tested += 1
                    continue

                grapheme_count += 1
                category_tested += 1
                col += 1

                if col >= num_columns:
                    writer(term.magenta(" ║") + "\n")
                    col = 0

            if col > 0:
                writer(term.magenta(" ║") + "\n")

    for lang, start_time in lang_start_times.items():
        time_report[lang] = time.monotonic() - start_time

    report_languages = [
        language
        for language in failure_report.keys() | success_report.keys()
        if failure_report[language] or success_report[language]
    ]

    return {
        lang: _make_result_entry(
            n_errors=len(failure_report[lang]),
            n_total=len(failure_report[lang]) + success_report[lang],
            elapsed=time_report.get(lang, 0.0),
            extra={"failed": failure_report[lang]},
        )
        for lang in report_languages
    }


def wchar_to_str(wchar):
    """Convert a codepoint (int) or sequence (tuple of ints) to a string."""
    if isinstance(wchar, int):
        return chr(wchar)
    return "".join(chr(cp) for cp in wchar)


def exit_and_display_timeout_error(term, writer, timeout, **_kwargs):
    writer("\n" + term.reverse_red(f"Timeout Exceeded ({timeout:.1f}s)") + "\n")
    sys.exit(1)


def _get_pos_or_exit(term, writer, timeout):
    """Get cursor position, exiting on timeout."""
    ypos, xpos = get_location_with_retry(term, timeout)
    if (ypos, xpos) == (-1, -1):
        exit_and_display_timeout_error(term, writer, timeout)
    return ypos, xpos


def _make_result_entry(n_errors, n_total, elapsed, extra=None):
    """Build a standard result dict for test reporting."""
    entry = {
        "n_errors": n_errors,
        "n_total": n_total,
        "pct_success": make_success_pct(n_errors, n_total),
        "seconds_elapsed": elapsed,
        "codepoints_per_second": (n_total / elapsed) if elapsed > 0 else 0.0,
    }
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
):
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)
    time_report = {}

    if suppress_output:
        outer_ypos, outer_xpos = _get_pos_or_exit(term, writer, timeout)

    cell_inner = expected_width + 3
    num_columns = max(1, (term.width - 1) // cell_inner)

    category_start = time.monotonic()
    category_tested = 0
    time_limited = False

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
            if limit_codepoints:
                wchars_slice = wchars[:limit_codepoints]
            elif limit_pct and 0 < limit_pct < 100:
                step = max(1, round(100 / limit_pct))
                wchars_slice = wchars[::step]
            else:
                wchars_slice = wchars

            if limit_category_time and category_tested >= 20:
                elapsed = time.monotonic() - category_start
                remaining = limit_category_time - elapsed
                if remaining > 0:
                    cps = category_tested / elapsed
                    max_items = int(remaining * cps)
                    if max_items < len(wchars_slice):
                        wchars_slice = wchars_slice[:max_items]
                        time_limited = True

            if suppress_output:
                writer(term.move_yx(outer_ypos, outer_xpos) + term.clear_eol)
            else:
                hdr_label = label or (test_type.upper() if test_type else "test")
                pct_note = ""
                if limit_pct and 0 < limit_pct < 100 and not limit_codepoints:
                    pct_note = f", {limit_pct}% sampled"
                if time_limited:
                    pct_note += ", time-limited"
                header = (f"Testing {hdr_label} v={ver}"
                          f" ({len(wchars_slice)}/{n_wchars}{pct_note})")
                writer("\n" + status_header(term, header) + "\n")

            col = 0
            end_ypos, end_xpos = 0, 0

            for wchar in wchars_slice:
                category_tested += 1
                if (limit_category_time and category_tested % 50 == 0
                        and time.monotonic() - category_start >= limit_category_time):
                    break
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
                        term.move_yx(outer_ypos, outer_xpos) + term.clear_eol
                    )
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
                    failure_report[ver].append(
                        {"wchar": unicode_escape_string(wchars_str)}
                    )
                    if delta_ypos != 0:
                        failure_report[ver][-1]["delta_ypos"] = delta_ypos
                    if delta_xpos != expected_width:
                        failure_report[ver][-1][
                            "measured_by_wcwidth"
                        ] = expected_width
                        failure_report[ver][-1][
                            "measured_by_terminal"
                        ] = delta_xpos

                    if not suppress_output:
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

                if not suppress_output:
                    col += 1
                    if col >= num_columns:
                        writer(term.magenta(" ║") + "\n")
                        col = 0

            if not suppress_output and col > 0:
                writer(term.magenta(" ║") + "\n")

            time_report[ver] = time.monotonic() - ver_start_time
            if (limit_category_time
                    and time.monotonic() - category_start >= limit_category_time):
                break

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
    return {
        ver: _make_result_entry(
            n_errors=len(failure_report[ver]),
            n_total=len(failure_report[ver]) + success_report[ver],
            elapsed=time_report.get(ver, 0.0),
            extra={"failed_codepoints": failure_report[ver]},
        )
        for ver in report_versions
    }

def make_success_pct(n_errors, n_total):
    return ((n_total - n_errors) / n_total if n_total else 0) * 100


def parse_udhr():
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
