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

# Try to use faster C-based YAML loader
try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader

# 3rd party
import wcwidth
import tabulate

# Plotting support
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for ReadTheDocs
import matplotlib.pyplot as plt
import numpy as np

GITHUB_DATA_LINK = 'https://github.com/jquast/ucs-detect/blob/master/data/{fname}'
DATA_PATH = os.path.join(os.path.dirname(__file__), "data")
TERMINAL_DETAIL_MIXINS_PATH = os.path.join(DATA_PATH, "terminal_detail_mixins.yaml")
PLOTS_PATH = os.path.join(os.path.dirname(__file__), "docs", "_static", "plots")
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
    return f'score-{round(score * 100)}'


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
    score_value = round(score * 100) if not math.isnan(score) else 'na'
    link_target = make_link(terminal_name + section_suffix)
    return f':sref:`{text} <{link_target}> {score_value}`'


def wrap_time_with_hyperlink(text, score, elapsed_seconds, terminal_name, section_suffix):
    """
    Wrap elapsed time text with hyperlink and score styling, using actual seconds for sorting.
    """
    score_value_for_color = round(score * 100) if not math.isnan(score) else 'na'
    sort_value = int(elapsed_seconds) if not math.isnan(elapsed_seconds) else 'na'
    link_target = make_link(terminal_name + section_suffix)
    # Use score for color (inverted - faster is better), but elapsed_seconds for sorting
    return f':sref:`{text} <{link_target}> {score_value_for_color}:{sort_value}`'


def load_terminal_detail_mixins():
    """
    Load terminal detail mixins from YAML file.
    Returns a dictionary keyed by lowercase software_name.
    """
    if not os.path.exists(TERMINAL_DETAIL_MIXINS_PATH):
        return {}

    with open(TERMINAL_DETAIL_MIXINS_PATH, 'r') as f:
        data = yaml.load(f, Loader=SafeLoader)

    # Normalize keys to lowercase for case-insensitive matching
    terminals = data.get('terminals', {})
    return {key.lower(): value for key, value in terminals.items()}


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


def create_score_plots(sw_name, entry, score_table):
    """
    Create matplotlib plot comparing terminal scores against all terminals.

    Parameters
    ----------
    sw_name : str
        Terminal software name
    entry : dict
        Score entry for this terminal
    score_table : list
        List of all score entries for comparison
    """
    # Collect all scores for comparison
    metrics = ['WIDE', 'ZWJ', 'LANG', 'VS16', 'VS15', 'Sixel', 'DEC', 'TIME']
    terminal_scores_scaled = {}
    all_scores_scaled = {}

    # Map metric names to entry keys
    score_keys = {
        'WIDE': 'score_wide',
        'ZWJ': 'score_zwj',
        'LANG': 'score_language',
        'VS16': 'score_emoji_vs16',
        'VS15': 'score_emoji_vs15',
        'Sixel': 'score_sixel',
        'DEC': 'score_dec_modes',
        'TIME': 'score_elapsed',
    }

    for metric in metrics:
        key = score_keys[metric]
        terminal_scores_scaled[metric] = entry[key + '_scaled']
        all_scores_scaled[metric] = [e[key + '_scaled'] for e in score_table]

    # Create output directory
    os.makedirs(PLOTS_PATH, exist_ok=True)

    # Create plot for scaled scores
    plot_filename_scaled = f"{make_link(sw_name)}_scores_scaled.png"
    plot_path_scaled = os.path.join(PLOTS_PATH, plot_filename_scaled)
    _create_multi_metric_plot(sw_name, terminal_scores_scaled, all_scores_scaled,
                              plot_path_scaled, use_scaled=True)

    return plot_filename_scaled


def _create_multi_metric_plot(terminal_name, scores_dict, all_scores_dict,
                               output_path, use_scaled=False):
    """
    Create a bar chart showing multiple metrics at once.

    Parameters
    ----------
    terminal_name : str
        Name of the terminal
    scores_dict : dict
        Dictionary of {metric_name: score_value}
    all_scores_dict : dict
        Dictionary of {metric_name: [list of all scores]}
    output_path : str
        Path to save the plot
    use_scaled : bool
        If True, use scaled scores, otherwise raw scores
    """
    metrics = list(scores_dict.keys())
    values = []
    percentiles = []

    for metric in metrics:
        score = scores_dict[metric]
        all_scores = all_scores_dict[metric]
        valid_scores = [s for s in all_scores if not math.isnan(s)]

        if math.isnan(score):
            values.append(0)
            percentiles.append(0)
        else:
            values.append(score * 100)
            pct = sum(1 for s in valid_scores if s <= score) / len(valid_scores) * 100
            percentiles.append(pct)

    # Create bar chart (8 inches at 100dpi = 800px wide to accommodate 8 metrics)
    fig, ax = plt.subplots(figsize=(8, 4))

    x_pos = np.arange(len(metrics))
    colors = ['#FF6B6B' if p < 33 else '#4ECDC4' if p < 66 else '#95E1D3'
              for p in percentiles]

    bars = ax.bar(x_pos, values, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)

    # Add mean lines for each metric
    for i, metric in enumerate(metrics):
        all_scores = all_scores_dict[metric]
        valid = [s * 100 for s in all_scores if not math.isnan(s)]
        if valid:
            mean_val = np.mean(valid)
            ax.hlines(mean_val, i - 0.4, i + 0.4, colors='red',
                     linestyles='dashed', linewidth=2, label='Mean' if i == 0 else '')

    ylabel = 'Final Scaled Score' if use_scaled else 'RAW Score'
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(f'{terminal_name} - {"Scaled" if use_scaled else "Raw"} Scores vs All Terminals',
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(metrics, rotation=0, ha='center')
    ax.set_ylim(0, 110)
    ax.grid(True, alpha=0.3, axis='y')
    ax.legend()

    plt.tight_layout()
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.close()


def main():
    print(f'Generating score table... ', file=sys.stderr, end='', flush=True)
    score_table, all_successful_languages = make_score_table()
    print('ok', file=sys.stderr)

    print(f'Loading terminal detail mixins... ', file=sys.stderr, end='', flush=True)
    terminal_mixins = load_terminal_detail_mixins()
    print('ok', file=sys.stderr)

    print(f'Writing docs/_static/score-colors.css ... ', file=sys.stderr, end='', flush=True)
    os.makedirs('docs/_static', exist_ok=True)
    with open('docs/_static/score-colors.css', 'w') as fout:
        fout.write(generate_score_css())
    print('ok', file=sys.stderr)

    print(f'Writing docs/results.rst ... ', file=sys.stderr, end='', flush=True)
    with open('docs/results.rst', 'w') as fout, contextlib.redirect_stdout(fout):
        display_tabulated_scores(score_table)
        # Definitions removed - not shown in individual terminal pages
        display_common_languages(all_successful_languages)
        display_dec_modes_feature_table(score_table)
        display_results_toc(score_table)
        display_common_hyperlinks()
    print('ok', file=sys.stderr)
    for entry in score_table:
        sw_name = entry["terminal_software_name"]

        # Generate score comparison plot
        print(f'Generating plots for {sw_name} ... ', file=sys.stderr, end='', flush=True)
        plot_scaled = create_score_plots(sw_name, entry, score_table)
        print('ok', file=sys.stderr)

        # Write terminal documentation page
        fname = f'docs/sw_results/{make_link(sw_name)}.rst'
        print(f'Writing {fname} ... ', file=sys.stderr, end='', flush=True)
        with open(fname, 'w') as fout, contextlib.redirect_stdout(fout):
            show_software_header(entry, sw_name, terminal_mixins)
            show_score_breakdown(sw_name, entry, plot_scaled)
            show_wide_character_support(sw_name, entry)
            show_emoji_zwj_results(sw_name, entry)
            show_vs_results(sw_name, entry, '16')
            show_vs_results(sw_name, entry, '15')
            show_sixel_results(sw_name, entry)
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


def display_results_toc(score_table):
    display_title("Full Report by Terminal", 2)
    print(".. toctree::")
    print("   :maxdepth: 1")
    print()
    for entry in score_table:
        sw_name = make_link(entry["terminal_software_name"])
        print(f"   sw_results/{sw_name}")
    print()


def display_common_hyperlinks():
    print(".. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html")
    print(".. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html")
    print(".. _`ucs-detect`: https://github.com/jquast/ucs-detect")
    print(".. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html")

def make_link(text):
    return re.sub(LINK_REGEX, '', text).lower()

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
            and fname != 'terminal_detail_mixins.yaml'
        ]:
            data = yaml.load(open(yaml_path, "r"), Loader=SafeLoader)

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

            # Sixel support - binary score based on DA1 device attributes response
            _sixel_support = data.get("terminal_results", {}).get("sixel", False)
            _score_sixel = 1.0 if _sixel_support else 0.0

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
                    score_language=score_language,
                    score_wide=_score_wide,
                    score_zwj=_score_zwj,
                    score_sixel=_score_sixel,
                    version_best_wide=version_best_wide,
                    version_best_zwj=version_best_zwj,
                    sixel_support=_sixel_support,
                    data=data,
                    fname=os.path.basename(yaml_path),
                )
            )
    except Exception:
        print(f"Error in yaml_path={yaml_path}", file=sys.stderr)
        raise

    # Normalize DEC modes and elapsed time scores to 0-1 range
    # Get valid dec_modes scores
    valid_dec_modes = [e["score_dec_modes"] for e in score_table if not math.isnan(e["score_dec_modes"])]
    max_dec_modes = max(valid_dec_modes) if valid_dec_modes else 1.0
    min_dec_modes = min(valid_dec_modes) if valid_dec_modes else 0.0

    # Get valid elapsed scores
    valid_elapsed = [e["score_elapsed"] for e in score_table if not math.isnan(e["score_elapsed"])]
    max_elapsed = max(valid_elapsed) if valid_elapsed else 1.0
    min_elapsed = min(valid_elapsed) if valid_elapsed else 0.0

    # Normalize and calculate final scores
    for entry in score_table:
        # Normalize DEC modes to 0-1
        if not math.isnan(entry["score_dec_modes"]):
            if max_dec_modes == min_dec_modes:
                entry["score_dec_modes_norm"] = 1.0
            else:
                entry["score_dec_modes_norm"] = (
                    (entry["score_dec_modes"] - min_dec_modes) / (max_dec_modes - min_dec_modes)
                )
        else:
            entry["score_dec_modes_norm"] = float('NaN')

        # Normalize elapsed time to 0-1 (inverse - lower is better)
        if not math.isnan(entry["score_elapsed"]):
            if max_elapsed == min_elapsed:
                entry["score_elapsed_norm"] = 1.0
            else:
                # Use log scale for time (inverse)
                log_elapsed = math.log10(entry["score_elapsed"])
                log_min = math.log10(min_elapsed)
                log_max = math.log10(max_elapsed)
                entry["score_elapsed_norm"] = 1.0 - ((log_elapsed - log_min) / (log_max - log_min))
        else:
            entry["score_elapsed_norm"] = float('NaN')

        # Calculate final score using normalized values
        scores = (
            entry["score_language"],
            entry["score_emoji_vs16"],
            entry["score_emoji_vs15"],
            entry["score_zwj"],
            entry["score_wide"],
            entry["score_sixel"],
            entry["score_dec_modes_norm"],
            entry["score_elapsed_norm"]
        )
        valid_scores = [s for s in scores if not math.isnan(s)]
        entry["score_final"] = sum(valid_scores) / len(valid_scores) if valid_scores else float('NaN')

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
    return f'{round(score*100)}'


def display_tabulated_scores(score_table):
    display_title("Results", 1)

    # Introduction and disclaimer
    print("This is a volunteer-maintained analysis created by and for terminal emulator developers.")
    print("We welcome productive contributions and corrections to improve the accuracy and")
    print("completeness of these measurements.")
    print()
    print(".. note::")
    print()
    print("   These test results are provided as-is and we do not guarantee their correctness.")
    print("   The scores and ratings presented here are objective measurements of Unicode and")
    print("   terminal feature support, and should not be interpreted as an overall assessment")
    print("   of terminal emulator quality or a recommendation. Many factors beyond Unicode")
    print("   support contribute to terminal quality.")
    print()

    display_title("General Tabulated Summary", 2)
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
                    mode_2027_score = 0.75
                else:
                    mode_2027_status = "no"
                    mode_2027_score = 0.5
            else:
                mode_2027_status = "no"
                mode_2027_score = 0.5
        else:
            mode_2027_score = float('NaN')

        # Create DEC modes display text (just the number, hyperlink will be added by wrap_score_with_hyperlink)
        dec_modes_display = f"{dec_modes_count}" if not math.isnan(result["score_dec_modes"]) else "0"

        # Create elapsed time display text (integer seconds, no suffix)
        elapsed_display = f"{int(result['elapsed_seconds'])}" if not math.isnan(result['elapsed_seconds']) else "N/A"

        # Create WIDE display text showing only version (e.g., "16" instead of "16.0.0")
        wide_version = result["version_best_wide"] or "na"
        # Remove trailing .0's from version
        if wide_version != "na":
            wide_version = wide_version.rstrip('.0')
            # Ensure we don't remove all digits after decimal if it's something like "15.1.0"
            if not '.' in wide_version:
                # If we stripped everything, it was like "16.0.0", keep just "16"
                pass
            elif wide_version.endswith('.'):
                # If it ends with '.', remove it (was like "16.0.")
                wide_version = wide_version.rstrip('.')
        wide_display = wide_version

        tabulated_scores.append(
            {
                "Terminal Software": make_outbound_hyperlink(result["terminal_software_name"]),
                "Software Version": result["terminal_software_version"],
                "OS System": result["os_system"],

                "Final Scaled Score": wrap_score_with_hyperlink(
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
                    result["score_dec_modes_scaled"] if not math.isnan(result["score_dec_modes_scaled"]) else 0.0,
                    result["terminal_software_name"],
                    "_dec_modes"
                ),
                "Sixel": wrap_with_score_role("yes", 1.0) if result.get("sixel_support", False) else wrap_with_score_role("no", 0.0),
                "Elapsed(s)": wrap_score_with_hyperlink(
                    elapsed_display,
                    result["score_elapsed_scaled"],
                    result["terminal_software_name"],
                    "_time"
                ),
            }
        )

    # Output role definitions for inline score coloring
    print(generate_score_roles())

    # Generate and print table with inline role-colored scores
    table_str = tabulate.tabulate(tabulated_scores, headers="keys", tablefmt="rst")
    print_datatable(table_str)


def display_table_definitions():
    print("Definitions:\n")
    print(
        "- *FINAL score*: The overall terminal emulator quality score, calculated as\n"
        "  the average of all feature scores (WIDE, LANG, ZWJ, VS16, VS15, DEC Modes, and TIME),\n"
        "  then scaled (normalized 0-100%) relative to all terminals tested. Higher scores\n"
        "  indicate better overall Unicode and terminal feature support. DEC Modes and TIME\n"
        "  are normalized to 0-1 range before averaging with other scores."
    )
    print(
        "- *WIDE score*: Overall percentage of wide character codepoints correctly\n"
        "  displayed across all Unicode versions tested. Calculated as the total\n"
        "  number of successful codepoints divided by total codepoints tested, scaled."
    )
    print(
        "- *LANG score*: Calculated using the geometric mean of success percentages\n"
        "  across all international languages tested. This fairly accounts for partial\n"
        "  support (e.g., 99%, 98%) without letting one low score dominate, scaled."
    )
    print(
        "- *ZWJ score*: Overall percentage of emoji ZWJ (Zero-Width Joiner) sequences\n"
        "  correctly displayed across all emoji versions tested. Calculated as the total\n"
        "  number of successful sequences divided by total sequences tested, scaled."
    )
    print(
        "- *VS16 score*: Determined by the number of Emoji using Variation\n"
        "  Selector-16 supported as wide characters."
    )
    print(
        "- *VS15 score*: Determined by the number of Emoji using Variation\n"
        "  Selector-15 supported as narrow characters."
    )
    print(
        "- *Mode 2027*: DEC Mode 2027 (GRAPHEME_CLUSTERING) support. Shows 'enabled'\n"
        "  if the mode is currently enabled, 'may enable' if the mode is supported but\n"
        "  not enabled and can be changed to enabled, or 'no' if not supported.\n"
        "  This mode enables grapheme clustering behavior in the terminal."
    )
    print(
        "- *DEC Modes*: Determined by the number of DEC private modes\n"
        "  that are changeable by the terminal, scaled."
    )
    print(
        "- *Elapsed Time*: Test execution time in seconds, scaled inversely\n"
        "  (lower time is better)."
    )
    print()


def scale_scores(score_table, entry, key):
    my_score = entry[key]
    if math.isnan(my_score):
        return float('NaN')

    # VS16, VS15, and Sixel are not scaled - return raw score (binary 0/1)
    if key in ('score_emoji_vs16', 'score_emoji_vs15', 'score_sixel'):
        return my_score

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
    """
    Calculate ZWJ score as the total percentage of successful codepoints across all versions.

    Returns the overall success rate across all ZWJ emoji sequences tested.
    """
    zwj_results = data["test_results"]["emoji_zwj_results"]
    if not zwj_results:
        return 0.0

    # Calculate total successes and total codepoints across all versions
    total_success = 0
    total_tested = 0
    for version_data in zwj_results.values():
        n_total = version_data["n_total"]
        n_errors = version_data["n_errors"]
        n_success = n_total - n_errors
        total_success += n_success
        total_tested += n_total

    if total_tested == 0:
        return 0.0

    return total_success / total_tested


def score_wide(data):
    """
    Calculate WIDE score as the total percentage of successful codepoints across all versions.

    Returns the overall success rate across all wide character codepoints tested.
    """
    wide_results = data["test_results"]["unicode_wide_results"]
    if not wide_results:
        return 0.0

    # Calculate total successes and total codepoints across all versions
    total_success = 0
    total_tested = 0
    for version_data in wide_results.values():
        n_total = version_data["n_total"]
        n_errors = version_data["n_errors"]
        n_success = n_total - n_errors
        total_success += n_success
        total_tested += n_total

    if total_tested == 0:
        return 0.0

    return total_success / total_tested


def score_lang(data):
    """
    Calculate language support score using geometric mean of all language success percentages.

    This gives a fairer score than simple counting of 100% languages, as it considers
    partial support (e.g., 99%, 98%) and doesn't let one low score dominate the result.
    """
    language_results = data["test_results"]["language_results"]
    if not language_results:
        return 0.0

    # Get success percentages for all languages (as fractions 0.0-1.0)
    percentages = [
        lang_data["pct_success"] / 100
        for lang_data in language_results.values()
    ]

    # Calculate geometric mean using log space to avoid overflow
    # geometric_mean = exp(mean(log(percentages)))
    if any(p == 0 for p in percentages):
        # If any language has 0% support, treat those as very small values
        percentages = [max(p, 0.0001) for p in percentages]

    log_percentages = [math.log(p) for p in percentages]
    geometric_mean = math.exp(sum(log_percentages) / len(log_percentages))

    return geometric_mean


def score_dec_modes(data):
    """
    Calculate score based on changeable DEC private modes.

    Returns the count of changeable modes.
    """
    if "terminal_results" not in data or "modes" not in data["terminal_results"]:
        return float('NaN')

    modes = data["terminal_results"]["modes"]
    changeable_modes = sum(
        1 for mode_data in modes.values()
        if mode_data.get("changeable", False)
    )

    return changeable_modes


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

    Shows each mode as a row, with terminals as columns.
    """
    # Collect all DEC modes across all terminals
    terminal_modes = {}  # terminal_name -> {mode_num -> (supported, changeable, mode_data)}
    terminal_changeable_counts = {}  # terminal_name -> changeable_count
    all_changeable_modes = set()  # All modes that are changeable by at least one terminal
    mode_info = {}  # mode_num -> {name, description}

    for entry in score_table:
        terminal_name = entry["terminal_software_name"]

        # Skip terminals without DEC modes data
        if ("terminal_results" not in entry["data"] or
            "modes" not in entry["data"]["terminal_results"]):
            continue

        modes = entry["data"]["terminal_results"]["modes"]
        terminal_modes[terminal_name] = {}

        changeable_count = 0
        for mode_num, mode_data in modes.items():
            supported = mode_data.get("supported", False)
            changeable = mode_data.get("changeable", False)
            terminal_modes[terminal_name][mode_num] = (supported, changeable, mode_data)

            if changeable:
                all_changeable_modes.add(mode_num)
                changeable_count += 1

            # Store mode info (name and description) from any terminal that has it
            if mode_num not in mode_info:
                mode_info[mode_num] = {
                    "name": mode_data.get("mode_name", ""),
                    "description": mode_data.get("mode_description", "")
                }

        terminal_changeable_counts[terminal_name] = changeable_count

    # Filter out terminals with 0 changeable modes
    terminals_with_changeable = {
        name: count for name, count in terminal_changeable_counts.items() if count > 0
    }

    if not terminals_with_changeable:
        # No terminals with changeable modes
        return

    display_title("DEC Private Modes Support", 2)
    print("This table shows which DEC Private Modes are supported for each terminal.")
    print("Terminals are sorted by number of changeable modes (most first).")
    print("Only terminals with at least one changeable mode are shown.")
    print("Each cell shows 'yes' (green) if supported, or 'no' (red) if not supported.")
    print()

    # Sort terminals by changeable count (descending)
    sorted_terminals = sorted(terminals_with_changeable.keys(),
                             key=lambda t: terminal_changeable_counts[t],
                             reverse=True)

    # Sort all changeable modes by mode number
    sorted_modes = sorted(all_changeable_modes, key=int)

    # Build the table data (modes as rows, terminals as columns)
    table_data = []
    for mode_num in sorted_modes:
        # Get description and extract right-hand side if '/' present
        description = mode_info[mode_num]["description"]
        if '/' in description:
            # Take the right-hand side after the '/'
            description = description.split('/', 1)[1].strip()

        row = {
            "Mode": mode_num,
            "Description": description,
        }

        # Add a column for each terminal
        for terminal_name in sorted_terminals:
            if mode_num in terminal_modes[terminal_name]:
                supported, changeable, mode_data = terminal_modes[terminal_name][mode_num]
                if supported:
                    # Show green "yes" with hyperlink for supported modes
                    row[terminal_name] = f":sref:`yes <{make_link(terminal_name + '_dec_modes')}> 100`"
                else:
                    # Show red "no" without hyperlink for unsupported modes
                    row[terminal_name] = wrap_with_score_role("no", 0.0)
            else:
                # Mode not in this terminal's data - show red "no"
                row[terminal_name] = wrap_with_score_role("no", 0.0)

        table_data.append(row)

    if table_data:
        table_str = tabulate.tabulate(table_data, headers="keys", tablefmt="rst")
        print_datatable(table_str)
    else:
        print("No changeable DEC Private Modes data available for any terminal.")
        print()


def show_score_breakdown(sw_name, entry, plot_filename_scaled):
    display_inbound_hyperlink(entry["terminal_software_name"] + "_scores")
    display_title("Score Breakdown", 3)
    print(f"Detailed breakdown of how scores are calculated for *{sw_name}*:")
    print()

    # Create table showing raw scores, scaled scores, and how they're calculated
    def format_raw_score(score):
        return "N/A" if math.isnan(score) else f'{score*100:0.2f}%'

    score_breakdown = [
        {
            "#": 1,
            "Score Type": make_outbound_hyperlink("WIDE", sw_name + "_wide"),
            "Raw Score": format_raw_score(entry["score_wide"]),
            "Final Scaled Score": format_score_pct(entry["score_wide_scaled"]),
        },
        {
            "#": 2,
            "Score Type": make_outbound_hyperlink("ZWJ", sw_name + "_zwj"),
            "Raw Score": format_raw_score(entry["score_zwj"]),
            "Final Scaled Score": format_score_pct(entry["score_zwj_scaled"]),
        },
        {
            "#": 3,
            "Score Type": make_outbound_hyperlink("LANG", sw_name + "_lang"),
            "Raw Score": format_raw_score(entry["score_language"]),
            "Final Scaled Score": format_score_pct(entry["score_language_scaled"]),
        },
        {
            "#": 4,
            "Score Type": make_outbound_hyperlink("VS16", sw_name + "_vs16"),
            "Raw Score": format_raw_score(entry["score_emoji_vs16"]),
            "Final Scaled Score": format_score_pct(entry["score_emoji_vs16_scaled"]),
        },
        {
            "#": 5,
            "Score Type": make_outbound_hyperlink("VS15", sw_name + "_vs15"),
            "Raw Score": format_raw_score(entry["score_emoji_vs15"]),
            "Final Scaled Score": format_score_pct(entry["score_emoji_vs15_scaled"]),
        },
        {
            "#": 6,
            "Score Type": make_outbound_hyperlink("Sixel", sw_name + "_sixel"),
            "Raw Score": "yes" if entry.get("sixel_support", False) else "no",
            "Final Scaled Score": format_score_pct(entry["score_sixel_scaled"]),
        },
        {
            "#": 7,
            "Score Type": make_outbound_hyperlink("DEC Modes", sw_name + "_dec_modes"),
            "Raw Score": f"{int(entry['score_dec_modes'])}" if not math.isnan(entry['score_dec_modes']) else "N/A",
            "Final Scaled Score": format_score_pct(entry["score_dec_modes_scaled"]),
        },
        {
            "#": 8,
            "Score Type": make_outbound_hyperlink("TIME", sw_name + "_time"),
            "Raw Score": f"{entry['elapsed_seconds']:.2f}s" if not math.isnan(entry['elapsed_seconds']) else "N/A",
            "Final Scaled Score": format_score_pct(entry["score_elapsed_scaled"]),
        },
    ]
    table_str = tabulate.tabulate(score_breakdown, headers="keys", tablefmt="rst")
    print_datatable(table_str)

    # Add score comparison plot
    print("**Score Comparison Plot:**")
    print()
    print("The following plot shows how this terminal's scores compare to all other terminals tested.")
    print()

    print(".. figure:: ../_static/plots/" + plot_filename_scaled)
    print("   :align: center")
    print("   :width: 800px")
    print()
    print("   Scaled scores comparison across all metrics (normalized 0-100%)")
    print()

    print(f"**Final Scaled Score Calculation:**")
    print()
    print(f"- Raw Final Score: {format_raw_score(entry['score_final'])}")
    print(f"  (average of all raw scores: WIDE + ZWJ + LANG + VS16 + VS15 + Sixel + DEC Modes + TIME) / 8")
    print(f"  the categorized 'average' absolute support level of this terminal")
    print(f"  Note: DEC Modes and TIME are normalized to 0-1 range before averaging")
    print()
    print(f"- Final Scaled Score: {format_score_pct(entry['score_final_scaled'])}")
    print(f"  (normalized across all terminals tested).")
    print(f"  *Final Scaled scores* are normalized (0-100%) relative to all terminals tested")
    print()

    # Add detailed score breakdowns for each type
    print(f"**WIDE Score Details:**")
    print()
    wide_results = entry["data"]["test_results"]["unicode_wide_results"]
    if wide_results:
        # Calculate totals across all versions
        total_success = 0
        total_tested = 0
        for version_data in wide_results.values():
            n_total = version_data["n_total"]
            n_errors = version_data["n_errors"]
            total_success += (n_total - n_errors)
            total_tested += n_total

        print(f"Wide character support calculation:")
        print(f"- Total successful codepoints: {total_success}")
        print(f"- Total codepoints tested: {total_tested}")
        print(f"- Best matching Unicode version: {entry['version_best_wide']}")
        print(f"- Formula: {total_success} / {total_tested}")
        print(f"- Result: {entry['score_wide']*100:.2f}%")
    else:
        print(f"No WIDE character support detected.")
    print()

    print(f"**ZWJ Score Details:**")
    print()
    zwj_results = entry["data"]["test_results"]["emoji_zwj_results"]
    if zwj_results:
        # Calculate totals across all versions
        total_success = 0
        total_tested = 0
        for version_data in zwj_results.values():
            n_total = version_data["n_total"]
            n_errors = version_data["n_errors"]
            total_success += (n_total - n_errors)
            total_tested += n_total

        print(f"Emoji ZWJ (Zero-Width Joiner) support calculation:")
        print(f"- Total successful sequences: {total_success}")
        print(f"- Total sequences tested: {total_tested}")
        print(f"- Best matching Emoji version: {entry['version_best_zwj']}")
        print(f"- Formula: {total_success} / {total_tested}")
        print(f"- Result: {entry['score_zwj']*100:.2f}%")
    else:
        print(f"No ZWJ support detected.")
    print()

    print(f"**VS16 Score Details:**")
    print()
    if not math.isnan(entry["score_emoji_vs16"]):
        vs16_results = entry["data"]["test_results"]["emoji_vs16_results"]["9.0.0"]
        n_errors = vs16_results["n_errors"]
        n_total = vs16_results["n_total"]
        pct_success = vs16_results["pct_success"]

        print(f"Variation Selector-16 support calculation:")
        print(f"- Errors: {n_errors} of {n_total} codepoints tested")
        print(f"- Success rate: {pct_success:.1f}%")
        print(f"- Formula: {pct_success:.1f} / 100")
        print(f"- Result: {entry['score_emoji_vs16']*100:.2f}%")
    else:
        print(f"VS16 results not available.")
    print()

    print(f"**VS15 Score Details:**")
    print()
    if not math.isnan(entry["score_emoji_vs15"]):
        vs15_base = entry["data"]["test_results"].get("emoji_vs15_results",
                                                       entry["data"]["test_results"].get("emoji_vs15_type_a_results"))
        if vs15_base:
            vs15_results = vs15_base["9.0.0"]
            n_errors = vs15_results["n_errors"]
            n_total = vs15_results["n_total"]
            pct_success = vs15_results["pct_success"]

            print(f"Variation Selector-15 support calculation:")
            print(f"- Errors: {n_errors} of {n_total} codepoints tested")
            print(f"- Success rate: {pct_success:.1f}%")
            print(f"- Formula: {pct_success:.1f} / 100")
            print(f"- Result: {entry['score_emoji_vs15']*100:.2f}%")
        else:
            print(f"VS15 results not available.")
    else:
        print(f"VS15 results not available.")
    print()

    print(f"**Sixel Score Details:**")
    print()
    sixel_status = "yes" if entry.get("sixel_support", False) else "no"
    print(f"Sixel graphics support: **{sixel_status}**")
    print()
    print(f"Sixel support is determined by the terminal's response to the Device Attributes")
    print(f"(DA1) query. Terminals that include '4' in their DA1 extensions response support")
    print(f"Sixel graphics protocol.")
    print()

    print(f"**DEC Modes Score Details:**")
    print()
    if not math.isnan(entry["score_dec_modes"]):
        modes = entry["data"]["terminal_results"]["modes"]
        total_modes = len(modes)
        changeable_modes = sum(1 for mode_data in modes.values() if mode_data.get("changeable", False))

        print(f"DEC Private Modes support calculation:")
        print(f"- Changeable modes: {changeable_modes}")
        print(f"- Total modes tested: {total_modes}")
        print(f"- Raw score: {int(entry['score_dec_modes'])} modes")
        print(f"- Scaled: normalized against max changeable modes across all terminals")
    else:
        print(f"DEC Modes results not available.")
    print()

    print(f"**TIME Score Details:**")
    print()
    if not math.isnan(entry["elapsed_seconds"]):
        elapsed = entry["elapsed_seconds"]

        print(f"Test execution time:")
        print(f"- Elapsed time: {elapsed:.2f} seconds")
        print(f"- Note: This is a raw measurement; lower is better")
        print(f"- Scaled score uses inverse log10 scaling across all terminals")
        print(f"- Scaled result: {format_score_pct(entry['score_elapsed_scaled'])}")
    else:
        print(f"Time results not available.")
    print()

    print(f"**LANG Score Details (Geometric Mean):**")
    print()
    lang_results = entry["data"]["test_results"]["language_results"]
    if lang_results:
        n = len(lang_results)
        geo_mean = entry["score_language"]

        print(f"Geometric mean calculation:")
        print(f"- Formula: (p₁ × p₂ × ... × pₙ)^(1/n) where n = {n} languages")
        print(f"- About `geometric mean <https://en.wikipedia.org/wiki/Geometric_mean>`_")
        print(f"- Result: {geo_mean*100:.2f}%")
    print()

def show_software_header(entry, sw_name, terminal_mixins):
    display_inbound_hyperlink(entry["terminal_software_name"])
    display_title(sw_name, 2)
    print()
    print(f'Tested Software version {entry["terminal_software_version"]} on {entry["os_system"]}.')

    # Look up homepage URL from terminal_mixins (case-insensitive)
    sw_name_lower = entry["terminal_software_name"].lower()
    if sw_name_lower in terminal_mixins:
        homepage = terminal_mixins[sw_name_lower].get('homepage')
        if homepage:
            print(f'The homepage URL of this terminal is {homepage}.')

    print('Full results available at ucs-detect_ repository path')
    print(f"`data/{entry['fname']} <{GITHUB_DATA_LINK.format(fname=entry['fname'])}>`_.")
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


def show_sixel_results(sw_name, entry):
    """
    Display Sixel graphics support results.
    """
    display_inbound_hyperlink(entry["terminal_software_name"] + "_sixel")
    display_title("Sixel Graphics Support", 3)

    sixel_supported = entry.get("sixel_support", False)

    if sixel_supported:
        print(f"*{sw_name}* **supports Sixel graphics protocol**.")
    else:
        print(f"*{sw_name}* **does not support Sixel graphics protocol**.")
    print()

    print(f"Sixel support is determined by the terminal's response to the Device Attributes")
    print(f"(DA1) query. Terminals that include '4' in their DA1 extensions response indicate")
    print(f"support for the Sixel graphics protocol, which allows inline image rendering.")
    print()

    # Show DA1 response if available
    if "terminal_results" in entry["data"] and "device_attributes" in entry["data"]["terminal_results"]:
        da1_data = entry["data"]["terminal_results"]["device_attributes"]
        extensions = da1_data.get("extensions", [])

        print(f"**Device Attributes Response:**")
        print()
        print(f"- Extensions reported: {', '.join(map(str, extensions)) if extensions else 'none'}")
        print(f"- Sixel indicator ('4'): {'present' if '4' in str(extensions) or 4 in extensions else 'not present'}")
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

    # Count modes that are supported but neither enabled nor changeable
    supported_but_inactive = sum(
        1 for mode_data in modes.values()
        if mode_data.get("supported", False)
        and not mode_data.get("enabled", False)
        and not mode_data.get("changeable", False)
    )

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

    # Check if many modes are supported but not enabled or changeable
    if supported_but_inactive > 50:
        print(".. note::")
        print()
        print(f"   This terminal reports {supported_but_inactive} modes as supported, but these modes")
        print(f"   are neither enabled nor changeable. This may sometimes be interpreted as")
        print(f"   not truly supporting these modes, as they cannot be toggled or utilized.")
        print()

    # Create detailed table of all modes with reference anchors
    print("Complete list of DEC private modes tested:")
    print()

    # Create the table data
    tabulated_modes = []
    for mode_num in sorted(modes.keys(), key=int):
        mode_data = modes[mode_num]

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
