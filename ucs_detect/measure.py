# std
import os
import re
import sys
import time
import codecs
import collections

# 3rd party
import wcwidth

# to accommodate varying screen sizes, we measure by each word,
# but some languages do not use ASCII space, we make some
# effort to use any their word boundaries.
WORD_SPLIT_DELIMITERS = (" ", "，", "、", ",", "\u200b", "。", "\uA9C0")



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
    for lang, multiline_text in parse_udhr(unicode_version=unicode_version):
        writer(term.move_yx(top - 1, orig_xpos))
        writer(f"{lang}" + term.clear_eos)
        writer(term.move_yx(top, 0))
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
                assert expected_width != -1, (wchars, lang, unicode_version)
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
                    exit_and_display_timeout_error(term, writer, timeout, orig_xpos, top)

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
                if end_ypos >= bottom - 2:
                    last_ypos = top
                    writer(term.move_yx(top - 1, orig_xpos))
                    writer(f"{lang}" + term.clear_eos)
                    writer(term.move_yx(top, 0))

    report_languages = [
        language
        for language in set(list(failure_report.keys()) + list(success_report.keys()))
        if len(failure_report[language]) or success_report[language]
    ]
    test_total_sum = sum(success_report.values()) + sum(
        [len(v) for v in failure_report.values()]
    )

    writer(term.move_yx(top - 1, 0) + term.clear_eos)
    writer(f"ucs-detect Languages testing completed {test_total_sum:n} wchars in total, ")
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
    largest_xpos,
    report_lbound,
    shell,
):
    # begin test by version, newest to old
    success_report = collections.defaultdict(int)
    failure_report = collections.defaultdict(list)

    start_time = time.monotonic()
    outer_ypos, outer_xpos = term.get_location(timeout=timeout)
    if (-1, -1) == (outer_xpos, outer_xpos):
        exit_and_display_timeout_error(term, writer, timeout, orig_xpos=1, top=term.height)

    for ver, wchars in table:
        maybe_str = f", version={ver}: " if not shell else ""
        writer(term.move_yx(outer_ypos, outer_xpos) + maybe_str + term.clear_eol)
        orig_start_ypos, orig_start_xpos = term.get_location(timeout=timeout)
        if (-1, -1) == (orig_start_ypos, orig_start_xpos):
                exit_and_display_timeout_error(term, writer, timeout, orig_xpos=outer_xpos, top=term.height)

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

def do_languages_test(
    term, writer, timeout, unicode_version, limit_words, limit_errors
):
    writer(f"\nucs-detect: testing language support: ")
    orig_ypos, orig_xpos = term.get_location(timeout=timeout)
    if (-1, -1) == (orig_ypos, orig_xpos):
        exit_and_display_timeout_error(term, writer, timeout, orig_xpos=1, top=term.height-1)
    writer("\n" * 20)
    if orig_ypos != term.height - 1:
        next_ypos, _ = term.get_location(timeout=timeout)
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
        unicode_version=unicode_version,
        largest_xpos=15,
        limit_words=limit_words,
        limit_errors=limit_errors,
    )

    writer(term.move_yx(top, 0) + term.clear_eos)
    writer(term.move_yx(top - 1, orig_xpos))
    writer(f"{len(language_results):n} total, ")
    writer(f"{time.monotonic() - start_time:.2f}s elapsed.")
    return language_results

def make_success_pct(n_errors, n_total):
    # protect from divide-by-zero and convert decimal to whole percentage points
    return ((n_total - n_errors) / n_total if n_total else 0) * 100

def parse_udhr(unicode_version="auto"):
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
                    wcs_width = wcwidth.wcswidth(stripped, unicode_version=unicode_version)
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

