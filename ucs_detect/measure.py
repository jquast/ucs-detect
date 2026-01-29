# std
import os
import sys
import time
import codecs
import collections

# 3rd party
import wcwidth

# local
from ucs_detect import terminal


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


def make_printf_hex(wchar):
    """
    Convert a Unicode string to printf hex escape format.

    Python's b'\x12..' representation is compatible enough with printf(1).
    """
    return repr(wchar.encode("utf8"))[2:-1]


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
    # Save current cursor position
    saved_ypos, saved_xpos = get_location_with_retry(term, 1.0)

    # Move to current y position (column 0) and clear to end of screen
    if saved_ypos != -1:
        writer(term.move_yx(saved_ypos+1, 0) + term.clear_eos)

    # Display error information
    writer(term.bold(f"Failure in {context_name}:\n"))

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

    writer(f"\n{term.bold('press return for next error, or')} {term.bold_red('n')} {term.bold('for non-stop:')}")

    # Wait for user input
    key = term.inkey()

    # Check if user wants to disable stopping
    should_continue_stopping = key.lower() != 'n'

    # Check if screen scrolled by getting current position
    current_ypos, current_xpos = get_location_with_retry(term, 1.0)

    # If we're near the bottom or position seems invalid, just clear screen
    # Otherwise try to restore to saved position
    if current_ypos == -1 or current_ypos >= term.height - 2 or saved_ypos == -1:
        # Screen likely scrolled or position invalid - clear everything
        writer(term.home + term.clear)
    else:
        # Safe to restore - no scrolling occurred
        writer(term.move_yx(saved_ypos, saved_xpos) + term.clear_eos)

    return should_continue_stopping





def test_language_support(
    term,
    writer,
    timeout,
    orig_xpos,
    top,
    bottom,
    largest_xpos,
    limit_words,
    limit_errors,
    stop_at_error=None,
    grapheme_delay_ms=0,
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
    usable_width = int(term.width * 2 / 3)

    for lang, multiline_text in parse_udhr():
        lang_start_time = time.monotonic()
        # reset display area for each language
        writer(term.move_yx(top - 1, orig_xpos))
        writer(f"{lang}" + term.clear_eos)
        writer(term.move_yx(top, 0))

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

            # cell_width: | <grapheme> |·
            cell_width = 1 + 1 + expected_width + 1 + 1 + 1
            num_columns = max(1, usable_width // cell_width)

            n_inherited = inherited_ok + inherited_fail
            if n_inherited:
                inherited_msg = f", {n_inherited} shared"
            else:
                inherited_msg = ""
            header = (
                f"{lang} w={expected_width}"
                f" ({len(novel)} novel{inherited_msg})"
            )
            writer(header + "\n")

            # sync actual cursor position after header
            cur_ypos, _ = get_location_with_retry(term, timeout)
            if (-1, -1) == (cur_ypos, _):
                exit_and_display_timeout_error(
                    term, writer, timeout, orig_xpos, top
                )

            col = 0
            last_ypos = cur_ypos
            for idx, grapheme in enumerate(novel):
                if grapheme_count >= limit_words or error_count >= limit_errors:
                    break

                grapheme_id = f"{lang}-{expected_width}-{idx:02x}"

                # write opening pipe + pad space, then measure before/after grapheme
                writer(term.magenta("|") + " ")
                start_ypos, start_xpos = get_location_with_retry(
                    term, timeout
                )
                if (-1, -1) == (start_ypos, start_xpos):
                    exit_and_display_timeout_error(
                        term, writer, timeout, orig_xpos, top
                    )

                writer(term.cyan(grapheme))
                if grapheme_delay_ms:
                    time.sleep(grapheme_delay_ms / 1000.0)
                end_ypos, end_xpos = get_location_with_retry(term, timeout)
                if (-1, -1) == (end_ypos, end_xpos):
                    exit_and_display_timeout_error(
                        term, writer, timeout, orig_xpos, top
                    )

                # write right pad, closing pipe, and dot separator
                writer(" " + term.magenta("|") + "\u00b7")

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
                    writer("\n")
                    col = 0
                    last_ypos += 1
                    if last_ypos >= bottom - 2:
                        # overflow: clear display area, keep at top
                        writer(term.move_yx(top - 1, orig_xpos))
                        writer(f"{lang}" + term.clear_eos)
                        writer(term.move_yx(top, 0))
                        last_ypos = top

            # finish incomplete row with a newline
            if col > 0:
                writer("\n")

        # Record elapsed time for this language
        time_report[lang] = time.monotonic() - lang_start_time

    report_languages = [
        language
        for language in set(list(failure_report.keys()) + list(success_report.keys()))
        if len(failure_report[language]) or success_report[language]
    ]
    test_total_sum = sum(success_report.values()) + sum(
        [len(v) for v in failure_report.values()]
    )

    writer(term.move_yx(top - 1, 0) + term.clear_eos)
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


def exit_and_display_timeout_error(term, writer, timeout, orig_xpos, top):
    writer(term.move_yx(top - 1, orig_xpos) + term.clear_eos)
    writer(term.reverse_red(f"Timeout Exceeded ({timeout:.1f}s)"))
    sys.exit(1)


def test_support(
    table,
    term,
    writer,
    timeout,
    quick,
    limit_codepoints,
    limit_errors,
    expected_width,
    report_lbound,
    suppress_output=False,
    stop_at_error=None,
    test_type=None,
    grapheme_delay_ms=0,
):
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)
    time_report = {}

    start_time = time.monotonic()
    outer_ypos, outer_xpos = get_location_with_retry(term, timeout)
    if (-1, -1) == (outer_ypos, outer_xpos):
        exit_and_display_timeout_error(
            term, writer, timeout, orig_xpos=1, top=term.height
        )

    if suppress_output:
        # suppress_output path: single-line overwrite, no grid
        top = outer_ypos
        bottom = outer_ypos
    else:
        # reserve 20-line display area below status line
        writer("\n" * 20)
        if outer_ypos != term.height - 1:
            next_ypos, _ = get_location_with_retry(term, timeout)
            if (-1, -1) == (next_ypos, _):
                exit_and_display_timeout_error(
                    term, writer, timeout, orig_xpos=1, top=term.height
                )
            top = max(0, next_ypos - 19)
        else:
            top = max(0, term.height - 20)
        bottom = min(top + 20, term.height - 1)
        writer(term.move_yx(top, 0) + term.clear_eos)

    usable_width = int(term.width * 2 / 3)
    # cell_width: | <grapheme> |·
    cell_width = 1 + 1 + expected_width + 1 + 1 + 1
    num_columns = max(1, usable_width // cell_width)

    with terminal.maybe_grapheme_clustering_mode(term):
        for ver, wchars in table:
            ver_start_time = time.monotonic()
            n_wchars = len(wchars)
            wchars_slice = wchars[
                : limit_codepoints if limit_codepoints else None
            ]

            if suppress_output:
                writer(term.move_yx(outer_ypos, outer_xpos) + term.clear_eol)
            else:
                # reset display area for this version
                writer(term.move_yx(top - 1, outer_xpos))
                label = test_type.upper() if test_type else "test"
                writer(f"{label} v={ver}" + term.clear_eos)
                writer(term.move_yx(top, 0))
                header = f"{label} v={ver} ({len(wchars_slice)}/{n_wchars})"
                writer(header + "\n")
                # sync cursor after header
                cur_ypos, _ = get_location_with_retry(term, timeout)
                if (-1, -1) == (cur_ypos, _):
                    exit_and_display_timeout_error(
                        term, writer, timeout,
                        orig_xpos=outer_xpos, top=top,
                    )

            col = 0
            last_ypos = top if not suppress_output else outer_ypos
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
                        if quick:
                            break
                        term.inkey(timeout=1)
                    delta_xpos = end_xpos - outer_xpos
                    delta_ypos = end_ypos - outer_ypos
                    writer(
                        term.move_yx(outer_ypos, outer_xpos) + term.clear_eol
                    )
                else:
                    # grid display: | grapheme |·
                    writer(term.magenta("|") + " ")
                    start_ypos, start_xpos = get_location_with_retry(
                        term, timeout
                    )
                    if (-1, -1) == (start_ypos, start_xpos):
                        exit_and_display_timeout_error(
                            term, writer, timeout,
                            orig_xpos=outer_xpos, top=top,
                        )

                    writer(term.cyan(wchars_str))
                    if grapheme_delay_ms:
                        time.sleep(grapheme_delay_ms / 1000.0)
                    end_ypos, end_xpos = get_location_with_retry(
                        term, timeout
                    )
                    if (-1, -1) == (end_ypos, end_xpos):
                        exit_and_display_timeout_error(
                            term, writer, timeout,
                            orig_xpos=outer_xpos, top=top,
                        )

                    writer(" " + term.magenta("|") + "\u00b7")
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
                        writer("\n")
                        col = 0
                        last_ypos += 1
                        if last_ypos >= bottom - 2:
                            label = test_type.upper() if test_type else "test"
                            writer(term.move_yx(top - 1, outer_xpos))
                            writer(f"{label} v={ver}" + term.clear_eos)
                            writer(term.move_yx(top, 0))
                            last_ypos = top

            # finish incomplete row
            if not suppress_output and col > 0:
                writer("\n")

            if quick:
                if (
                    wchars
                    and not failure_report[ver]
                    and success_report[ver] >= report_lbound
                ):
                    break
                if (-1, -1) == (end_ypos, end_xpos):
                    break

            # Record elapsed time for this version
            time_report[ver] = time.monotonic() - ver_start_time

    if not suppress_output:
        writer(term.move_yx(top - 1, 0) + term.clear_eos)
    writer(term.move_yx(outer_ypos, outer_xpos))

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
    test_total_sum = sum(success_report.values()) + sum(
        [len(v) for v in failure_report.values()]
    )
    if not suppress_output:
        writer(
            f": {test_total_sum:n} wchars total, "
            f"{time.monotonic() - start_time:.2f}s elapsed."
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
    writer(f"\nucs-detect: testing language support: ")
    orig_ypos, orig_xpos = get_location_with_retry(term, timeout)
    if (-1, -1) == (orig_ypos, orig_xpos):
        exit_and_display_timeout_error(term, writer, timeout, orig_xpos=1, top=term.height-1)
    writer("\n" * 20)
    if orig_ypos != term.height - 1:
        next_ypos, _ = get_location_with_retry(term, timeout)
        top = max(0, next_ypos - 19)
    else:
        top = max(0, term.height - 20)
    bottom = min(top + 20, term.height - 1)
    start_time = time.monotonic()
    writer(term.move_yx(top, 0) + term.clear_eos)
    language_results = test_language_support(
        term=term,
        writer=writer,
        timeout=timeout,
        orig_xpos=orig_xpos,
        top=top,
        bottom=bottom,
        # ensure up to ~half the screen is available, for really long language "words"
        # eg. 'རྒྱལ་ཡོངས་དང་རྒྱལ་སྤྱིའི་ཉེས་འགེལ་ཁྲིམས་ཀྱི་གྲངས་སུ་ཐོ་བཀོད་འབད་དེ་མེད་པ་ཅིན་'
        largest_xpos=max(40, term.width // 2),
        limit_words=limit_words,
        limit_errors=limit_errors,
        stop_at_error=stop_at_error,
        grapheme_delay_ms=grapheme_delay_ms,
    )

    writer(term.move_yx(top, 0) + term.clear_eos)
    writer(term.move_yx(top - 1, orig_xpos))
    writer(f"{len(language_results):n} total, ")
    writer(f"{time.monotonic() - start_time:.2f}s elapsed.")
    return language_results

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

