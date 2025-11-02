#!/usr/bin/env python
# a bit of a mess, output is more important than the processing.
import re
import os
import sys
import math
import yaml
import contextlib
import unicodedata
import colorsys

# 3rd party
import wcwidth
import tabulate

GITHUB_DATA_LINK = 'https://github.com/jquast/ucs-detect/blob/master/data/{fname}'
DATA_PATH = os.path.join(os.path.dirname(__file__), "data")
RST_DEPTH = [None, "=", "-", "+", "^"]
LINK_REGEX = re.compile(r'[^a-zA-Z0-9]')


def score_to_color(score):
    # Map score to hue: 0 degrees (red) to 120 degrees (green)
    # In HSV, hue is 0-1, so 120 degrees = 120/360 = 0.333
    hue = score * 0.333
    saturation = 0.2
    value = 0.95

    # Convert HSV to RGB (returns 0-1 range)
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)

    # Convert to 0-255 range
    return (int(r * 255), int(g * 255), int(b * 255))


def make_score_css_class(score):
    if math.isnan(score):
        return 'score-na'
    return f'score-{int(score * 100)}'


def generate_score_css():
    """
    Generate CSS rules for all score classes (0-100).
    Returns a string containing CSS rules.
    """
    css_lines = [
        '/* Auto-generated score color classes */',
        '/* Common properties for all score classes */',
        '[class^="score-"], [class*=" score-"] {',
        '  display: block;',
        '  padding: 0.3em 0.5em;',
        '}',
        ''
    ]
    for score_pct in range(101):
        score = score_pct / 100.0
        r, g, b = score_to_color(score)
        class_name = make_score_css_class(score)
        css_lines.append(f'.{class_name} {{ background-color: rgb({r}, {g}, {b}); }}')
    return '\n'.join(css_lines)


def generate_score_roles():
    """
    Generate reStructuredText role definitions for all score classes.
    Returns a string containing role definitions that can be used inline.
    """
    lines = ['.. Generate custom roles for score coloring', '']
    for score_pct in range(101):
        score = score_pct / 100.0
        class_name = make_score_css_class(score)
        lines.append(f'.. role:: {class_name}')
        lines.append(f'   :class: {class_name}')
        lines.append('')
    # Add role for N/A scores
    lines.append('.. role:: score-na')
    lines.append('   :class: score-na')
    lines.append('')
    return '\n'.join(lines)


def wrap_with_score_role(text, score):
    """
    Wrap text with a reStructuredText role based on the score.

    Args:
        text: The text content to wrap (e.g., "75.0%")
        score: The score value (0.0 to 1.0) used to determine the role class

    Returns:
        Text wrapped with inline role syntax: :score-75:`75.0%`
    """
    role_name = make_score_css_class(score)
    return f':{role_name}:`{text}`'


def wrap_score_with_hyperlink(text, score, terminal_name, section_suffix):
    """
    Wrap score text with both a hyperlink and score styling using the :sref: role.

    Args:
        text: The text to display (e.g., "75.0%", "32s")
        score: The score value (0.0 to 1.0) for styling
        terminal_name: The terminal name for creating the link target
        section_suffix: The section suffix (e.g., "_wide", "_lang", "_time")

    Returns:
        Text wrapped with hyperlink and role: :sref:`75.0% <terminal_wide> 75`
    """
    score_value = int(score * 100) if not math.isnan(score) else 'na'
    link_target = make_link(terminal_name + section_suffix)
    return f':sref:`{text} <{link_target}> {score_value}`'


def print_datatable(table_str, caption=None):
    """
    Print a table with sphinx-datatable class for sortable/searchable functionality.

    Args:
        table_str: The table string (RST format from tabulate)
        caption: Optional caption for the table
    """
    if caption:
        print(f".. table:: {caption}")
    else:
        print(".. table::")
    print("   :class: sphinx-datatable")
    print()
    # Indent the table content
    for line in table_str.split('\n'):
        if line.strip():  # Only indent non-empty lines
            print(f"   {line}")
        else:
            print()
    print()


def main():
    print(f'Generating score table... ', file=sys.stderr, end='', flush=True)
    score_table, all_successful_languages = make_score_table()
    print('ok', file=sys.stderr)

    print(f'Writing docs/_static/score-colors.css ... ', file=sys.stderr, end='', flush=True)
    os.makedirs('docs/_static', exist_ok=True)
    with open('docs/_static/score-colors.css', 'w') as fout:
        fout.write(generate_score_css())
    print('ok', file=sys.stderr)

    print(f'Writing docs/results.rst ... ', file=sys.stderr, end='', flush=True)
    with open('docs/results.rst', 'w') as fout, contextlib.redirect_stdout(fout):
        display_tabulated_scores(score_table)
        display_table_definitions()
        display_common_languages(all_successful_languages)
        display_dec_modes_feature_table(score_table)
        display_results_toc()
        display_common_hyperlinks()
    print('ok', file=sys.stderr)
    for entry in score_table:
        sw_name = entry["terminal_software_name"]
        fname = f'docs/sw_results/{make_link(sw_name)}.rst'
        print(f'Writing {fname} ... ', file=sys.stderr, end='', flush=True)
        with open(fname, 'w') as fout, contextlib.redirect_stdout(fout):
            show_software_header(entry, sw_name)
            show_score_breakdown(sw_name, entry)
            show_wide_character_support(sw_name, entry)
            show_emoji_zwj_results(sw_name, entry)
            show_vs_results(sw_name, entry, '16')
            show_vs_results(sw_name, entry, '15')
            show_language_results(sw_name, entry)
            show_dec_modes_results(sw_name, entry)
            show_reproduce_command(sw_name, entry)
            show_time_elapsed_results(sw_name, entry)
            display_common_hyperlinks()
        print('ok', file=sys.stderr)


def make_unicode_codepoint(wchar):
    if ord(wchar) > 0xFFFF:
        u_str = f"U+{ord(wchar):08X}"
    else:
        u_str = f"U+{ord(wchar):04X}"
    return f"`{u_str} <https://codepoints.net/{u_str}>`_"


def display_results_toc():
    display_title("Detailed Reports", 2)
    print(".. toctree::")
    print("   :glob:")
    print()
    print("   sw_results/*")
    print()


def display_common_hyperlinks():
    print(".. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html")
    print(".. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html")
    print(".. _`ucs-detect`: https://github.com/jquast/ucs-detect")
    print(".. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html")

def make_link(text):
    return re.sub(LINK_REGEX, '', text)

def make_outbound_hyperlink(text, link_text=None):
    if link_text is None:
        link_text = text
    return f":ref:`{text} <{make_link(link_text)}>`"

def display_inbound_hyperlink(link_text):
    print(f".. _{make_link(link_text)}:")
    print()


def find_best_failure(records):
    sorted_records = sorted(records, key=lambda record: record["measured_by_wcwidth"])
    return sorted_records[len(sorted_records) // 2]


def make_printf_hex(wchar):
    # python's b'\x12..' representation is compatible enough with printf(1)
    return repr(bytes(wchar, "utf8").decode("unicode-escape").encode("utf8"))[2:-1]


def make_score_table():
    score_table = []
    #
    # Suggest generating YAML files with something like:
    #     python ucs_detect/__init__.py --save-yaml data/output.yaml --limit-codepoints=1000 --limit-words=1000 --limit-errors=100
    #
    try:
        for yaml_path in [
            os.path.join(DATA_PATH, fname)
            for fname in os.listdir(DATA_PATH)
            if fname.endswith(".yaml") and os.path.isfile(os.path.join(DATA_PATH, fname))
        ]:
            data = yaml.safe_load(open(yaml_path, "r"))

            # determine score for 'WIDE',
            version_best_wide = data["test_results"]["unicode_wide_version"]
            _score_wide = score_wide(data)

            # 'EMOJI ZWJ',
            version_best_zwj = data["test_results"]["emoji_zwj_version"]
            _score_zwj = score_zwj(data)

            # 'EMOJI VS-16',
            score_emoji_vs16 = data["test_results"]["emoji_vs16_results"]["9.0.0"]["pct_success"] / 100

            # 'EMOJI VS-15',
            # Support both new (emoji_vs15_results) and old (emoji_vs15_type_a_results) formats
            _vs15_base = data["test_results"].get("emoji_vs15_results",
                                                   data["test_results"].get("emoji_vs15_type_a_results"))
            if _vs15_base:
                score_emoji_vs15 = _vs15_base["9.0.0"]["pct_success"] / 100
            else:
                score_emoji_vs15 = float('NaN')

            # Language Support,
            score_language = score_lang(data)

            # DEC Modes Support,
            _score_dec_modes = score_dec_modes(data)

            # Elapsed time (inverse score - lower is better)
            _score_elapsed = score_elapsed_time(data)
            _elapsed_seconds = data.get("seconds_elapsed", float('NaN'))

            # Exclude elapsed time from raw average since it's in seconds, not 0-1 fraction
            scores = (score_language, score_emoji_vs16, score_emoji_vs15, _score_zwj, _score_wide, _score_dec_modes)
            valid_scores = [s for s in scores if not math.isnan(s)]
            score_table.append(
                dict(
                    terminal_software_name=data.get("software_name", data.get('software')),
                    terminal_software_version=data.get("software_version", data.get('version')),
                    os_system=data["system"],
                    score_emoji_vs16=score_emoji_vs16,
                    score_emoji_vs15=score_emoji_vs15,
                    score_dec_modes=_score_dec_modes,
                    score_elapsed=_score_elapsed,
                    elapsed_seconds=_elapsed_seconds,
                    score_final=sum(valid_scores) / len(valid_scores) if valid_scores else float('NaN'),
                    score_language=score_language,
                    score_wide=_score_wide,
                    score_zwj=_score_zwj,
                    version_best_wide=version_best_wide,
                    version_best_zwj=version_best_zwj,
                    data=data,
                    fname=os.path.basename(yaml_path),
                )
            )
    except Exception:
        print(f"Error in yaml_path={yaml_path}", file=sys.stderr)
        raise
    # after accumulating all entries, create graded scale
    result = []
    _score_keys = [key for key in score_table[0].keys() if key.startswith("score_")]
    for entry in score_table:
        for key in _score_keys:
            entry[key + "_scaled"] = scale_scores(score_table, entry, key)
        result.append(entry)
    # Sort with NaN values at the end (treat NaN as negative infinity for sorting)
    result.sort(key=lambda x: (math.isnan(x["score_final"]), -x["score_final"] if not math.isnan(x["score_final"]) else 0))

    # create unique set of all languages tested, then find languages that are
    # successful for all terminals (english, etc.) and remove them from the
    # result.
    all_languages = set()
    for entry in result:
        all_languages.update(
            [
                lang
                for lang in entry["data"]["test_results"]["language_results"]
                if entry["data"]["test_results"]["language_results"][lang]["n_errors"] == 0
            ]
        )

    all_successful_languages = set()
    for lang in all_languages:
        if all(
            lang in entry["data"]["test_results"]["language_results"] and
            entry["data"]["test_results"]["language_results"][lang]["n_errors"] == 0
            for entry in result
        ):
            all_successful_languages.add(lang)
            for entry in result:
                if lang in entry["data"]["test_results"]["language_results"]:
                    del entry["data"]["test_results"]["language_results"][lang]
    return result, all_successful_languages


def find_failed_version(entry, version_keys, results_key, best_match_version):
    """
    Find best version candidate among failure records for display
    """
    if (
        best_match_version is None
        or not entry["data"]["test_results"][results_key][best_match_version]["n_errors"]
    ):
        # find another version with errors, to show
        sorted_by_version_errors = sorted(
            [
                (wcwidth._wcversion_value(v), v)
                for v in version_keys
                if entry["data"]["test_results"][results_key][v]["n_errors"] > 0
            ],
            reverse=True,
        )
        if sorted_by_version_errors:
            return sorted_by_version_errors[0][1]
    return best_match_version


def format_score_pct(score):
    """Format a score as a percentage, handling NaN values."""
    if math.isnan(score):
        return "N/A"
    return f'{score*100:0.1f}%'


def format_score_int(score):
    """Format a score as an integer 0-100, handling NaN values."""
    if math.isnan(score):
        return "N/A"
    return f'{int(score*100)}'


def display_tabulated_scores(score_table):
    tabulated_scores = []

    for result in score_table:
        # Get the total number of changeable DEC modes for display
        dec_modes_count = 0
        mode_2027_status = "N/A"
        if not math.isnan(result["score_dec_modes"]):
            modes = result["data"]["terminal_results"]["modes"]
            dec_modes_count = sum(1 for mode_data in modes.values() if mode_data.get("changeable", False))

            # Check Mode 2027 (GRAPHEME_CLUSTERING) status
            if 2027 in modes:
                mode_2027_data = modes[2027]
                is_supported = mode_2027_data.get("supported", False)
                is_enabled = mode_2027_data.get("enabled", False)
                is_changeable = mode_2027_data.get("changeable", False)

                # Determine status and score based on support, enabled state, and changeability
                if is_supported and is_enabled:
                    mode_2027_status = "enabled"
                    mode_2027_score = 1.0
                elif is_supported and not is_enabled and is_changeable:
                    mode_2027_status = "may enable"
                    mode_2027_score = 0.5
                else:
                    mode_2027_status = "no"
                    mode_2027_score = 0.0
            else:
                mode_2027_status = "no"
                mode_2027_score = 0.0
        else:
            mode_2027_score = float('NaN')

        # Create DEC modes display text (just the number, hyperlink will be added by wrap_score_with_hyperlink)
        dec_modes_display = f"{dec_modes_count}" if not math.isnan(result["score_dec_modes"]) else "N/A"

        # Create elapsed time display text (integer seconds with 's' suffix)
        elapsed_display = f"{int(result['elapsed_seconds'])}s" if not math.isnan(result['elapsed_seconds']) else "N/A"

        # Create WIDE display text combining version and percentage (e.g., "16.0.0/86.4%")
        wide_version = result["version_best_wide"] or "na"
        wide_pct = format_score_pct(result["score_wide_scaled"])
        wide_display = f"{wide_version}/{wide_pct}"

        tabulated_scores.append(
            {
                "Terminal Software": make_outbound_hyperlink(result["terminal_software_name"]),
                "Software Version": result["terminal_software_version"],
                "OS System": result["os_system"],

                "FINAL": wrap_score_with_hyperlink(
                    format_score_int(result["score_final_scaled"]),
                    result["score_final_scaled"],
                    result["terminal_software_name"],
                    "_scores"
                ),
                "WIDE": wrap_score_with_hyperlink(
                    wide_display,
                    result["score_wide_scaled"],
                    result["terminal_software_name"],
                    "_wide"
                ),
                "LANG": wrap_score_with_hyperlink(
                    format_score_int(result["score_language_scaled"]),
                    result["score_language_scaled"],
                    result["terminal_software_name"],
                    "_lang"
                ),
                "ZWJ": wrap_score_with_hyperlink(
                    format_score_int(result["score_zwj_scaled"]),
                    result["score_zwj_scaled"],
                    result["terminal_software_name"],
                    "_zwj"
                ),
                "VS16": wrap_score_with_hyperlink(
                    format_score_int(result["score_emoji_vs16_scaled"]),
                    result["score_emoji_vs16_scaled"],
                    result["terminal_software_name"],
                    "_vs16"
                ),
                "VS15": wrap_score_with_hyperlink(
                    format_score_int(result["score_emoji_vs15_scaled"]),
                    result["score_emoji_vs15_scaled"],
                    result["terminal_software_name"],
                    "_vs15"
                ),
                "Mode 2027": wrap_score_with_hyperlink(
                    mode_2027_status,
                    mode_2027_score,
                    result["terminal_software_name"],
                    "_dec_modes"
                ) if not math.isnan(mode_2027_score) else wrap_with_score_role("N/A", 0.0),
                "DEC Modes": wrap_score_with_hyperlink(
                    dec_modes_display,
                    result["score_dec_modes_scaled"],
                    result["terminal_software_name"],
                    "_dec_modes"
                ),
                "TIME": wrap_score_with_hyperlink(
                    elapsed_display,
                    result["score_elapsed_scaled"],
                    result["terminal_software_name"],
                    "_time"
                ),
            }
        )

    display_title("Unicode Testing Results", 1)

    # Output role definitions for inline score coloring
    print(generate_score_roles())

    # Generate and print table with inline role-colored scores
    table_str = tabulate.tabulate(tabulated_scores, headers="keys", tablefmt="rst")
    print_datatable(table_str)


def display_table_definitions():
    print("Definitions:\n")
    print(
        "- *FINAL score*: The overall terminal emulator quality score, calculated as\n"
        "  the average of all feature scores (WIDE, LANG, ZWJ, VS16, VS15, and DEC Modes),\n"
        "  then scaled (normalized 0-100%) relative to all terminals tested. Higher scores\n"
        "  indicate better overall Unicode and terminal feature support. This score excludes\n"
        "  TIME performance metrics to focus purely on feature completeness."
    )
    print(
        "- *WIDE score*: Shows the Unicode version specification most closely\n"
        "  matching in compatibility (highest version with 90% match or greater),\n"
        "  followed by the scaled percentage score (determined by version release\n"
        "  level multiplied by the pct of wide codepoints supported at that version).\n"
        "  Format: version/percentage (e.g., 16.0.0/86.4%)."
    )
    print(
        "- *LANG score*: The percentage of international languages tested\n"
        "  as having support, scaled."
    )
    print(
        "- *ZWJ score*: Determined by version release level of emoji sequences\n"
        "  with Zero-Width Joiner support, multiplied by the pct of emoji\n"
        "  sequences supported at that version, scaled."
    )
    print(
        "- *VS16 score*: Determined by the number of Emoji using Variation\n"
        "  Selector-16 supported as wide characters, scaled."
    )
    print(
        "- *VS15 score*: Determined by the number of Emoji using Variation\n"
        "  Selector-15 supported as narrow characters, scaled."
    )
    print(
        "- *Mode 2027*: DEC Mode 2027 (GRAPHEME_CLUSTERING) support. Shows 'enabled'\n"
        "  if the mode is currently enabled, 'may enable' if the mode is supported but\n"
        "  not enabled and can be changed to enabled, or 'no' if not supported.\n"
        "  This mode enables grapheme clustering behavior in the terminal."
    )
    print(
        "- *DEC Modes score*: Determined by the number of DEC private modes\n"
        "  that are changeable by the terminal, scaled. The number shows\n"
        "  the total count of changeable modes, with a link to detailed results."
    )
    print(
        "- *TIME score*: Determined by test execution time in seconds, scaled\n"
        "  inversely (lower time is better). The value shows elapsed seconds\n"
        "  during the test run, with a link to detailed timing information."
    )
    print()


def scale_scores(score_table, entry, key):
    my_score = entry[key]
    if math.isnan(my_score):
        return float('NaN')
    valid_scores = [_entry[key] for _entry in score_table if not math.isnan(_entry[key])]
    if not valid_scores:
        return float('NaN')
    max_score = max(valid_scores)
    min_score = min(valid_scores)
    if max_score == min_score:
        return 1.0  # All scores are the same

    # Inverse log10 scaling for elapsed time (lower is better, log scale for color distribution)
    if key == 'score_elapsed':
        log_my_score = math.log10(my_score)
        log_min_score = math.log10(min_score)
        log_max_score = math.log10(max_score)
        return 1.0 - ((log_my_score - log_min_score) / (log_max_score - log_min_score))

    return (my_score - min_score) / (max_score - min_score)


def score_zwj(data):
    score = 0.0
    best_zwj_version = data["test_results"]["emoji_zwj_version"]
    if best_zwj_version:
        score = (
            list(data["test_results"]["emoji_zwj_results"].keys()).index(best_zwj_version) + 1
        ) / len(data["test_results"]["emoji_zwj_results"])
    score2 = 0.01
    if best_zwj_version:
        score2 = data["test_results"]["emoji_zwj_results"][best_zwj_version]["pct_success"] / 100
    return score * score2


def score_wide(data):
    score = 0.0
    best_wide_version = data["test_results"]["unicode_wide_version"]
    unicode_versions = sorted(data["test_results"]["unicode_wide_results"].keys(),
                              key=lambda x: wcwidth._wcversion_value(x))
    if best_wide_version and best_wide_version in unicode_versions:
        score = (unicode_versions.index(best_wide_version) + 1) / len(unicode_versions)
    score2 = 0.01
    if best_wide_version:
        score2 = (
            data["test_results"]["unicode_wide_results"][best_wide_version]["pct_success"] / 100
        )
    return score * score2


def score_lang(data):
    _total_langs_supported = sum(
        1
        for lang in data["test_results"]["language_results"]
        if data["test_results"]["language_results"][lang]["n_errors"] == 0
    )
    _total_langs_available = len(data["test_results"]["language_results"])
    return _total_langs_supported / _total_langs_available


def score_dec_modes(data):
    """
    Calculate score based on changeable DEC private modes.

    Returns the ratio of changeable modes to total modes tested.
    """
    if "terminal_results" not in data or "modes" not in data["terminal_results"]:
        return float('NaN')

    modes = data["terminal_results"]["modes"]
    total_modes = len(modes)
    changeable_modes = sum(
        1 for mode_data in modes.values()
        if mode_data.get("changeable", False)
    )

    if total_modes == 0:
        return float('NaN')

    return changeable_modes / total_modes


def score_elapsed_time(data):
    """
    Calculate score based on elapsed time (inverse - lower is better).

    Returns the raw seconds_elapsed value, which will be inverted during scaling.
    This is a raw score where lower values are better.
    """
    elapsed = data.get("seconds_elapsed")
    if elapsed is None or math.isnan(elapsed):
        return float('NaN')
    return elapsed



def show_wchar(wchar):
    wchar_raw = bytes(wchar, "utf8").decode("unicode-escape")
    wchar_records = [
        {
            "#": idx + 1,  # Index column for proper default sorting
            "Codepoint": make_unicode_codepoint(_wchar),
            "Python": repr(_wchar.encode("unicode-escape").decode()),
            "Category": unicodedata.category(_wchar),
            "wcwidth": wcwidth.wcwidth(_wchar),
            "Name": unicodedata.name(_wchar, "na"),
        }
        for idx, _wchar in enumerate(wchar_raw)
    ]
    table_str = tabulate.tabulate(wchar_records, headers="keys", tablefmt="rst")
    print_datatable(table_str)
    print("Total codepoints:", len(wchar_raw))
    print()


def display_common_languages(all_successful_languages):
    if all_successful_languages:
        display_title("Common Language support", 2)
        print("The following languages were successfull")
        print("with all terminals emulators tested,")
        print("and will not be reported:")
        print()
        print("\n".join(sorted(all_successful_languages)) + ".")
        print()


def display_dec_modes_feature_table(score_table):
    """
    Display a feature comparison table for DEC Private Modes.

    Shows a compact table with changeable/supported counts and a list of supported modes.
    """
    # Collect all DEC modes across all terminals
    terminal_modes = {}  # terminal_name -> {mode_num -> (supported, changeable)}
    terminal_entries = {}  # terminal_name -> entry

    for entry in score_table:
        terminal_name = entry["terminal_software_name"]

        # Skip terminals without DEC modes data
        if ("terminal_results" not in entry["data"] or
            "modes" not in entry["data"]["terminal_results"]):
            continue

        modes = entry["data"]["terminal_results"]["modes"]
        terminal_modes[terminal_name] = {}
        terminal_entries[terminal_name] = entry

        for mode_num, mode_data in modes.items():
            supported = mode_data.get("supported", False)
            changeable = mode_data.get("changeable", False)
            terminal_modes[terminal_name][mode_num] = (supported, changeable)

    if not terminal_modes:
        # No DEC modes data available
        return

    display_title("DEC Private Modes Feature Comparison", 2)
    print("This table shows DEC Private Modes support for each terminal.")
    print("Terminals are sorted by number of changeable modes (most first).")
    print()

    # Build the table data with counts and mode lists
    table_data = []
    for terminal_name in terminal_modes:
        entry = terminal_entries[terminal_name]
        modes = terminal_modes[terminal_name]

        # Count supported and changeable modes
        changeable_count = sum(1 for supported, changeable in modes.values() if changeable)
        supported_count = sum(1 for supported, changeable in modes.values() if supported)

        # Get list of supported mode numbers, sorted
        supported_modes = sorted([int(mode_num) for mode_num, (supported, changeable) in modes.items() if supported], key=int)

        # Create list of mode numbers - only link changeable modes (they have anchors)
        mode_strs = []
        for mode_num in supported_modes:
            supported, changeable = modes[mode_num]
            if changeable:
                # Changeable modes get hyperlinks
                mode_anchor = make_link(f"{terminal_name}_decmode_{mode_num}")
                mode_strs.append(f':ref:`{mode_num} <{mode_anchor}>`')
            else:
                # Non-changeable modes shown as plain text
                mode_strs.append(str(mode_num))

        # Join mode strings with commas
        supported_modes_str = ", ".join(mode_strs) if mode_strs else "None"

        row = {
            "Terminal": make_outbound_hyperlink(terminal_name, terminal_name + "_dec_modes"),
            "Changeable": str(changeable_count),
            "Supported": str(supported_count),
            "Supported Modes": supported_modes_str
        }

        table_data.append((changeable_count, row))

    # Sort by changeable count (descending)
    table_data.sort(key=lambda x: x[0], reverse=True)

    # Extract just the row dictionaries
    sorted_rows = [row for count, row in table_data]

    if sorted_rows:
        table_str = tabulate.tabulate(sorted_rows, headers="keys", tablefmt="rst")
        print_datatable(table_str)
        print("**Legend:**")
        print()
        print("- **Changeable**: Number of modes that can be enabled/disabled by the terminal")
        print("- **Supported**: Number of modes that are recognized and supported")
        print("- **Supported Modes**: List of all supported mode numbers (click to see details)")
        print()
    else:
        print("No DEC Private Modes data available for any terminal.")
        print()


def show_score_breakdown(sw_name, entry):
    display_inbound_hyperlink(entry["terminal_software_name"] + "_scores")
    display_title("Score Breakdown", 3)
    print(f"Detailed breakdown of how scores are calculated for *{sw_name}*:")
    print()

    # Create table showing raw scores, scaled scores, and how they're calculated
    def format_raw_score(score):
        return "N/A" if math.isnan(score) else f'{score*100:0.2f}%'

    score_breakdown = [
        {
            "Score Type": "WIDE",
            "Raw Score": format_raw_score(entry["score_wide"]),
            "Scaled Score": format_score_pct(entry["score_wide_scaled"]),
            "Calculation": f'(version_index / total_versions) × (pct_success / 100)',
        },
        {
            "Score Type": "ZWJ",
            "Raw Score": format_raw_score(entry["score_zwj"]),
            "Scaled Score": format_score_pct(entry["score_zwj_scaled"]),
            "Calculation": f'(version_index / total_versions) × (pct_success / 100)',
        },
        {
            "Score Type": "LANG",
            "Raw Score": format_raw_score(entry["score_language"]),
            "Scaled Score": format_score_pct(entry["score_language_scaled"]),
            "Calculation": f'languages_supported / total_languages',
        },
        {
            "Score Type": "VS16",
            "Raw Score": format_raw_score(entry["score_emoji_vs16"]),
            "Scaled Score": format_score_pct(entry["score_emoji_vs16_scaled"]),
            "Calculation": f'pct_success / 100',
        },
        {
            "Score Type": "VS15",
            "Raw Score": format_raw_score(entry["score_emoji_vs15"]),
            "Scaled Score": format_score_pct(entry["score_emoji_vs15_scaled"]),
            "Calculation": f'pct_success / 100',
        },
        {
            "Score Type": "DEC Modes",
            "Raw Score": format_raw_score(entry["score_dec_modes"]),
            "Scaled Score": format_score_pct(entry["score_dec_modes_scaled"]),
            "Calculation": f'modes_changeable / total_modes',
        },
        {
            "Score Type": "TIME",
            "Raw Score": f"{entry['elapsed_seconds']:.2f}s" if not math.isnan(entry['elapsed_seconds']) else "N/A",
            "Scaled Score": format_score_pct(entry["score_elapsed_scaled"]),
            "Calculation": f'1 - ((elapsed - min) / (max - min)) [inverse]',
        },
    ]
    table_str = tabulate.tabulate(score_breakdown, headers="keys", tablefmt="rst")
    print_datatable(table_str)
    print(f"**Final Score Calculation:**")
    print()
    print(f"- Raw Final Score: {format_raw_score(entry['score_final'])}")
    print(f"  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + DEC Modes) / 6")
    print(f"  the categorized 'average' absolute support level of this terminal")
    print(f"  Note: TIME is excluded from raw average since it measures performance, not feature support")
    print()
    print(f"- Scaled Final Score: {format_score_pct(entry['score_final_scaled'])}")
    print(f"  (normalized across all terminals tested, including TIME performance).")
    print(f"  *Scaled scores* are normalized (0-100%) relative to all terminals tested")
    print()

def show_software_header(entry, sw_name):
    display_inbound_hyperlink(entry["terminal_software_name"])
    display_title(sw_name, 2)
    print()
    print(f'Tested Software version {entry["terminal_software_version"]} on {entry["os_system"]}')
    print('Full results available at ucs-detect_ repository path')
    print(f"`data/{entry['fname']} <{GITHUB_DATA_LINK.format(fname=entry['fname'])}>`_")
    print()


def show_wide_character_support(sw_name, entry):
    display_inbound_hyperlink(entry["terminal_software_name"] + "_wide")
    display_title("Wide character support", 3)
    print(
        f"The best wide unicode table version for {sw_name} appears to be \n"
        f'**{entry["version_best_wide"]}**, this is from a summary of the following\n'
        f"results:"
    )
    print()
    print("")
    tabulated_wide_results = [
        {
            "version": repr(version),
            "n_errors": result["n_errors"],
            "n_total": result["n_total"],
            "pct_success": f'{result["pct_success"]:0.1f}%',
        }
        for version, result in sorted(entry["data"]["test_results"]["unicode_wide_results"].items(),
                                      key=lambda x: wcwidth._wcversion_value(x[0]))
    ]
    table_str = tabulate.tabulate(tabulated_wide_results, headers="keys", tablefmt="rst")
    print_datatable(table_str)

    unicode_versions = list(entry["data"]["test_results"]["unicode_wide_results"].keys())
    show_failed_version = find_failed_version(
        entry,
        version_keys=unicode_versions,
        results_key="unicode_wide_results",
        best_match_version=entry["version_best_wide"],
    )

    # conditionally show one example record failure
    if entry["data"]["test_results"]["unicode_wide_results"][show_failed_version]["n_errors"] > 0:
        fail_record = find_best_failure(
            entry["data"]["test_results"]["unicode_wide_results"][show_failed_version][
                "failed_codepoints"
            ]
        )
        show_record_failure(
            sw_name, f"of a WIDE character from Unicode Version {show_failed_version},", fail_record
        )


def show_emoji_zwj_results(sw_name, entry):
    display_inbound_hyperlink(entry["terminal_software_name"] + "_zwj")
    display_title("Emoji ZWJ support", 3)
    print(
        f"The best Emoji ZWJ table version for *{sw_name}* appears to be \n"
        f'**{entry["version_best_zwj"]}**, this is from a summary of the following\n'
        f"results:"
    )
    print()
    print("")
    tabulated_emoji_zwj_results = [
        {
            "version": repr(version),
            "n_errors": result["n_errors"],
            "n_total": result["n_total"],
            "pct_success": f'{result["pct_success"]:0.1f}%',
        }
        for version, result in sorted(entry["data"]["test_results"]["emoji_zwj_results"].items(),
                                      key=lambda x: wcwidth._wcversion_value(x[0]))
    ]
    table_str = tabulate.tabulate(tabulated_emoji_zwj_results, headers="keys", tablefmt="rst")
    print_datatable(table_str)

    emoji_zwj_versions = list(entry["data"]["test_results"]["emoji_zwj_results"].keys())
    show_failed_version = find_failed_version(
        entry,
        version_keys=emoji_zwj_versions,
        results_key="emoji_zwj_results",
        best_match_version=entry["version_best_zwj"],
    )

    # conditionally show one example record failure
    records = entry["data"]["test_results"]["emoji_zwj_results"][show_failed_version]
    if records["n_errors"] > 0:
        fail_record = find_best_failure(records["failed_codepoints"])
        whatis = f"of an Emoji ZWJ Sequence from Emoji Version {show_failed_version},"
        show_record_failure(sw_name, whatis, fail_record)


def show_vs_results(sw_name, entry, variation_str):
    display_inbound_hyperlink(entry["terminal_software_name"] + f"_vs{variation_str}")
    display_title(f"Variation Selector-{variation_str} support", 3)

    # Check if the VS results exist (e.g., VS15 might not be available for all terminals)
    vs_results_key = f"emoji_vs{variation_str}_results"
    if vs_results_key not in entry["data"]["test_results"]:
        print(f"Emoji VS-{variation_str} results for *{sw_name}* are not available.")
        print()
        return

    show_failed_version = "9.0.0"  # static table, '9.0.0' in beta PR of wcwidth,
    records = entry["data"]["test_results"][vs_results_key][show_failed_version]
    n_errors = records["n_errors"]
    n_total = records["n_total"]
    pct_success = records["pct_success"]
    print(f"Emoji VS-{variation_str} results for *{sw_name}* is {n_errors} errors")
    print(f"out of {n_total} total codepoints tested, {pct_success:0.1f}% success.")
    failed_codepoints = records["failed_codepoints"]
    if not failed_codepoints:
        print(f"All codepoint combinations with Variation Selector-{variation_str} tested were successful.")
    else:
        failure_record = failed_codepoints[len(failed_codepoints) // 2]
        description = 'NARROW Emoji made WIDE' if variation_str == '16' else 'WIDE Emoji made NARROW'
        whatis = f"of a {description} by *Variation Selector-{variation_str}*,"
        show_record_failure(sw_name, whatis, failure_record)
    print()


def display_title(text, depth):
    print(text)
    print(RST_DEPTH[depth] * len(text))
    print()

def show_language_results(sw_name, entry):
    display_inbound_hyperlink(entry["terminal_software_name"] + "_lang")
    display_title("Language Support", 3)
    languages_successful = [
        lang
        for lang in entry["data"]["test_results"]["language_results"]
        if entry["data"]["test_results"]["language_results"][lang]["n_errors"] == 0
    ]

    if len(languages_successful) > 0:
        print(f"The following {len(languages_successful)} languages were tested with 100% success:")
        print()
        print(", ".join(sorted(languages_successful)) + ".")
        print()
    else:
        print("No languages were tested with 100% success.")
        print()

    languages_failed = [
        lang
        for lang in entry["data"]["test_results"]["language_results"]
        if entry["data"]["test_results"]["language_results"][lang]["n_errors"] > 0
    ]
    languages_failed.sort(
        key=lambda lang: entry["data"]["test_results"]["language_results"][lang]["pct_success"]
    )
    tabulated_failed_language_results = [
        {
            "lang": make_outbound_hyperlink(lang, sw_name + "_lang_" + lang),
            "n_errors": entry["data"]["test_results"]["language_results"][lang]["n_errors"],
            "n_total": entry["data"]["test_results"]["language_results"][lang]["n_total"],
            "pct_success": f'{entry["data"]["test_results"]["language_results"][lang]["pct_success"]:0.1f}%',
        }
        for lang in languages_failed
    ]

    print(f"The following {len(languages_failed)} languages are not fully supported:")
    print()
    table_str = tabulate.tabulate(tabulated_failed_language_results, headers="keys", tablefmt="rst")
    print_datatable(table_str)
    for failed_lang in languages_failed:
        fail_record = entry["data"]["test_results"]["language_results"][failed_lang]["failed"][0]
        display_inbound_hyperlink(sw_name + "_lang_" + failed_lang)
        display_title(failed_lang, 4)
        show_record_failure(sw_name, f"of language *{failed_lang}*", fail_record)


def show_dec_modes_results(sw_name, entry):
    """
    Display detailed DEC private mode support results.
    """
    display_inbound_hyperlink(entry["terminal_software_name"] + "_dec_modes")
    display_title("DEC Private Modes Support", 3)

    if "terminal_results" not in entry["data"] or "modes" not in entry["data"]["terminal_results"]:
        print(f"This Terminal does not appear capable of reporting about any DEC Private modes.")
        print()
        return

    modes = entry["data"]["terminal_results"]["modes"]
    total_modes = len(modes)

    if total_modes == 0:
        print(f"This Terminal does not appear capable of reporting about any DEC Private modes.")
        print()
        return

    changeable_modes = sum(1 for mode_data in modes.values() if mode_data.get("changeable", False))
    supported_modes = sum(1 for mode_data in modes.values() if mode_data.get("supported", False))
    unchangeable_modes = total_modes - changeable_modes

    print(f"DEC private modes results for *{sw_name}*: {changeable_modes} changeable modes")
    print(f"of {supported_modes} supported out of {total_modes} total modes tested "
          f"({(supported_modes/total_modes*100):0.1f}% support, "
          f"{(changeable_modes/total_modes*100):0.1f}% changeable).")
    print()

    # Check if terminal reports supporting all modes tested (likely an error)
    if supported_modes == total_modes and total_modes == 159:
        print(".. warning::")
        print()
        print(f"   This terminal reports to support all {total_modes} modes tested, but this")
        print(f"   is probably an error.")
        print()

    # Create detailed table of all modes with reference anchors
    print("Complete list of DEC private modes tested:")
    print()

    # We need to manually create the table with anchors for each changeable mode
    # First, create the table data
    tabulated_modes = []
    for mode_num in sorted(modes.keys(), key=int):
        mode_data = modes[mode_num]

        # Add anchor for changeable modes
        if mode_data.get("changeable", False):
            mode_anchor = make_link(f"{sw_name}_decmode_{mode_num}")
            display_inbound_hyperlink(mode_anchor)

        tabulated_modes.append({
            "Mode": mode_num,  # Just the number for proper numeric sorting
            "Name": mode_data.get("mode_name", "N/A"),
            "Description": mode_data.get("mode_description", "N/A"),
            "Supported": "Yes" if mode_data.get("supported", False) else "No",
            "Changeable": "Yes" if mode_data.get("changeable", False) else "No",
            "Enabled": "Yes" if mode_data.get("enabled", False) else "No",
        })

    table_str = tabulate.tabulate(tabulated_modes, headers="keys", tablefmt="rst")
    print_datatable(table_str)

    # Show summary of changeable vs unchangeable modes
    print(f"**Summary**: {changeable_modes} changeable, {unchangeable_modes} not changeable.")
    print()


def show_reproduce_command(sw_name, entry):
    """
    Display command to reproduce the test results.
    """
    display_inbound_hyperlink(entry["terminal_software_name"] + "_reproduce")
    display_title("Reproduction", 3)

    # Get session arguments to reconstruct the command
    session_args = entry["data"].get("session_arguments", {})
    fname = entry["fname"]

    print(f"To reproduce these results for *{sw_name}*, install and run ucs-detect_")
    print(f"with the following commands::")
    print()
    print(f"    pip install ucs-detect")

    # Build the command with available parameters
    cmd_parts = [f"ucs-detect --save-yaml={fname}"]

    # Add limit parameters if they exist
    if "limit_codepoints" in session_args:
        cmd_parts.append(f"--limit-codepoints={session_args['limit_codepoints']}")
    if "limit_words" in session_args:
        cmd_parts.append(f"--limit-words={session_args['limit_words']}")
    if "limit_errors" in session_args:
        cmd_parts.append(f"--limit-errors={session_args['limit_errors']}")
    if session_args.get("quick"):
        cmd_parts.append("--quick")

    # Join command parts with line continuation for readability
    if len(cmd_parts) > 1:
        print(f"    {cmd_parts[0]} \\")
        for part in cmd_parts[1:-1]:
            print(f"        {part} \\")
        print(f"        {cmd_parts[-1]}")
    else:
        print(f"    {cmd_parts[0]}")

    print()


def show_time_elapsed_results(sw_name, entry):
    """
    Display test execution time results.
    """
    display_inbound_hyperlink(entry["terminal_software_name"] + "_time")
    display_title("Test Execution Time", 3)

    if math.isnan(entry["elapsed_seconds"]):
        print(f"Test execution time for *{sw_name}* is not available.")
        print()
        return

    elapsed = entry["elapsed_seconds"]
    print(f"The test suite completed in **{elapsed:.2f} seconds** ({int(elapsed)}s).")
    print()
    print(f"This time measurement represents the total duration of the test execution,")
    print(f"including all Unicode wide character tests, emoji ZWJ sequences, variation")
    print(f"selectors, language support checks, and DEC mode detection.")
    print()

def show_record_failure(sw_name, whatis, fail_record):
    num_bars = "1234567890" * ((fail_record["measured_by_wcwidth"] // 10) + 1)
    ruler = num_bars[: fail_record["measured_by_wcwidth"]]
    wchars = fail_record.get("wchar", fail_record.get("wchars"))
    assert wchars
    as_printf_hex = make_printf_hex(wchars)
    print(f"Sequence {whatis} from midpoint of alignment failure records:")
    print()
    show_wchar(wchars)
    print()
    print(f"- Shell test using `printf(1)`_, ``'|'`` should align in output::")
    print()
    print(rf'        $ printf "{as_printf_hex}|\\n{ruler}|\\n"')
    print(f'        {bytes(wchars, "utf8").decode("unicode-escape")}|')
    print(f"        {ruler}|")
    print()
    if fail_record.get("delta_ypos", 0) != 0:
        print(f"- Cursor Y-Position moved {fail_record['delta_ypos']} rows"
              " where no movement is expected.")
    elif fail_record["measured_by_wcwidth"] != fail_record["measured_by_terminal"]:
        print(f"- python `wcwidth.wcswidth()`_ measures width"
              f" {fail_record['measured_by_wcwidth']},")
        print(f"  while *{sw_name}* measures width"
              f" {fail_record['measured_by_terminal']}.")
    print()


if __name__ == "__main__":
    main()
