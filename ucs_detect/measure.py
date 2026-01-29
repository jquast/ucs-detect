# std
import os
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

# Unicode ranges where most fonts lack glyphs, causing slow fallback lookups
# and replacement character rendering. Sorted by start for bisect lookup.
UNCOMMON_WIDE_RANGES = (
    (0x17000, 0x18CD5),   # Tangut
    (0x18D00, 0x18D7F),   # Tangut Supplement
    (0x1B000, 0x1B2FF),   # Kana Supplement/Extended
    (0x20000, 0x2A6DF),   # CJK Extension B
    (0x2A700, 0x2B73F),   # CJK Extension C
    (0x2B740, 0x2B81F),   # CJK Extension D
    (0x2B820, 0x2CEAF),   # CJK Extension E
    (0x2CEB0, 0x2EBEF),   # CJK Extension F
    (0x2EBF0, 0x2F7FF),   # CJK Extension I
    (0x30000, 0x3134F),   # CJK Extension G
    (0x31350, 0x323AF),   # CJK Extension H
    (0x323B0, 0x3FFFD),   # Future CJK extensions (reserved)
)

_UNCOMMON_STARTS = tuple(s for s, _ in UNCOMMON_WIDE_RANGES)


def _is_uncommon(codepoint):
    """Return True if codepoint is in an uncommon wide range.

    :param int codepoint: Unicode codepoint value.
    :rtype: bool
    """
    idx = bisect.bisect_right(_UNCOMMON_STARTS, codepoint) - 1
    if idx < 0:
        return False
    start, end = UNCOMMON_WIDE_RANGES[idx]
    return start <= codepoint <= end


def extract_unique_graphemes(text):
    """
    Extract unique grapheme clusters from text, grouped by display width.

    :param text: Unicode text to extract graphemes from.
    :return: dict mapping display width to sorted list of unique graphemes.
    """
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
    """
    Wrapper around term.get_location() that handles false timeouts.

    Blessed may use time.time() internally which is affected by VM clock skew,
    causing false timeouts. This wrapper uses time.monotonic() to validate the
    actual elapsed time and retries if a suspiciously fast timeout occurs.

    :param term: blessed.Terminal instance
    :param timeout: Timeout in seconds
    :param max_retries: Maximum number of retries for false timeouts
    :return: Tuple of (ypos, xpos)
    """
    for attempt in range(max_retries):
        start = time.monotonic()
        ypos, xpos = term.get_location(timeout=timeout)
        elapsed = time.monotonic() - start

        # Success case
        if (ypos, xpos) != (-1, -1):
            return (ypos, xpos)

        # Check if this was a false timeout (returned too quickly)
        # Allow 10% tolerance for processing time
        if elapsed < (timeout * 0.1):
            # Suspiciously fast timeout, likely a false timeout due to clock skew
            # Retry with a slightly longer timeout (I'm using vm's on laptop sometimes)
            timeout = timeout * 1.5
            continue

        # Real timeout - actual time elapsed
        return (-1, -1)

    # All retries exhausted
    return (-1, -1)


def measure_width(term, writer, text, timeout):
    """
    Measure actual rendered width of text using cursor position reports.

    :param term: blessed.Terminal instance.
    :param writer: Output writer function.
    :param text: Text string to measure.
    :param timeout: CPR timeout in seconds.
    :return: Measured width in columns, or None on timeout.
    """
    _, x1 = get_location_with_retry(term, timeout)
    if x1 == -1:
        return None
    writer(text)
    _, x2 = get_location_with_retry(term, timeout)
    if x2 == -1:
        return None
    # erase the test character
    writer(term.move_x(x1) + ' ' * (x2 - x1) + term.move_x(x1))
    return x2 - x1


def make_printf_hex(wchar):
    """
    Convert a Unicode string to printf hex escape format.

    Python's b'\x12..' representation is compatible enough with printf(1).
    """
    return repr(wchar.encode("utf8"))[2:-1]


def _make_codepoint_table(wchars_display):
    """Build a prettytable showing codepoint breakdown of a character sequence.

    :param str wchars_display: The Unicode character(s) to decompose.
    :rtype: prettytable.colortable.ColorTable
    """
    from prettytable.colortable import ColorTable, Theme
    theme = Theme(
        default_color="\x1b[36m",
        vertical_color="\x1b[35m",
        horizontal_color="\x1b[35m",
        junction_color="\x1b[35m",
    )
    table = ColorTable(theme=theme)
    table.field_names = ["#", "Codepoint", "Python", "Category", "wcwidth", "Name"]
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
    """
    Display error details and prompt user to continue or disable stopping.

    :param term: blessed.Terminal instance
    :param writer: Output writer function
    :param context_name: Test type or language name
    :param wchars_display: The character(s) that failed
    :param measured_by_terminal: Width measured by terminal
    :param measured_by_wcwidth: Width measured by wcwidth
    :return: True to continue stopping, False to disable stopping
    """
    writer(f"\n{term.bold(f'Failure in {context_name}:')}\n")

    # Codepoint breakdown table
    writer(str(_make_codepoint_table(wchars_display)) + "\n")

    # Create a tight box around the failing character(s)
    interior = wcwidth.width(wchars_display) + 2
    border = "+" + "-" * interior + "+"
    writer(f"{border}\n|{wcwidth.center(wchars_display, interior)}|\n{border}\n")

    writer(f"\nmeasured by terminal: {measured_by_terminal}\n")
    writer(f"measured by wcwidth:  {measured_by_wcwidth}\n")

    unicode_escaped = unicode_escape_string(wchars_display)
    printf_hex = make_printf_hex(wchars_display)

    writer(f"\nShell\n-----\n")
    writer(f"printf '{printf_hex}\\n'\n")

    writer(f"\nPython\n------\n")
    writer(f'python -c "print(\'{unicode_escaped}\')"\n')

    writer(f"\n{term.bold('press return for next error, or')} "
           f"{term.bold_red('n')} {term.bold('for non-stop:')}")

    key = term.inkey()
    writer("\n")

    return key.lower() != 'n'





def test_language_support(
    term,
    writer,
    timeout,
    largest_xpos,
    limit_words,
    limit_errors,
    stop_at_error=None,
    grapheme_delay_ms=0,
    **_kwargs,
):
    # This is more of a "Test zero-width support" exercise,
    # many languages include zero-width characters, at least:
    # Tamil, Tibetan, Syriac, Gujarati, Grantha, Tamil, Myanmar, Adlam,
    # Mongolian, Gurmukhi, Telugu, Tai, Thaana, Tagalog, Arabic, Kannada,
    # Tibetan, Lao, Sinhala, Javanese, Thai, Chakma, Devanagari, Malayalam,
    # Khmer, Bengali ..
    #
    # begin test, success group-by language
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)
    time_report = {}
    tested_graphemes = {}  # grapheme -> (lang_tested_by, success)
    start_time = time.monotonic()

    for lang, multiline_text in parse_udhr():
        lang_start_time = time.monotonic()
        graphemes_by_width = extract_unique_graphemes(multiline_text)
        grapheme_count = 0
        error_count = 0

        for expected_width, graphemes in graphemes_by_width.items():
            # skip graphemes already tested by a previous language
            novel = [g for g in graphemes if g not in tested_graphemes]
            inherited_ok = sum(
                1 for g in graphemes
                if g in tested_graphemes and tested_graphemes[g][1]
            )
            inherited_fail = sum(
                1 for g in graphemes
                if g in tested_graphemes and not tested_graphemes[g][1]
            )
            # credit this language with results from prior testing
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

            # row layout: | X · X · X |
            # row_width = 2 + N*(expected_width + 3) - 2 + 1
            #           = N*(expected_width + 3) + 1
            cell_inner = expected_width + 3  # "X · "
            num_columns = max(1, (term.width - 1) // cell_inner)

            n_inherited = inherited_ok + inherited_fail
            if n_inherited:
                inherited_msg = f", {n_inherited} shared"
            else:
                inherited_msg = ""
            header_text = (
                f"[ {lang} w={expected_width}"
                f" ({len(novel)} novel{inherited_msg}) ]"
            )
            text_width = wcwidth.wcswidth(header_text)
            pad_total = max(0, term.width - text_width)
            pad_left = pad_total // 2
            pad_right = pad_total - pad_left
            dashes_l = term.bold_black('-' * pad_left)
            dashes_r = term.bold_black('-' * pad_right)
            writer("\n" + dashes_l + header_text + dashes_r + "\n")

            col = 0
            for idx, grapheme in enumerate(novel):
                if limit_words and grapheme_count >= limit_words:
                    break
                if limit_errors and error_count >= limit_errors:
                    break

                grapheme_id = f"{lang}-{expected_width}-{idx:02x}"

                # row layout: | X · X · X |
                if col == 0:
                    writer(term.magenta("| "))
                else:
                    writer(term.magenta(" \u00b7 "))

                start_ypos, start_xpos = get_location_with_retry(
                    term, timeout
                )
                if (-1, -1) == (start_ypos, start_xpos):
                    exit_and_display_timeout_error(term, writer, timeout)

                writer(term.cyan(grapheme))
                if grapheme_delay_ms:
                    time.sleep(grapheme_delay_ms / 1000.0)
                end_ypos, end_xpos = get_location_with_retry(term, timeout)
                if (-1, -1) == (end_ypos, end_xpos):
                    exit_and_display_timeout_error(term, writer, timeout)

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
                col += 1

                if col >= num_columns:
                    writer(term.magenta(" |") + "\n")
                    col = 0

            # close incomplete row
            if col > 0:
                writer(term.magenta(" |") + "\n")

        # Record elapsed time for this language
        time_report[lang] = time.monotonic() - lang_start_time

    report_languages = [
        language
        for language in set(list(failure_report.keys()) + list(success_report.keys()))
        if len(failure_report[language]) or success_report[language]
    ]

    return {
        lang: {
            "n_errors": len(failure_report[lang]),
            "n_total": len(failure_report[lang]) + success_report[lang],
            "pct_success": make_success_pct(
                n_errors=len(failure_report[lang]),
                n_total=len(failure_report[lang]) + success_report[lang],
            ),
            "seconds_elapsed": time_report.get(lang, 0.0),
            "codepoints_per_second": (
                (len(failure_report[lang]) + success_report[lang])
                / time_report.get(lang, 1.0)
                if time_report.get(lang, 0.0) > 0
                else 0.0
            ),
            "failed": failure_report[lang],
        }
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
    grapheme_delay_ms=0,
    limit_pct=0,
    include_uncommon=True,
):
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)
    time_report = {}

    start_time = time.monotonic()

    if suppress_output:
        outer_ypos, outer_xpos = get_location_with_retry(term, timeout)
        if (-1, -1) == (outer_ypos, outer_xpos):
            exit_and_display_timeout_error(term, writer, timeout)

    # row layout: | X · X · X |
    cell_inner = expected_width + 3  # "X · "
    num_columns = max(1, (term.width - 1) // cell_inner)

    with terminal.maybe_grapheme_clustering_mode(term):
        for ver, wchars in table:
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
                # stride-based sampling: take 1-of-every-N evenly across
                step = max(1, round(100 / limit_pct))
                wchars_slice = wchars[::step]
            else:
                wchars_slice = wchars

            if suppress_output:
                writer(term.move_yx(outer_ypos, outer_xpos) + term.clear_eol)
            else:
                label = test_type.upper() if test_type else "test"
                pct_note = ""
                if limit_pct and 0 < limit_pct < 100 and not limit_codepoints:
                    pct_note = f", {limit_pct}% sampled"
                header = (f"{label} v={ver}"
                          f" ({len(wchars_slice)}/{n_wchars}{pct_note})")
                writer(header + "\n")

            col = 0
            end_ypos, end_xpos = 0, 0

            for wchar in wchars_slice:
                wchars_str = wchar_to_str(wchar)

                if suppress_output:
                    # single-line: write, measure, reposition
                    writer(wchars_str)
                    if grapheme_delay_ms:
                        time.sleep(grapheme_delay_ms / 1000.0)
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
                    # row layout: | X · X · X |
                    if col == 0:
                        writer(term.magenta("| "))
                    else:
                        writer(term.magenta(" \u00b7 "))

                    start_ypos, start_xpos = get_location_with_retry(
                        term, timeout
                    )
                    if (-1, -1) == (start_ypos, start_xpos):
                        exit_and_display_timeout_error(
                            term, writer, timeout)

                    writer(term.cyan(wchars_str))
                    if grapheme_delay_ms:
                        time.sleep(grapheme_delay_ms / 1000.0)
                    end_ypos, end_xpos = get_location_with_retry(
                        term, timeout
                    )
                    if (-1, -1) == (end_ypos, end_xpos):
                        exit_and_display_timeout_error(
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

                if not suppress_output:
                    col += 1
                    if col >= num_columns:
                        writer(term.magenta(" |") + "\n")
                        col = 0

            # close incomplete row
            if not suppress_output and col > 0:
                writer(term.magenta(" |") + "\n")

            # Record elapsed time for this version
            time_report[ver] = time.monotonic() - ver_start_time

    # create sorted list of versions that have any results
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
    return {
        ver: {
            "n_errors": len(failure_report[ver]),
            "n_total": len(failure_report[ver]) + success_report[ver],
            "pct_success": make_success_pct(
                n_errors=len(failure_report[ver]),
                n_total=len(failure_report[ver]) + success_report[ver],
            ),
            "seconds_elapsed": time_report.get(ver, 0.0),
            "codepoints_per_second": (
                (len(failure_report[ver]) + success_report[ver])
                / time_report.get(ver, 1.0)
                if time_report.get(ver, 0.0) > 0
                else 0.0
            ),
            "failed_codepoints": failure_report[ver],
        }
        for ver in report_versions
    }

def do_languages_test(
    term, writer, timeout, limit_words, limit_errors, stop_at_error=None,
    grapheme_delay_ms=0,
):
    return test_language_support(
        term=term,
        writer=writer,
        timeout=timeout,
        largest_xpos=max(40, term.width // 2),
        limit_words=limit_words,
        limit_errors=limit_errors,
        stop_at_error=stop_at_error,
        grapheme_delay_ms=grapheme_delay_ms,
    )

def make_success_pct(n_errors, n_total):
    # protect from divide-by-zero and convert decimal to whole percentage points
    return ((n_total - n_errors) / n_total if n_total else 0) * 100


def parse_udhr():
    path_udhr = os.path.join(os.path.dirname(__file__), 'udhr')
    for fname in sorted(os.listdir(path_udhr)):
        if not fname.lower().endswith('.txt'):
            # skip past xml file
            continue

        full_path = os.path.join(path_udhr, fname)

        # First pass: quick scan to determine if file is interesting
        with open(full_path) as fin:
            # read only up to first '-----' marker
            language = fin.readline().split('-', 1)[1].strip()
            while True:
                line = fin.readline()
                if line.startswith('---'):
                    # stop at language break
                    break
                elif not line:
                    # reached EOF without finding a marker
                    raise RuntimeError(f'No marker found in {fname!r}, expected "---"')

            # Quick scan: check if any line has complex unicode
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
                        break  # Found interesting line, stop scanning

        # Skip files where all lines have wcwidth == len (no complex unicode)
        if not is_interesting:
            continue

        # Second pass: collect the actual text for interesting files
        with open(full_path) as fin:
            # Skip header again
            fin.readline()  # language line
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
    encoded_str = codecs.encode(input_str, "unicode-escape").decode("utf-8")
    return encoded_str

