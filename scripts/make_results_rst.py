#!/usr/bin/env python
"""Generate reStructuredText documentation pages for ucs-detect terminal test results.

Reads YAML test result files from ``data/``, computes scores, and produces
``docs/results.rst``, per-terminal ``docs/sw_results/<terminal>.rst`` pages,
CSS, and matplotlib plots.
"""

from __future__ import annotations

import re
import os
import sys
import math
from pathlib import Path
import contextlib
import unicodedata
import colorsys

import yaml

# Try to use faster C-based YAML loader
try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader

# 3rd party
import blessed
import wcwidth
import tabulate

_DPM = blessed.Terminal.DecPrivateMode


def _fmt_mode(mode_num):
    """Format a DEC private mode as ``'description (number)'``."""
    return f"{_DPM(mode_num).long_description} ({mode_num})"


# Plotting support
import matplotlib  # pylint: disable=wrong-import-position
matplotlib.use('Agg')  # Non-interactive backend for ReadTheDocs
import matplotlib.pyplot as plt  # pylint: disable=wrong-import-position
import numpy as np  # pylint: disable=wrong-import-position
from PIL import Image  # pylint: disable=wrong-import-position

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from ucs_detect.accessories import find_best_failure, safe_name, decode_wchars, load_mixins
from ucs_detect.measure import UNCOMMON_WIDE_RANGES, make_printf_hex
from ucs_detect.table_tofu import TOFU_CODEPOINTS
from ucs_detect.table_lang_contested import LANG_CONTESTED
from ucs_detect.table_narrow_contested import NARROW_CONTESTED
from ucs_detect.table_wide_contested import WIDE_CONTESTED
from ucs_detect.profiler import (ProfileSession, generate_graphs, GRAPH_DPI,
                                 GRAPH_WIDTH_PX, GRAPH_WIDTH_ALL_PX)

#: Display width of the per-terminal score comparison plot, ``figsize=(8, 4)``.
SCORE_PLOT_WIDTH_PX = 800

GITHUB_DATA_LINK = 'https://github.com/jquast/ucs-detect/blob/master/data/{fname}'
GITHUB_EXAMPLE_BASE = 'https://github.com/jquast/ucs-detect/blob/master/docs/ucs_example_files'
EXAMPLE_FILES_DIR = os.path.join(_ROOT, 'docs', 'ucs_example_files')
DATA_PATH = os.path.join(_ROOT, "data")
PLOTS_PATH = os.path.join(_ROOT, "docs", "_static", "plots")
RST_DEPTH = [None, "=", "-", "+", "^"]
LINK_REGEX = re.compile(r'[^a-zA-Z0-9_]')
CONPTY_DA_CAVEAT_LINES = (
    "† On Windows, MSYS2_ and Cygwin_ launch native Windows programs through "
    "ConPTY (conhost.exe or OpenConsole.exe), which answers DA1 itself instead "
    "of passing it to the terminal, so the response shown is **conhost.exe's**.  "
    "See mintty's `Input/Output interaction with alien programs`_.",
)

SERVICE_CLASS_NAMES = {
    1: "VT100",
    2: "VT200",
    6: "Level 4 (no VT class)",
    18: "VT330",
    41: "VT420",
    61: "VT510",
    62: "VT520",
    63: "VT320",
    64: "VT420",
    65: "VT525",
}

DA1_EXTENSION_NAMES = {
    1: "132-column mode",
    2: "Printer port",
    3: "ReGIS graphics",
    4: "Sixel graphics",
    6: "Selective erase",
    7: "Soft character sets (DRCS)",
    8: "User-defined keys (UDK)",
    9: "National replacement charsets",
    12: "Yugoslavian, Serbian/Croatian (SCS)",
    14: "Advanced video option",
    15: "Technical character set",
    17: "Terminal state reports (16-bit)",
    18: "User windows",
    21: "Horizontal scrolling",
    22: "ANSI color",
    23: "Greek",
    24: "Turkish",
    28: "Rectangular area operations",
    29: "Text locator (mouse)",
    32: "ANSI text terminal (Level 3)",
    42: "ISO Latin-2 character set",
    52: "OSC 52 clipboard",
    314: "Pixel geometry",
}

# Mapping from test category to example file basename.
# Language failures use ucs_graphemes_{width}.txt, resolved at lookup time.
CATEGORY_FILE_MAP = {
    'wide': 'ucs_wide.txt',
    'zwj': 'ucs_zwj.txt',
    'vs16': 'ucs_vs16.txt',
    'vs16n': 'ucs_vs16.txt',
    'vs15': 'ucs_vs15.txt',
    'sri': None,
    'sfz': None,
    'ri': None,
}

# Lazily populated cache: filepath -> {hex_key: 1-based line number}
_example_index_cache = {}


def _build_example_index(filepath):
    """Parse an example file, returning ``{hex_key: 1_based_line_number}``."""
    index = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for lineno, line in enumerate(f, start=1):
            if '│' not in line:
                continue
            # left-aligned: │X│ 0x00020 Name   or   │XX│ 1F468+200D+...
            after_bar = line.split('│ ', 1)
            if len(after_bar) < 2:
                continue
            hex_word = after_bar[1].split()[0]
            # strip '0x' prefix, leading zeros, uppercase.
            if hex_word.startswith('0x'):
                hex_word = hex_word[2:]
            hex_word = hex_word.lstrip('0').upper() or '0'
            index[hex_word] = lineno
    return index


def _get_example_index(category, measured_width=None):
    """Return the ``{hex_key: line_number}`` index for *category*, building if needed.  """
    if category.startswith('lang'):
        if measured_width is None:
            return None
        basename = f'ucs_graphemes_{int(measured_width)}.txt'
    else:
        basename = CATEGORY_FILE_MAP.get(category)
        if basename is None:
            return None

    filepath = os.path.join(EXAMPLE_FILES_DIR, basename)
    if not os.path.exists(filepath):
        return None
    if filepath not in _example_index_cache:
        _example_index_cache[filepath] = _build_example_index(filepath)
    return _example_index_cache[filepath]


def _example_file_link(wchar, category, measured_width=None):
    """Return an RST hyperlink and line number for the example file at *wchar*.

    :returns: ``(basename, lineno, url)`` tuple or ``None``.
    """
    def _wchar_to_hex(wchar):
        cps = [f'{ord(c):X}' for c in wchar]
        return '+'.join(cps)
    if category.startswith('lang'):
        basename = f'ucs_graphemes_{int(measured_width)}.txt' if measured_width else None
    else:
        basename = CATEGORY_FILE_MAP.get(category)
    if basename is None:
        return None

    index = _get_example_index(category, measured_width)
    if index is None:
        return None

    hex_key = _wchar_to_hex(wchar)
    lineno = index.get(hex_key)
    if lineno is None:
        return None

    url = f'{GITHUB_EXAMPLE_BASE}/{basename}#L{lineno}'
    return basename, lineno, url


def score_to_color(score):
    """Map a normalized score (0-100) to an RGB hex color (red to green)."""
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
    """Return CSS class name for a given score value."""
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
    css_lines.append('.score-contested { background-color: rgb(220, 220, 220); }')
    css_lines.append('.score-warn { background-color: rgb(255, 255, 150); }')
    css_lines.append('.score-pass { background-color: rgb(193, 242, 193); }')
    css_lines.append('.score-fail { background-color: rgb(242, 193, 193); }')
    css_lines.append('.score-na { background-color: rgb(220, 220, 220); }')
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
    # Add role for contested scores (light grey)
    lines.append('.. role:: score-contested')
    lines.append('   :class: score-contested')
    lines.append('')
    # Add role for warn scores (yellow, COLORTERM-only detection)
    lines.append('.. role:: score-warn')
    lines.append('   :class: score-warn')
    lines.append('')
    # Add role for pass scores (green, feature present)
    lines.append('.. role:: score-pass')
    lines.append('   :class: score-pass')
    lines.append('')
    # Add role for fail scores (red, no identification method available)
    lines.append('.. role:: score-fail')
    lines.append('   :class: score-fail')
    lines.append('')
    return '\n'.join(lines)


def wrap_with_score_role(text, score):
    """Wrap text with a reStructuredText inline role based on the score."""
    role_name = make_score_css_class(score)
    return f':{role_name}:`{text}`'


def wrap_score_with_hyperlink(text, score, terminal_name, section_suffix):
    """Wrap score text with both a hyperlink and score styling using the :sref: role."""
    score_value = round(score * 100) if not math.isnan(score) else 'na'
    link_target = make_link(terminal_name + section_suffix)
    return f':sref:`{text} <{link_target}> {score_value}`'


def _wrap_colorterm_warn(text, terminal_name):
    """Wrap a capability value with warn (yellow) styling and hyperlink."""
    link_target = make_link(terminal_name + "_identification")
    return f':sref:`{text} <{link_target}> warn`'


def _wrap_id_fail(text, terminal_name):
    """Wrap a capability value with fail (red) styling and hyperlink."""
    link_target = make_link(terminal_name + "_identification")
    return f':sref:`{text} <{link_target}> fail`'


def _wrap_id_contested(text, terminal_name, section_suffix):
    """Wrap a capability value with contested (grey) styling and hyperlink."""
    link_target = make_link(terminal_name + section_suffix)
    return f':sref:`{text} <{link_target}> contested`'


def _wrap_untested(terminal_name, section_suffix):
    """Wrap untested score with grey styling and hyperlink."""
    link_target = make_link(terminal_name + section_suffix)
    return f':sref:`N/A <{link_target}> contested`'


def wrap_time_with_hyperlink(text, score, elapsed_seconds, terminal_name, section_suffix):
    """
    Wrap elapsed time text with hyperlink and score styling, using actual seconds for sorting.
    """
    score_value_for_color = round(score * 100) if not math.isnan(score) else 'na'
    sort_value = int(elapsed_seconds) if not math.isnan(elapsed_seconds) else 'na'
    link_target = make_link(terminal_name + section_suffix)
    # Use score for color (inverted - faster is better), but elapsed_seconds for sorting
    return f':sref:`{text} <{link_target}> {score_value_for_color}:{sort_value}`'


def print_datatable(table_str, caption=None):
    """Print a table with sphinx-datatable class for sortable/searchable functionality."""
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
    """Create matplotlib plot comparing terminal scores against all terminals."""
    # Collect all scores for comparison
    metrics = ['WIDE', 'NARROW', 'ZWJ', 'LANG', 'VS16', 'SRI', 'SFZ', 'RI', 'CAP', 'GFX', 'RSC']
    terminal_scores_scaled = {}
    all_scores_scaled = {}

    # Map metric names to entry keys
    score_keys = {
        'WIDE': 'score_wide',
        'NARROW': 'score_narrow',
        'ZWJ': 'score_zwj',
        'LANG': 'score_language',
        'VS16': 'score_emoji_vs16',
        'VS15': 'score_emoji_vs15',
        'SRI': 'score_sri',
        'SFZ': 'score_sfz',
        'RI': 'score_ri',
        'CAP': 'score_features',
        'GFX': 'score_graphics',
        'RSC': 'score_resource',
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


def _percentile_to_color(pct):
    """Interpolate HSV shortest path from red (0%) to green (100%)."""
    # hue 0.0 = red, hue 0.333 = green, interpolate by percentile
    h = (pct / 100.0) * (1.0 / 3.0)
    r, g, b = colorsys.hsv_to_rgb(h, 0.7, 0.9)
    return '#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255))


def _create_multi_metric_plot(terminal_name, scores_dict, all_scores_dict,
                               output_path, use_scaled=False):  # noqa: E127
    """Create a bar chart showing multiple metrics at once."""
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

    # Create bar chart (8 inches wide to accommodate 8 metrics, saved at GRAPH_DPI)
    fig, ax = plt.subplots(figsize=(8, 4))

    x_pos = np.arange(len(metrics))
    colors = [_percentile_to_color(p) for p in percentiles]

    bars = ax.bar(x_pos, values, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)  # noqa: F841

    # Add mean lines for each metric
    for i, metric in enumerate(metrics):
        all_scores = all_scores_dict[metric]
        valid = [s * 100 for s in all_scores if not math.isnan(s)]
        if valid:
            mean_val = np.mean(valid)
            ax.hlines(mean_val, i - 0.4, i + 0.4, colors='red',
                     linestyles='dashed', linewidth=2, label='Mean' if i == 0 else '')  # noqa: E128

    # Add value labels above all bars, drawn on top of mean lines
    for i, val in enumerate(values):
        y_pos = max(val, 2)
        ax.text(i, y_pos + 1, f'{val:.0f}%', ha='center', va='bottom',
                fontsize=9, fontweight='bold', color='black')

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
    plt.savefig(output_path, dpi=GRAPH_DPI, bbox_inches='tight',
                # 'None' CreationDate is used so the git hash's don't unnecessarily update
                metadata={'CreationDate': None})
    plt.close()


def create_time_summary_plot(score_table):
    """
    Create a scatterplot showing the correlation between final Score and CPR
    round-trip time (rtt_avg_ms).

    :returns: filename of the generated plot
    """
    os.makedirs(PLOTS_PATH, exist_ok=True)

    names = []
    scores = []
    timing_data = []  # [rtt_avg, rtt_mdev] per terminal

    for entry in score_table:
        if math.isnan(entry["score_final_scaled"]):
            continue
        cps = entry["data"].get("cps_summary") or {}
        # Prefer per-category "cpr" stats (excludes capability detection
        # timeouts), fall back to top-level summary for older data files
        cpr_stats = cps.get("cpr") or cps
        rtt_avg = cpr_stats.get("rtt_avg_ms")
        rtt_mdev = cpr_stats.get("rtt_mdev_ms", 0)
        rtt_min = cpr_stats.get("rtt_min_ms", rtt_avg)
        rtt_max = cpr_stats.get("rtt_max_ms", rtt_avg)
        if rtt_avg is None:
            continue
        names.append(entry["terminal_software_name"])
        scores.append(entry["score_final_scaled"] * 100)
        timing_data.append((rtt_avg, rtt_mdev, rtt_min, rtt_max))

    if not names:
        return None

    scores_arr = np.array(scores)

    # Sort ascending by score (lowest score leftmost)
    order = np.argsort(scores_arr)
    scores_arr = scores_arr[order]
    names = [names[i] for i in order]
    timing_data = [timing_data[i] for i in order]

    rtt_avg_arr = np.array([d[0] for d in timing_data])
    rtt_mdev_arr = np.array([d[1] for d in timing_data])
    _rtt_min_arr = np.array([d[2] for d in timing_data])  # noqa: F841
    _rtt_max_arr = np.array([d[3] for d in timing_data])  # noqa: F841

    fig, ax = plt.subplots(figsize=(12, max(7, len(names) * 0.3)))

    positions = np.arange(len(names))
    colors = [_percentile_to_color(s) for s in scores_arr]

    # Horizontal bars at the average, with T-capped whiskers at +/- 1 std dev
    xerr_lower = np.minimum(rtt_mdev_arr, rtt_avg_arr)  # clamp so bar doesn't go negative
    xerr_upper = rtt_mdev_arr
    ax.barh(positions, rtt_avg_arr, height=0.5, color=colors,
            edgecolor='black', linewidth=0.5, alpha=0.7, zorder=1)
    ax.errorbar(rtt_avg_arr, positions, xerr=[xerr_lower, xerr_upper],
                fmt='s', markersize=4, color='black',
                ecolor='black', elinewidth=1.5, capsize=4,
                capthick=1.5, zorder=2, label='Avg RTT (\u00b11 std dev)')

    ax.set_xscale('log')
    ax.set_yticks(positions)
    ax.set_yticklabels([
        f"{name} ({scores_arr[i]:.0f} to {_fmt_ms(rtt_avg_arr[i])})"
        for i, name in enumerate(names)
    ], fontsize=8)
    ax.set_xlabel('CPR Round-Trip Time', fontsize=12)
    ax.set_title('Final Scaled Score to Cursor Position Report Response Time',
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, which='both', axis='x')
    ax.legend(fontsize=9, loc='lower right')

    # Human-readable x-axis tick labels
    from matplotlib.ticker import FuncFormatter
    def _ms_formatter(x, _pos):  # noqa: E306
        if x >= 1000:
            return f"{x / 1000:.0f}s"
        if x >= 100:
            return f"{x:.0f}ms"
        if x >= 10:
            return f"{x:.0f}ms"
        if x >= 1:
            return f"{x:.1f}ms"
        return f"{x:.2f}ms"
    ax.xaxis.set_major_formatter(FuncFormatter(_ms_formatter))

    plt.tight_layout()
    plot_filename = "time_summary_scatter.png"
    plt.savefig(os.path.join(PLOTS_PATH, plot_filename), dpi=GRAPH_DPI,
                bbox_inches='tight', metadata={'CreationDate': None})
    plt.close()
    return plot_filename


def process_resource_data():
    """Generate resource profile graphs and compute resource_score in YAML files.

    Reads ``resource_profile`` data from all data YAML files, builds
    per-terminal CPU/RSS/time graphs, computes 0-100 resource scores
    across all terminals, and writes scores back to the data YAML files.
    """
    sessions: dict[str, ProfileSession] = {}
    yaml_map: dict[str, str] = {}  # sw_name -> yaml file path

    for fname in os.listdir(DATA_PATH):
        if not fname.endswith(".yaml") or fname.startswith("_"):
            continue
        if fname == "terminals.yaml":
            continue
        yaml_path = os.path.join(DATA_PATH, fname)
        with open(yaml_path) as f:
            data = yaml.load(f, Loader=SafeLoader) or {}
        rp = data.get("resource_profile") or {}
        elapsed = rp.get("elapsed_s", [])
        cpu = rp.get("cpu_pct", [])
        rss = rp.get("rss_mb", [])
        if not elapsed or not cpu or not rss:
            continue
        mean_cpu = sum(cpu) / len(cpu)
        mean_rss = sum(rss) / len(rss)
        if mean_cpu < 0.1 and mean_rss < 5.0:
            continue  # profiling failed, process tree was never captured
        sw_name = data.get("software_name", fname.replace(".yaml", ""))
        session = ProfileSession(sw_name, 0)
        samples = list(zip(elapsed, cpu, rss))
        while samples and samples[-1][2] <= 0.0:
            samples.pop()
        session._samples = samples
        sessions[sw_name] = session
        yaml_map[sw_name] = yaml_path

    if not sessions:
        return

    profiles_dir = os.path.join(_ROOT, "docs", "_static", "profiles")
    generate_graphs(sessions, Path(profiles_dir))


def main():
    """Generate all RST documentation pages, CSS, and plots from YAML data files."""
    print('Processing resource data... ', file=sys.stderr, end='', flush=True)
    process_resource_data()
    print('ok', file=sys.stderr)

    print('Generating score table... ', file=sys.stderr, end='', flush=True)
    score_table, all_successful_languages = make_score_table()
    print('ok', file=sys.stderr)

    print('Loading terminal detail mixins... ', file=sys.stderr, end='', flush=True)
    terminal_mixins = load_mixins()
    print('ok', file=sys.stderr)

    print('Writing docs/_static/score-colors.css ... ', file=sys.stderr, end='', flush=True)
    os.makedirs('docs/_static', exist_ok=True)
    with open('docs/_static/score-colors.css', 'w') as fout:
        fout.write(generate_score_css())
    print('ok', file=sys.stderr)

    print('Generating TIME summary plot... ', file=sys.stderr, end='', flush=True)
    _time_plot = create_time_summary_plot(score_table)  # noqa: F841
    print('ok', file=sys.stderr)

    print('Writing docs/results.rst ... ', file=sys.stderr, end='', flush=True)
    with open('docs/results.rst', 'w') as fout, contextlib.redirect_stdout(fout):
        display_tabulated_scores(score_table)
        # Definitions removed - not shown in individual terminal pages
        display_common_languages(all_successful_languages)
        display_features_table(score_table)
        display_truecolor_table(score_table)
        display_osc52_table(score_table)
        display_da1_response_section(score_table)
        display_id_table(score_table, terminal_mixins)
        display_id_summary_bullets(score_table, terminal_mixins)
        display_xtgettcap_summary_bullets(score_table)
        display_xtgettcap_comparison_table(score_table)
        display_performance_section(score_table)
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
            show_narrow_results(sw_name, entry)
            show_emoji_zwj_results(sw_name, entry)
            show_vs_results(sw_name, entry, '16')
            show_vs_results(sw_name, entry, '15')
            show_sri_results(sw_name, entry)
            show_sfz_results(sw_name, entry)
            show_ri_results(sw_name, entry)
            show_graphics_results(sw_name, entry)
            show_device_attributes(sw_name, entry)
            show_language_results(sw_name, entry)
            show_dec_modes_results(sw_name, entry)
            show_kitty_keyboard_results(sw_name, entry)
            show_xtgettcap_results(sw_name, entry)
            show_text_sizing_results(sw_name, entry)
            show_tofu_results(sw_name, entry)
            show_truecolor_results(sw_name, entry)
            show_osc52_results(sw_name, entry)
            show_id_results(sw_name, entry, terminal_mixins)
            show_reproduce_command(sw_name, entry)
            show_time_elapsed_results(sw_name, entry)
            display_common_hyperlinks()
        print('ok', file=sys.stderr)

    # Remove stale per-terminal RST files not in the current score table
    expected = {f"{make_link(e['terminal_software_name'])}.rst" for e in score_table}
    sw_dir = os.path.join(_ROOT, "docs", "sw_results")
    if os.path.isdir(sw_dir):
        for fname in os.listdir(sw_dir):
            if fname.endswith(".rst") and fname not in expected:
                stale = os.path.join(sw_dir, fname)
                print(f'Removing stale {stale} ... ', file=sys.stderr, end='', flush=True)
                os.unlink(stale)
                print('ok', file=sys.stderr)


def _fmt_ms(ms):
    """Format milliseconds with adaptive precision."""
    if ms >= 1000:
        return f"{ms / 1000:.1f}s"
    if ms >= 100:
        return f"{ms:.0f}ms"
    if ms >= 10:
        return f"{ms:.1f}ms"
    return f"{ms:.2f}ms"


def _escape_terminfo_value(value):
    """Escape non-printable control characters for display in RST tables."""
    result = []
    for ch in value:
        if ch == '\x1b':
            result.append('\\E')
        elif ch == '\x07':
            result.append('\\a')
        elif ch == '\x08':
            result.append('\\b')
        elif ch == '\n':
            result.append('\\n')
        elif ch == '\r':
            result.append('\\r')
        elif ch == '\t':
            result.append('\\t')
        elif ord(ch) < 0x20:
            result.append(f'\\x{ord(ch):02x}')
        else:
            result.append(ch)
    return ''.join(result)


def make_unicode_codepoint(wchar):
    """Render a unicode codepoint/sequence as human-readable hex notation."""
    if ord(wchar) > 0xFFFF:
        u_str = f"U+{ord(wchar):08X}"
    else:
        u_str = f"U+{ord(wchar):04X}"
    return f"`{u_str} <https://codepoints.net/{u_str}>`_"


def display_results_toc(score_table):
    """Display the table of contents linking to per-terminal detail pages."""
    display_title("Full Report by Terminal", 2)
    print(".. toctree::")
    print("   :maxdepth: 1")
    print()
    seen = set()
    for entry in score_table:
        sw_name = make_link(entry["terminal_software_name"])
        if sw_name in seen:
            continue
        seen.add(sw_name)
        print(f"   sw_results/{sw_name}")
    print()


def display_common_hyperlinks():
    """Display common hyperlink definitions used across the documentation."""
    print(".. _`printf(1)`: https://www.man7.org/linux/man-pages/man1/printf.1.html")
    print(".. _`wcwidth.wcswidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html")
    print(".. _`ucs-detect`: https://github.com/jquast/ucs-detect")
    print(".. _`ttyscan`: https://github.com/jquast/ttyscan")
    print(".. _`DEC Private Modes`: https://blessed.readthedocs.io/en/latest/dec_modes.html")
    print(".. _`OSC 52`: https://dev.to/djmitche/clipboards-terminals-and-linux-3pk5")
    print(".. _`XTGETTCAP`: https://codeberg.org/dnkl/foot#xtgettcap")
    print(".. _`Truecolor`: https://github.com/termstandard/colors/blob/master/README.md")
    print(".. _`Kitty graphics`: https://sw.kovidgoyal.net/kitty/graphics-protocol/")
    print(".. _`Font Glyph Coverage Enquiry`: "
          "https://github.com/mintty/mintty/wiki/CtrlSeqs#font-glyph-coverage-enquiry")
    print(".. _`Glyph Protocol`: "
          "https://rapha.land/introducing-glyph-protocol-for-terminals/")
    print(".. _MSYS2: https://www.msys2.org/")
    print(".. _Cygwin: https://www.cygwin.com/")


def make_link(text):
    """Strip non-alphanumeric characters from link_text for use as an anchor name."""
    return re.sub(LINK_REGEX, '', text).lower()


def make_outbound_hyperlink(text, link_text=None):
    """Create an RST :ref: role hyperlink with the given text and anchor target."""
    if link_text is None:
        link_text = text
    return f":ref:`{text} <{make_link(link_text)}>`"


def display_inbound_hyperlink(link_text):
    """Emit an RST hyperlink anchor target for cross-references."""
    print(f".. _{make_link(link_text)}:")
    print()


def resource_cost(data):
    """Compute a raw resource cost from profile data (higher = worse).
    
    Returns NaN if no valid profile data is available.
    """
    rp = (data.get("resource_profile") or {})
    elapsed = rp.get("elapsed_s", [])
    cpu = rp.get("cpu_pct", [])
    rss = rp.get("rss_mb", [])
    if not elapsed or not cpu or not rss:
        return float('NaN')
    # strip trailing zeros
    while elapsed and rss and rss[-1] <= 0.0:
        elapsed.pop()
        cpu.pop()
        rss.pop()
    if not elapsed:
        return float('NaN')
    mean_cpu = sum(cpu) / len(cpu)
    mean_rss = sum(rss) / len(rss)
    duration = elapsed[-1]
    if mean_cpu < 0.1 and mean_rss < 5.0:
        return float('NaN')
    return math.log(mean_cpu + 1) + math.log(mean_rss + 1) + math.log(duration + 1)


def make_score_table():
    """Read all YAML data files and compute normalized scores for each terminal."""
    score_table = []
    #
    # Suggest generating YAML files with something like:
    #     python ucs_detect/__init__.py --save-yaml data/output.yaml --limit-codepoints=1000 --limit-words=1000 --limit-errors=100
    #
    yaml_path = None
    for yaml_path in [
        os.path.join(DATA_PATH, fname)
        for fname in os.listdir(DATA_PATH)
        if fname.endswith(".yaml") and not fname.startswith("_")
        and fname != "terminals.yaml"
        and os.path.isfile(os.path.join(DATA_PATH, fname))
    ]:
        with open(yaml_path, "r") as f:
            data = yaml.load(f, Loader=SafeLoader)

        # determine score for 'WIDE',
        _score_wide = score_wide(data)

        # 'NARROW',
        _score_narrow = score_narrow(data)

        # 'EMOJI ZWJ',
        _score_zwj = score_zwj(data)

        # 'SRI' (Standalone Regional Indicators),
        _score_sri = score_sri(data)

        # 'SFZ' (Standalone Fitzpatrick),
        _score_sfz = score_sfz(data)

        # 'RI' (Regional Indicator Flags),
        _score_ri = score_ri(data)

        # 'EMOJI VS-16',
        _vs16_base = data["test_results"].get("emoji_vs16_results", {})
        if _vs16_base:
            score_emoji_vs16 = next(iter(_vs16_base.values()))["pct_success"] / 100
        else:
            score_emoji_vs16 = 0.0

        # 'EMOJI VS-15',
        # Support both new (emoji_vs15_results) and old (emoji_vs15_type_a_results) formats
        _vs15_base = data["test_results"].get("emoji_vs15_results",  # noqa: E127
                                               data["test_results"].get("emoji_vs15_type_a_results"))  # noqa: E127
        if _vs15_base:
            score_emoji_vs15 = next(iter(_vs15_base.values()))["pct_success"] / 100
        else:
            score_emoji_vs15 = 0.0

        # Language Support,
        score_language = score_lang(data)

        # DEC Modes Support,
        _score_dec_modes = score_dec_modes(data)

        # Resource score, negate raw cost so higher = better for scaling
        _cost = resource_cost(data)
        _score_resource = -_cost if not math.isnan(_cost) else float('NaN')
        _elapsed_seconds = data.get("seconds_elapsed", float('NaN'))

        # Sixel support, binary score based on DA1 device attributes response
        _sixel_support = data.get("terminal_results", {}).get("sixel", False)
        _score_sixel = 1.0 if _sixel_support else 0.0

        # Features score, fraction of notable features supported
        _score_features = score_features(data)

        # Graphics protocol score, 1.0 modern, 0.5 legacy, 0.0 none
        _score_graphics = score_graphics(data)

        _sw_name = data.get("software_name", data.get('software'))
        assert _sw_name, f"empty software_name in {yaml_path}"

        tr = data.get("terminal_results") or {}
        ts = tr.get("text_sizing", {})
        has_text_sizing = bool(ts.get("width") or ts.get("scale"))
        if has_text_sizing:
            score_language = 1.0
            _score_wide = 1.0
            _score_narrow = 1.0
            _score_zwj = 1.0
            score_emoji_vs16 = 1.0
            # VS15 is deliberately overridden here: the Text Sizing protocol can
            # programmatically set any character's cell width, so a supporting
            # terminal scores 100% on all width categories. The raw measurement
            # in the YAML remains untouched, and VS15 stays excluded from the
            # final score because its interpretation is contested (wcwidth #211).
            score_emoji_vs15 = 1.0
            _score_sri = 1.0
            _score_sfz = 1.0
            _score_ri = 1.0

        score_table.append(
            dict(
                terminal_software_name=_sw_name,
                terminal_software_version=data.get("software_version", data.get('version')),
                os_system=data["system"],
                score_emoji_vs16=score_emoji_vs16,
                score_emoji_vs15=score_emoji_vs15,
                score_sri=_score_sri,
                score_sfz=_score_sfz,
                score_ri=_score_ri,
                score_dec_modes=_score_dec_modes,
                score_resource=_score_resource,
                elapsed_seconds=_elapsed_seconds,
                score_language=score_language,
                score_wide=_score_wide,
                score_narrow=_score_narrow,
                score_zwj=_score_zwj,
                score_sixel=_score_sixel,
                sixel_support=_sixel_support,
                score_features=_score_features,
                score_graphics=_score_graphics,
                has_text_sizing=has_text_sizing,
                data=data,
                fname=os.path.basename(yaml_path),
            )
        )

    # Normalize DEC modes for display (not used in final score)
    valid_dec_modes = [e["score_dec_modes"] for e in score_table
                       if not math.isnan(e["score_dec_modes"])]
    max_dec_modes = max(valid_dec_modes) if valid_dec_modes else 1.0
    min_dec_modes = min(valid_dec_modes) if valid_dec_modes else 0.0

    # Normalize and calculate final scores
    for entry in score_table:
        # Normalize DEC modes to 0-1 (for display only)
        if not math.isnan(entry["score_dec_modes"]):
            if max_dec_modes == min_dec_modes:
                entry["score_dec_modes_norm"] = 1.0
            else:
                entry["score_dec_modes_norm"] = (
                    (entry["score_dec_modes"] - min_dec_modes)
                    / (max_dec_modes - min_dec_modes)
                )
        else:
            entry["score_dec_modes_norm"] = float('NaN')

    valid_rc = [e["score_resource"] for e in score_table
                if not math.isnan(e["score_resource"])]
    if valid_rc:
        rc_min, rc_max = min(valid_rc), max(valid_rc)
        for entry in score_table:
            if not math.isnan(entry["score_resource"]):
                if rc_max == rc_min:
                    entry["score_resource_norm"] = 1.0
                else:
                    entry["score_resource_norm"] = (
                        (entry["score_resource"] - rc_min) / (rc_max - rc_min))
            else:
                entry["score_resource_norm"] = float('NaN')

    RESOURCE_WEIGHT = 0.5
    GRAPHICS_WEIGHT = 0.5
    STANDALONE_WEIGHT = 1.0 / 3.0
    for entry in score_table:
        scores_with_weights = [
            (entry["score_language"], 1.0),
            (entry["score_emoji_vs16"], 1.0),
            # VS-15 excluded from final score - interpretation is contested,
            # see https://github.com/jquast/wcwidth/issues/211
            (entry["score_zwj"], 1.0),
            (entry["score_wide"], 1.0),
            (entry["score_narrow"], 1.0),
            (entry["score_sri"], STANDALONE_WEIGHT),
            (entry["score_sfz"], STANDALONE_WEIGHT),
            (entry["score_ri"], 1.0),
            (entry["score_features"], 1.0),
            (entry["score_graphics"], GRAPHICS_WEIGHT),
            (entry["score_resource_norm"], RESOURCE_WEIGHT)
        ]
        valid_scores_with_weights = [(s, w) for s, w in scores_with_weights if not math.isnan(s)]
        if valid_scores_with_weights:
            weighted_sum = sum(s * w for s, w in valid_scores_with_weights)
            total_weight = sum(w for s, w in valid_scores_with_weights)
            entry["score_final"] = weighted_sum / total_weight
        else:
            entry["score_final"] = float('NaN')

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
        lang_results = entry["data"]["test_results"].get("language_results") or {}
        all_languages.update(
            lang for lang in lang_results
            if lang_results[lang]["n_errors"] == 0
        )

    all_successful_languages = set()
    for lang in all_languages:
        if all(
            lang in (entry["data"]["test_results"].get("language_results") or {}) and
            (entry["data"]["test_results"].get("language_results") or {})[lang]["n_errors"] == 0
            for entry in result
        ):
            all_successful_languages.add(lang)
            for entry in result:
                lang_results = entry["data"]["test_results"].get("language_results") or {}
                if lang in lang_results:
                    del lang_results[lang]
    return result, all_successful_languages


def format_score_pct(score):
    """Format a score as a percentage, handling NaN values."""
    if math.isnan(score):
        return "N/A"
    return f'{score * 100:0.1f}%'


def format_score_int(score):
    """Format a score as an integer 0-100, handling NaN values."""
    if math.isnan(score):
        return "N/A"
    return f'{round(score * 100)}'


def _truncate_version(version):
    """Truncate version string at first '-', appending ellipsis if truncated."""
    version = str(version) if version is not None else ""
    # Strip non-printable characters (e.g. ESC from terminal response strings)
    # and trailing backslashes which break RST table formatting
    version = ''.join(ch for ch in version if ch.isprintable())
    version = version.rstrip('\\')
    if '-' in version:
        return version.split('-', 1)[0] + '\u2026'
    return version


def _classify_xtgettcap(data):
    """Classify XTGETTCAP support as full, partial, or none.

    Returns ``(label, score)`` where label is "full", "partial", or None,
    and score is 1.0, 0.5, or 0.0.

    ``data`` may be either a raw YAML-loaded dict or a score table entry
    dict.
    """
    if "data" in data:
        data = data["data"]
    tr = data.get("terminal_results") or {}
    xt = tr.get("xtgettcap", {})
    if not xt.get("supported", False):
        return (None, 0.0)
    caps = xt.get("capabilities", {})
    if not caps:
        return (None, 0.0)

    # ttyscan has_meaningful_caps: Full if meaningful caps beyond bare-minimum.
    # Skip RGB (special: parsed int) and TN (every terminal reports it).
    # Require at least 5 meaningful caps to be Full (filters out terminals
    # that only report basic color strings like setab/setaf).
    meaningful = 0
    for name, value in caps.items():
        if name in ("RGB", "TN"):
            continue
        if not value:
            meaningful += 1  # Boolean cap
        elif value.isdigit() and name not in ("colors", "Co"):
            meaningful += 1  # Meaningful numeric cap
        elif not value.isdigit() and not name.startswith("k"):
            meaningful += 1  # Output/screen string cap
        if meaningful >= 5:
            return ("full", 1.0)

    return ("partial", 0.5)


#: Kitty keyboard progressive enhancement flag keys recorded by
#: maybe_determine_kitty_keyboard()
KITTY_KB_FLAG_KEYS = ("disambiguate", "report_events", "report_alternates",
                      "report_all_keys", "report_text")


def _classify_kitty_keyboard(tr):
    """Classify Kitty keyboard support as full, partial, or none.

    Returns ``(label, score)`` where label is "full", "partial", or None.
    """
    # Score is ``(modes confirmed + state request) / 6``: full (1.0) requires
    # supporting state request and all five modes; partial is any lower score,
    # a terminal that *only* answers the state request scores 1/6.
    kk = tr.get("kitty_keyboard")
    if kk is None or "supported_flags" not in kk:
        return None, 0.0
    n_modes = sum(bool(kk.get(key)) for key in KITTY_KB_FLAG_KEYS)
    score = (n_modes + 1) / (len(KITTY_KB_FLAG_KEYS) + 1)
    return ("full" if score >= 1.0 else "partial"), score


def _classify_tofu(tr):
    """Classify font glyph coverage protocol support.

    Returns ``(protocol, score)`` where protocol is "mintty", "glyph", or None.
    """
    # Whether the terminal answers a font glyph coverage enquiry at all is a
    # property of the emulator, and is scored.  *Which* codepoints it reports a
    # glyph for is a property of the installed font, and is not.
    tofu = tr.get("tofu")
    if not isinstance(tofu, dict) or not tofu.get("supported"):
        return None, 0.0
    return tofu.get("protocol"), 1.0


def _format_features_summary(entry):
    """Format detected features as scaled score with hyperlink to Score Breakdown."""
    sw_name = entry["terminal_software_name"]
    score = entry["score_features_scaled"]
    return wrap_score_with_hyperlink(
        format_score_int(score), score, sw_name, "_scores"
    )


def _sixel_support_notes_for(sw_name):
    """Return True if *sw_name* has ``sixel_support_notes`` in terminals.yaml."""
    terminal_mixins = load_mixins()
    sw_name_lower = sw_name.lower()
    return (sw_name_lower in terminal_mixins
            and 'sixel_support_notes' in terminal_mixins[sw_name_lower])


def _format_graphics_protocols(entry, sw_name):
    """
    Format detected graphics protocols as a comma-joined list with color scoring.

    Green (1.0) for modern protocols (iTerm2, Kitty), yellow (0.5) for legacy
    only (Sixel, ReGIS), red (0.0) for none.
    """
    tr = entry["data"].get("terminal_results") or {}
    if not tr:
        return wrap_with_score_role("N/A", float('nan'))

    protocols = []
    if tr.get("sixel", False):
        sixel_label = "Sixel"
        if _sixel_support_notes_for(sw_name):
            sixel_label += " †"
        protocols.append(sixel_label)
    da_ext = tr.get("device_attributes", {}).get("extensions", [])
    if 3 in da_ext:
        protocols.append("ReGIS")
    has_modern = False
    iterm2 = tr.get("iterm2_features") or {}
    if iterm2.get("supported", False):
        protocols.append("iTerm2")
        has_modern = True
    if tr.get("kitty_graphics", False):
        protocols.append("Kitty")
        has_modern = True

    if not protocols:
        return wrap_score_with_hyperlink("none", 0.0, sw_name, "_graphics")
    score = 1.0 if has_modern else 0.5
    return wrap_score_with_hyperlink(", ".join(protocols), score, sw_name, "_graphics")


def display_tabulated_scores(score_table):
    """Display the main summary score table on the results page."""
    display_title("Results", 1)

    # Introduction and disclaimer
    print("This is a volunteer-maintained analysis created by and for terminal emulator and")
    print("TUI/CLI library developers.")
    print()
    print("We welcome productive contributions and corrections to improve the accuracy and")
    print("completeness of these measurements.")
    print()
    print(".. note::")
    print()
    print("   These test results are provided as-is and we do not guarantee their correctness.")
    print("   The scores and ratings presented here are objective measurements of Unicode and")
    print("   terminal feature support by analysis of automatic response, and should not be")
    print("   interpreted as an overall assessment of terminal emulator quality or a")
    print("   recommendation. Many factors beyond Unicode support contribute to terminal quality.")
    print("   Some terminals may optionally support features and modes not represented here.")
    print("   This data represents only automatic responses received when launched in their")
    print("   default configurations and packaged build options. Some languages and emoji")
    print("   tests may also pass 'accidentally'!")
    print()


    display_title("General Tabulated Summary", 2)  # noqa: E303

    tabulated_scores = []

    for rank, result in enumerate(score_table, start=1):
        # Build features summary (scaled score, links to Score Breakdown)
        features_list = _format_features_summary(result)

        tabulated_scores.append(
            {
                "Rank": rank,
                "Terminal Software": make_outbound_hyperlink(result["terminal_software_name"]),
                "Software Version": _truncate_version(result["terminal_software_version"]),
                "OS System": result["os_system"],

                "Score": wrap_score_with_hyperlink(
                    format_score_int(result["score_final_scaled"]),
                    result["score_final_scaled"],
                    result["terminal_software_name"],
                    "_scores"
                ),
                "WIDE": wrap_score_with_hyperlink(
                    format_score_int(result["score_wide_scaled"])
                    + (" †" if result.get("has_text_sizing") else ""),
                    result["score_wide_scaled"],
                    result["terminal_software_name"],
                    "_wide"
                ),
                "NARROW": wrap_score_with_hyperlink(
                    format_score_int(result["score_narrow_scaled"])
                    + (" †" if result.get("has_text_sizing") else ""),
                    result["score_narrow_scaled"],
                    result["terminal_software_name"],
                    "_narrow"
                ),
                "LANG": wrap_score_with_hyperlink(
                    format_score_int(result["score_language_scaled"])
                    + (" †" if result.get("has_text_sizing") else ""),
                    result["score_language_scaled"],
                    result["terminal_software_name"],
                    "_lang"
                ),
                "ZWJ": wrap_score_with_hyperlink(
                    format_score_int(result["score_zwj_scaled"])
                    + (" †" if result.get("has_text_sizing") else ""),
                    result["score_zwj_scaled"],
                    result["terminal_software_name"],
                    "_zwj"
                ),
                "VS16": wrap_score_with_hyperlink(
                    format_score_int(result["score_emoji_vs16_scaled"])
                    + (" †" if result.get("has_text_sizing") else ""),
                    result["score_emoji_vs16_scaled"],
                    result["terminal_software_name"],
                    "_vs16"
                ),
                "VS15": _wrap_id_contested(
                    format_score_int(result["score_emoji_vs15_scaled"])
                    + (" †" if result.get("has_text_sizing") else ""),
                    result["terminal_software_name"],
                    "_vs15"
                ),
                "SRI": (wrap_score_with_hyperlink(
                    format_score_int(result["score_sri_scaled"])
                    + (" †" if result.get("has_text_sizing") else ""),
                    result["score_sri_scaled"],
                    result["terminal_software_name"],
                    "_sri"
                ) if not math.isnan(result["score_sri_scaled"])
                    else _wrap_untested(result["terminal_software_name"], "_sri")),
                "SFZ": (wrap_score_with_hyperlink(
                    format_score_int(result["score_sfz_scaled"])
                    + (" †" if result.get("has_text_sizing") else ""),
                    result["score_sfz_scaled"],
                    result["terminal_software_name"],
                    "_sfz"
                ) if not math.isnan(result["score_sfz_scaled"])
                    else _wrap_untested(result["terminal_software_name"], "_sfz")),
                "RI": (wrap_score_with_hyperlink(
                    format_score_int(result["score_ri_scaled"])
                    + (" †" if result.get("has_text_sizing") else ""),
                    result["score_ri_scaled"],
                    result["terminal_software_name"],
                    "_ri"
                ) if not math.isnan(result["score_ri_scaled"])
                    else _wrap_untested(result["terminal_software_name"], "_ri")),
                "Features": features_list,
                "Graphics": _format_graphics_protocols(result, result["terminal_software_name"]),
                "Resources": wrap_score_with_hyperlink(
                    format_score_int(result["score_resource_scaled"]),
                    result["score_resource_scaled"],
                    result["terminal_software_name"],
                    "_resources"
                ),
            }
        )

    # Output role definitions for inline score coloring
    print(generate_score_roles())

    # Generate and print table with inline role-colored scores
    table_str = tabulate.tabulate(tabulated_scores, headers="keys", tablefmt="rst")
    print_datatable(table_str)

    has_any_text_sizing = any(e.get("has_text_sizing") for e in score_table)
    if has_any_text_sizing:
        print()
        print("† This terminal supports the `Kitty Text Sizing protocol`_,")
        print("which allows any application to programmatically set character widths,")
        print("remediating width issues for complex languages, emoji, and other")
        print("problematic codepoints. It is scored 100% on WIDE, NARROW, LANG, ZWJ, VS16,")
        print("VS15, SRI, SFZ, and RI. Interpretation of VS15 is `contested")
        print("<https://github.com/jquast/wcwidth/issues/211>`_ and excluded from")
        print("the final score.")
        print()
        print('.. _`Kitty Text Sizing protocol`: '
              'https://sw.kovidgoyal.net/kitty/text-sizing-protocol/')
        print()

    has_any_sixel_notes = any(
        _sixel_support_notes_for(e["terminal_software_name"])
        for e in score_table
        if e["data"].get("terminal_results", {}).get("sixel", False)
    )
    if has_any_sixel_notes:
        sixel_mixins = load_mixins()
        sixel_note_terminals = [
            e["terminal_software_name"]
            for e in score_table
            if (e["data"].get("terminal_results", {}).get("sixel", False)
                and _sixel_support_notes_for(e["terminal_software_name"]))
        ]
        for sw_name in sixel_note_terminals:
            notes = sixel_mixins[sw_name.lower()]['sixel_support_notes']
            print()
            print(f"† *{sw_name}*: {notes}")
        print()

    display_table_definitions()


def display_table_definitions():
    """Display RST role definitions for score-colored table cells."""
    print("Definitions:\n")
    print(
        "- *FINAL score*: The overall terminal emulator quality score, calculated as\n"
        "  the weighted average of all feature scores (WIDE, NARROW, LANG, ZWJ, VS16, SRI, SFZ, RI,\n"
        "  DEC Modes, and RESOURCES), then scaled (normalized 0-100%) relative to all terminals tested.\n"
        "  Higher scores indicate better overall Unicode and terminal feature support. DEC Modes and\n"
        "  RESOURCES are normalized to 0-1 range before averaging. RESOURCES and graphics is weighted at 0.5 (half as\n"
        "  powerful as other metrics), and standalone RI and Fitzpatrick are weighted at 0.3\n"
        "  to reduce its impact on the final score."
    )
    print(
        "- *WIDE score*: Percentage of wide character codepoints correctly\n"
        "  displayed for the latest Unicode version. Calculated as the total\n"
        "  number of successful codepoints divided by total codepoints tested, scaled."
    )
    print(
        "- *NARROW score*: Percentage of narrow character codepoints correctly\n"
        "  displayed for the latest Unicode version. Calculated as the total\n"
        "  number of successful codepoints divided by total codepoints tested, scaled."
    )
    print(
        "- *LANG score*: Calculated using the geometric mean of success percentages\n"
        "  across all international languages tested. This fairly accounts for partial\n"
        "  support (e.g., 99%, 98%) without letting one low score dominate, scaled."
    )
    print(
        "- *ZWJ score*: Percentage of emoji ZWJ (Zero-Width Joiner) sequences\n"
        "  correctly displayed for the latest Unicode Emoji version. Calculated as the\n"
        "  total number of successful sequences divided by total sequences tested, scaled."
    )
    print(
        "- *VS16 score*: Determined by the number of Emoji using Variation\n"
        "  Selector-16 supported as wide characters."
    )
    print(
        "- *VS15 score*: Determined by the number of Emoji using Variation\n"
        "  Selector-15 supported as narrow characters. Note: Interpretation\n"
        "  of VS15 is `contested <https://github.com/jquast/wcwidth/issues/211>`_\n"
        "  (excluded from final score).\n"
    )
    print(
        "- *SRI score*: Percentage of standalone Regional Indicator symbols\n"
        "  (U+1F1E6-U+1F1FF) correctly displayed as wide (2-cell) characters\n"
        "  when not paired as flag sequences."
    )
    print(
        "- *SFZ score*: Percentage of standalone Fitzpatrick skin tone modifiers\n"
        "  (U+1F3FB-U+1F3FF) correctly displayed as wide (2-cell) characters\n"
        "  when not combined with a base emoji."
    )
    print(
        "- *RI score*: Percentage of Regional Indicator flag sequences\n"
        "  (country and subdivision flags) correctly displayed as wide (2-cell)\n"
        "  characters. Sourced from the Unicode emoji-test.txt specification."
    )
    print(
        "- *Mode 2027*: DEC Mode 2027 (GRAPHEME_CLUSTERING) support. Shows 'enabled'\n"
        "  if the mode is currently enabled, 'may enable' if the mode is supported but\n"
        "  not enabled and can be changed to enabled, or 'no' if not supported.\n"
        "  This mode enables grapheme clustering behavior in the terminal."
    )
    print(
        "- *Tofu*: The font glyph coverage protocol the terminal answers, ``mintty``\n"
        "  (`Font Glyph Coverage Enquiry`_, ``OSC 7771``) or ``glyph`` (`Glyph\n"
        "  Protocol`_, ``APC 25a1``), by which it may be asked whether its font has a\n"
        "  glyph for a codepoint.  Answering at all counts towards the FEAT score; which\n"
        "  codepoints are covered does not, being a property of the installed font."
    )
    print(
        "- *DEC Modes*: Determined by the number of DEC private modes\n"
        "  that are changeable by the terminal, scaled."
    )
    print(
        "- *Resources*: Composite CPU, RSS memory, and run duration score (0-100),\n"
        "  where the global mean maps to 50 and the lightest/fastest terminal scores 100.\n"
        "  Computed by averaging sub-scores for mean CPU%, mean RSS (MB), and total\n"
        "  seconds, each individually scaled so the global mean = 50, min = 100, max = 0."
    )
    print()


def scale_scores(score_table, entry, key):
    """Normalize raw scores to 0-100% range across all terminals."""
    my_score = entry[key]
    if math.isnan(my_score):
        return float('NaN')

    # VS16, VS15, SRI, SFZ, RI, Sixel, and Graphics are not scaled - return raw score
    if key in ('score_emoji_vs16', 'score_emoji_vs15', 'score_sri',
               'score_sfz', 'score_ri', 'score_sixel', 'score_graphics'):
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


def _index_contested_languages():
    """Return contested graphemes by language, unioned over the width groups tested."""
    languages = {}
    for _expected_width, lang_entries in LANG_CONTESTED:
        for lang, graphemes in lang_entries:
            languages.setdefault(lang, set()).update(graphemes)
    return {lang: frozenset(graphemes) for lang, graphemes in languages.items()}


_CONTESTED_WIDE = {version: frozenset(codepoints) for version, codepoints in WIDE_CONTESTED}
_CONTESTED_NARROW = {version: frozenset(codepoints) for version, codepoints in NARROW_CONTESTED}
_CONTESTED_LANG = _index_contested_languages()


def tested_all_tables(data):
    """Return True when these results were measured with ``--all``."""
    return bool((data.get("session_arguments") or {}).get("all"))


def lookup_contested(contested_by_version, version):
    """Return the contested codepoints for *version*, or None when unknown."""
    if version in contested_by_version:
        return contested_by_version[version]
    if len(contested_by_version) == 1:
        return next(iter(contested_by_version.values()))
    return None


def contested_width_counts(data, results_key, contested_by_version):
    """Return ``(n_total, n_errors)`` of a width test, restricted to contested codepoints. """
    results = data["test_results"].get(results_key) or {}
    if not results:
        return 0, 0
    version, result = next(iter(results.items()))
    if not tested_all_tables(data) or "sampled_pct" in result:
        return result["n_total"], result["n_errors"]
    contested = lookup_contested(contested_by_version, version)
    if contested is None or result["n_total"] < len(contested):
        return result["n_total"], result["n_errors"]
    failed = {ord(decode_wchars(item["wchar"])[0])
              for item in result.get("failed_codepoints") or ()}
    return len(contested), len(failed & contested)


def contested_language_percentages(data):
    """Return ``{language: fraction_success}``, restricted to contested graphemes."""
    language_results = data.get("test_results", {}).get("language_results") or {}
    if not tested_all_tables(data):
        return {lang: result["pct_success"] / 100
                for lang, result in language_results.items()}
    percentages = {}
    for lang, result in language_results.items():
        contested = _CONTESTED_LANG.get(lang)
        if contested is None:
            continue
        if "sampled_pct" in result or result["n_total"] < len(contested):
            percentages[lang] = result["pct_success"] / 100
            continue
        failed = {decode_wchars(item["wchars"]) for item in result.get("failed") or ()}
        percentages[lang] = (len(contested) - len(failed & contested)) / len(contested)
    if not percentages:
        return {lang: result["pct_success"] / 100
                for lang, result in language_results.items()}
    return percentages


def score_zwj(data):
    """Calculate ZWJ score as percentage of successful sequences tested."""
    zwj_results = data["test_results"].get("emoji_zwj_results") or {}
    if not zwj_results:
        return 0.0
    result = next(iter(zwj_results.values()))
    n_total = result["n_total"]
    if n_total == 0:
        return 0.0
    return (n_total - result["n_errors"]) / n_total


def score_wide(data):
    """Calculate WIDE score as percentage of successful contested codepoints tested."""
    n_total, n_errors = contested_width_counts(
        data, "unicode_wide_results", _CONTESTED_WIDE)
    if n_total == 0:
        return 0.0
    return (n_total - n_errors) / n_total


def score_narrow(data):
    """Calculate NARROW score as percentage of successful contested codepoints tested."""
    n_total, n_errors = contested_width_counts(
        data, "narrow_results", _CONTESTED_NARROW)
    if n_total == 0:
        return 0.0
    return (n_total - n_errors) / n_total


def score_sri(data):
    """Calculate SRI score as percentage of standalone regional indicators tested."""
    sri_results = data["test_results"].get("sri_results") or {}
    if not sri_results:
        return float('NaN')
    result = next(iter(sri_results.values()))
    n_total = result["n_total"]
    if n_total == 0:
        return 0.0
    return (n_total - result["n_errors"]) / n_total


def score_sfz(data):
    """Calculate SFZ score as percentage of standalone Fitzpatrick modifiers tested."""
    sfz_results = data["test_results"].get("sfz_results") or {}
    if not sfz_results:
        return float('NaN')
    result = next(iter(sfz_results.values()))
    n_total = result["n_total"]
    if n_total == 0:
        return 0.0
    return (n_total - result["n_errors"]) / n_total


def score_ri(data):
    """Calculate RI score as percentage of Regional Indicator flag sequences tested."""
    ri_results = data["test_results"].get("ri_results") or {}
    if not ri_results:
        return float('NaN')
    result = next(iter(ri_results.values()))
    n_total = result["n_total"]
    if n_total == 0:
        return 0.0
    return (n_total - result["n_errors"]) / n_total


def score_lang(data):
    """
    Calculate language support score using geometric mean of contested language success.

    This gives a fairer score than simple counting of 100% languages, as it considers
    partial support (e.g., 99%, 98%) and doesn't let one low score dominate the result.
    """
    percentages = list(contested_language_percentages(data).values())
    if not percentages:
        return 0.0

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


def score_features(data):
    """
    Calculate score as fraction of notable terminal features supported.

    :rtype: float
    :returns: fraction 0.0-1.0 of features supported
    """
    tr = data.get("terminal_results") or {}
    if not tr:
        return float('NaN')

    modes = tr.get("modes") or {}
    count = 0
    total = 17

    for mode_num in (_DPM.BRACKETED_PASTE, _DPM.SYNCHRONIZED_OUTPUT,
                     _DPM.FOCUS_IN_OUT_EVENTS, _DPM.MOUSE_EXTENDED_SGR,
                     _DPM.GRAPHEME_CLUSTERING, _DPM.BRACKETED_PASTE_MIME):
        mode_key = str(mode_num) if str(mode_num) in modes else mode_num
        if mode_key in modes and _mode_is_usable(modes[mode_key]):
            count += 1

    _kk_label, kk_score = _classify_kitty_keyboard(tr)
    if kk_score > 0:
        count += kk_score

    _label, xt_score = _classify_xtgettcap(data)
    if xt_score > 0:
        count += xt_score

    _tofu_label, tofu_score = _classify_tofu(tr)
    if tofu_score > 0:
        count += tofu_score

    text_sizing = tr.get("text_sizing", {})
    if text_sizing.get("width") or text_sizing.get("scale"):
        count += 1

    if tr.get("kitty_clipboard_protocol", False):
        count += 1

    if tr.get("osc52_clipboard", False):
        count += 1

    kitty_ptr = tr.get("kitty_pointer_shapes")
    if isinstance(kitty_ptr, dict) and kitty_ptr.get("supported", False):
        count += 1

    kitty_notif = tr.get("kitty_notifications")
    if isinstance(kitty_notif, dict) and kitty_notif.get("supported", False):
        count += 1

    if tr.get("foreground_color_hex") or tr.get("background_color_hex"):
        count += 1

    if tr.get("software_method") == "XTVERSION":
        count += 1.0
    elif tr.get("software_method") == "TERM_PROGRAM":
        count += 0.5

    xt_has, dq_has, ct_has = _detect_truecolor_methods(data)
    if xt_has or dq_has:
        count += 1.0
    elif ct_has:
        count += 0.5

    return count / total


def score_graphics(data):
    """
    Calculate graphics protocol support score.

    :rtype: float
    :returns: 1.0 for modern (iTerm2/Kitty), 0.5 for legacy only (Sixel/ReGIS), 0.0 for none
    """
    tr = data.get("terminal_results") or {}
    if not tr:
        return 0.0

    has_any = False
    if tr.get("sixel", False):
        has_any = True
    da_ext = tr.get("device_attributes", {}).get("extensions", [])
    if 3 in da_ext:
        has_any = True

    iterm2 = tr.get("iterm2_features") or {}
    if iterm2.get("supported", False):
        return 1.0
    if tr.get("kitty_graphics", False):
        return 1.0

    return 0.5 if has_any else 0.0


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
    """Display a single wide character with its expected and measured widths."""
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
    """Display a table of common languages used in language support testing."""
    if all_successful_languages:
        display_title("Common Language support", 2)
        print("The following languages were successful")
        print("with all terminals emulators tested,")
        print("and will not be reported:")
        print()
        print("\n".join(sorted(all_successful_languages)) + ".")
        print()


def _format_xtgettcap_feature(entry, sw_name):
    """Format XTGETTCAP as Yes (Full), Yes (Partial), No, or N/A with score."""
    tr = entry["data"].get("terminal_results") or {}
    if not tr:
        return wrap_with_score_role("N/A", float("nan"))
    label, score = _classify_xtgettcap(entry)
    if label is None:
        return _capability_yes_no(False, sw_name, "_xtgettcap")
    text = "yes (Full)" if label == "full" else "yes (Partial)"
    return wrap_score_with_hyperlink(text, score, sw_name, "_xtgettcap")


def _detect_truecolor_methods(data):
    """Determine which methods detect 24-bit truecolor support."""
    if "data" in data:
        data = data["data"]
    tr = data.get("terminal_results") or {}
    env = data.get("environment") or {}

    xt = tr.get("xtgettcap", {})
    xt_has = xt.get("supported", False) and xt.get("capabilities", {}).get("RGB") in ("8", "8/8/8")

    dq_has = tr.get("decrqss_truecolor_probe", False)

    ct_has = env.get("COLORTERM") == "truecolor"

    return xt_has, dq_has, ct_has


def _detect_osc52_methods(data):
    """Determine which methods detect OSC 52 clipboard support."""
    if "data" in data:
        data = data["data"]
    tr = data.get("terminal_results") or {}
    methods = tr.get("osc52_detection") or {}
    return methods.get("da1_extension_52", False), methods.get("xtgettcap_ms", False)


def _is_conpty_interposed(data):
    """Check if DA1 response is from ConPTY, and that it isn't from terminal.exe."""
    if data.get("system") == "Windows":
        if (data.get("terminal_results") or {}).get("device_attributes", {}).get("service_class") == 61:
            sw_name = data.get("software_name", "").lower()
            return sw_name != "windowsterminal"
    return False


def _detect_id_methods(data):
    """Determine which methods can identify the terminal software.

    Returns ``(xt_has, tn_unique, tp_has, term_has, enq_has)`` where *tn_unique* is True
    when XTGETTCAP ``TN`` capability returns a distinctive (non-generic) name.
    """
    if "data" in data:
        data = data["data"]
    tr = data.get("terminal_results") or {}
    env = data.get("environment") or {}
    sm = tr.get("software_method", "")
    xt_has = sm == "XTVERSION"
    tp_has = sm == "TERM_PROGRAM" or bool(env.get("TERM_PROGRAM"))
    term_val = env.get("TERM", "")
    term_has = bool(term_val) and term_val not in ("xterm", "xterm-256color", "unknown")
    enq_has = sm == "ENQ"

    xt = tr.get("xtgettcap", {})
    caps = xt.get("capabilities", {}) if xt.get("supported") else {}
    tn_val = caps.get("TN", "")
    tn_unique = bool(tn_val) and tn_val.lower() not in (
        "xterm", "xterm-256color", "unknown", "")

    return xt_has, tn_unique, tp_has, term_has, enq_has


def _tn_unique_from_tr(tr):
    """Return True if XTGETTCAP TN is a distinctive (non-generic) name."""
    xt = tr.get("xtgettcap", {})
    if not xt.get("supported"):
        return False
    tn_val = xt.get("capabilities", {}).get("TN", "")
    return bool(tn_val) and tn_val.lower() not in (
        "xterm", "xterm-256color", "unknown", "")


def _capability_yes_no(value, terminal_name, section_suffix,
                       warn=False, fail=False, contested=False):
    """Format a boolean capability as a scored yes/no with hyperlink.

    When *warn* is True and *value* is True, displays 'Yes' in
    warning yellow (works locally but not over SSH).
    When *fail* is True and *value* is False, displays 'No' in
    fail red (no identification method works).
    When *contested* is True and *value* is False, displays 'No' in
    contested grey (another detection method disagrees)."""
    if value is None:
        return wrap_with_score_role("N/A", float('nan'))
    if contested and not value:
        return _wrap_id_contested("no", terminal_name, section_suffix)
    if fail and not value:
        return _wrap_id_fail("no", terminal_name)
    if warn and value:
        return _wrap_colorterm_warn("yes", terminal_name)
    status = "yes" if value else "no"
    score = 1.0 if value else 0.0
    return wrap_score_with_hyperlink(
        status, score, terminal_name, section_suffix)


def _mode_is_usable(mode_data):
    """Check if a DEC mode is usable (changeable or permanently enabled).

    DECRPM value 4 (permanently reset) means the terminal acknowledges the
    mode but it cannot be enabled: treat as unsupported.  Values 1 (set),
    2 (reset), and 3 (permanently set) are usable.  Checks the raw ``value``
    field for correctness with older data files, falling back to the
    ``supported`` and ``changeable`` fields.
    """
    value = mode_data.get('value')
    if value is not None:
        return value in {1, 2, 3}
    return (mode_data.get('changeable', False)
            or mode_data.get('enabled', False))


def _get_dec_mode_supported(modes, mode_num):
    """Check if a DEC mode is usable, handling both int and str keys."""
    mode_key = str(mode_num) if str(mode_num) in modes else mode_num
    if mode_key in modes:
        return _mode_is_usable(modes[mode_key])
    return False


def display_features_table(score_table):
    """Display a features comparison table with terminals as rows.

    Mirrors the notable features shown by the ucs-detect CLI tool's
    ``_build_features_kv_pairs`` output.
    """
    display_title("Terminal Features", 2)
    print("This table shows notable terminal features for each terminal,")
    print("matching the feature detection performed by ``ucs-detect``.")
    print()

    table_data = []
    features_sorted = sorted(
        score_table,
        key=lambda e: (math.isnan(e.get("score_features_scaled", float('NaN'))),
                       -e.get("score_features_scaled", 0) if not math.isnan(e.get("score_features_scaled", float('NaN'))) else 0))
    for rank, entry in enumerate(features_sorted, start=1):
        sw_name = entry["terminal_software_name"]
        tr = entry["data"].get("terminal_results") or {}
        modes = tr.get("modes") or {}
        _da_ext = tr.get("da", {}).get("extensions", [])  # noqa: F841
        suffix = "_dec_modes"
        tested = bool(tr)

        row = {
            "Rank": rank,
            "Terminal": make_outbound_hyperlink(sw_name, sw_name + "_scores"),
            "FEAT Score": wrap_score_with_hyperlink(
                format_score_int(entry["score_features_scaled"]),
                entry["score_features_scaled"],
                sw_name, "_scores"),
        }

        # Notable DEC modes (same as CLI)
        row["Bracketed Paste (2004)"] = _capability_yes_no(
            _get_dec_mode_supported(modes, _DPM.BRACKETED_PASTE) if tested else None,
            sw_name, suffix)
        row["Synced Output (2026)"] = _capability_yes_no(
            _get_dec_mode_supported(modes, _DPM.SYNCHRONIZED_OUTPUT) if tested else None,
            sw_name, suffix)
        row["Focus Events (1004)"] = _capability_yes_no(
            _get_dec_mode_supported(modes, _DPM.FOCUS_IN_OUT_EVENTS) if tested else None,
            sw_name, suffix)
        row["Mouse SGR (1006)"] = _capability_yes_no(
            _get_dec_mode_supported(modes, _DPM.MOUSE_EXTENDED_SGR) if tested else None,
            sw_name, suffix)
        row["Graphemes (2027)"] = _capability_yes_no(
            _get_dec_mode_supported(modes, _DPM.GRAPHEME_CLUSTERING) if tested else None,
            sw_name, suffix)
        row["Bracketed Paste MIME (5522)"] = _capability_yes_no(
            _get_dec_mode_supported(modes, _DPM.BRACKETED_PASTE_MIME) if tested else None,
            sw_name, suffix)

        # Kitty keyboard
        kk_label, kk_score = _classify_kitty_keyboard(tr)
        if not tested:
            row["Kitty Keyboard"] = _capability_yes_no(None, sw_name, "_kitty_kbd")
        elif kk_label is None:
            row["Kitty Keyboard"] = _capability_yes_no(False, sw_name, "_kitty_kbd")
        else:
            text = "yes (Full)" if kk_label == "full" else "yes (Partial)"
            row["Kitty Keyboard"] = wrap_score_with_hyperlink(
                text, kk_score, sw_name, "_kitty_kbd")

        # Graphics protocols
        row["Graphics"] = _format_graphics_protocols(entry, sw_name)

        # XTGETTCAP: classify as Full, Partial, or None
        row["XTGETTCAP"] = _format_xtgettcap_feature(entry, sw_name)

        # Text Sizing (OSC 66)
        text_sizing = tr.get('text_sizing', {})
        row["Text Size (OSC 66)"] = _capability_yes_no(
            (text_sizing.get('width') or text_sizing.get('scale'))
            if tested else None,
            sw_name, "_text_sizing")

        # Font glyph coverage enquiry (mintty OSC 7771, Glyph Protocol APC 25a1)
        tofu_protocol, tofu_score = _classify_tofu(tr)
        if tofu_protocol is None:
            row["Tofu"] = _capability_yes_no(
                False if tested and tr.get("tofu") is not None else None,
                sw_name, "_tofu")
        else:
            row["Tofu"] = wrap_score_with_hyperlink(
                tofu_protocol, tofu_score, sw_name, "_tofu")

        # Kitty Clipboard Protocol
        row["Kitty Clipboard"] = _capability_yes_no(
            tr.get('kitty_clipboard_protocol', False) if tested else None,
            sw_name, suffix)

        # OSC 52 Clipboard (DA1 ext 52 or XTGETTCAP Ms)
        osc52 = tr.get('osc52_clipboard', False)
        row["OSC 52 Clipboard"] = _capability_yes_no(
            osc52 if tested else None,
            sw_name, "_osc52")

        # Kitty Pointer Shapes (OSC 22)
        kitty_ptr = tr.get('kitty_pointer_shapes')
        row["Kitty Ptr (OSC 22)"] = _capability_yes_no(
            (isinstance(kitty_ptr, dict) and kitty_ptr.get('supported', False))
            if tested else None,
            sw_name, suffix)

        # Kitty Notifications (OSC 99)
        kitty_notif = tr.get('kitty_notifications')
        row["Kitty Notif (OSC 99)"] = _capability_yes_no(
            (isinstance(kitty_notif, dict) and kitty_notif.get('supported', False))
            if tested else None,
            sw_name, suffix)

        # Color Report (OSC 10/11)
        row["Color Report (OSC 10/11)"] = _capability_yes_no(
            (bool(tr.get('foreground_color_hex') or tr.get('background_color_hex')))
            if tested else None,
            sw_name, suffix)

        # Truecolor Detection
        xt_has, dq_has, ct_has = _detect_truecolor_methods(entry)
        row["Truecolor"] = _capability_yes_no(
            (xt_has or dq_has or ct_has) if tested else None,
            sw_name, "_truecolor")

        # Terminal Identification (XTVERSION, XTGETTCAP TN, TERM_PROGRAM, or ENQ)
        id_xt, id_tn, id_tp, id_term, id_enq = _detect_id_methods(entry)
        row["Identification"] = _capability_yes_no(
            (id_xt or id_tn or id_tp) if tested else None,
            sw_name, "_identification")

        table_data.append(row)

    if table_data:
        table_str = tabulate.tabulate(table_data, headers="keys", tablefmt="rst")
        print_datatable(table_str)
    else:
        print("No terminal feature data available.")
        print()


def _truecolor_cell(value, section_suffix, sw_name, has_any_yes, only_colorterm=False):
    """Format a truecolor detection cell as yes/no with context-aware coloring."""
    if value is None:
        return ":score-na:`N/A`"
    if value:
        return wrap_score_with_hyperlink("yes", 1.0, sw_name, section_suffix)
    if only_colorterm:
        return ":score-warn:`no`"
    if has_any_yes:
        return ":score-contested:`no`"
    return ":score-0:`no`"


def display_truecolor_table(score_table):
    """Display a truecolor detection methods comparison table."""
    display_title("Truecolor Detection", 2)
    print("This table shows which methods can be used to detect 24-bit")
    print("truecolor support for each terminal emulator. ``no`` cells are")
    print("yellow when only COLORTERM detects support (COLORTERM environment")
    print("variable is not forwarded over SSH without")
    print("``SendEnv`` / ``AcceptEnv`` configuration),")
    print("grey when at least one other method succeeds, and red when no")
    print("method can detect `Truecolor`_ support.")
    print()

    table_data = []
    for entry in score_table:
        sw_name = entry["terminal_software_name"]
        tr = entry["data"].get("terminal_results") or {}
        tested = bool(tr)

        xt_has, dq_has, ct_has = _detect_truecolor_methods(entry)
        has_any_yes = xt_has or dq_has or ct_has
        only_colorterm = ct_has and not xt_has and not dq_has

        row = {"Terminal": make_outbound_hyperlink(sw_name, sw_name + "_truecolor")}

        row["XTGETTCAP (RGB)"] = (
            _truecolor_cell(xt_has if tested else None,
                            "_truecolor", sw_name, has_any_yes, only_colorterm))
        row["DECRQSS"] = (
            _truecolor_cell(dq_has if tested else None,
                            "_truecolor", sw_name, has_any_yes, only_colorterm))
        row["COLORTERM"] = (
            _truecolor_cell(ct_has if tested else None,
                            "_truecolor", sw_name, has_any_yes, only_colorterm))

        table_data.append(row)

    if table_data:
        table_str = tabulate.tabulate(table_data, headers="keys", tablefmt="rst")
        print_datatable(table_str)
    else:
        print("No truecolor detection data available.")
        print()


def display_osc52_table(score_table):
    """Display an OSC 52 clipboard detection methods comparison table."""
    display_title("OSC 52 Clipboard Detection", 2)
    print("This table shows which methods can be used to detect `OSC 52`_")
    print("clipboard support for each terminal emulator."
          "  :ref:`DA1 <deviceattributesresponse>` extension 52")
    print("is the mechanism defined by the vt-extensions spec; `XTGETTCAP`_")
    print("``Ms`` is an alternative capability query that may work on")
    print("terminals not advertising the DA1 extension.")
    print()

    table_data = []
    for entry in score_table:
        sw_name = entry["terminal_software_name"]
        tr = entry["data"].get("terminal_results") or {}
        tested = bool(tr)

        da1_has, ms_has = _detect_osc52_methods(entry)

        row = {"Terminal": make_outbound_hyperlink(sw_name, sw_name + "_osc52")}

        row["DA1 ext 52"] = _capability_yes_no(
            da1_has if tested else None, sw_name, "_osc52",
            contested=bool(ms_has and not da1_has))
        row["XTGETTCAP Ms"] = _capability_yes_no(
            ms_has if tested else None, sw_name, "_osc52",
            contested=bool(da1_has and not ms_has))

        table_data.append(row)

    if table_data:
        table_str = tabulate.tabulate(table_data, headers="keys", tablefmt="rst")
        print_datatable(table_str)
    else:
        print("No OSC 52 detection data available.")
        print()


def display_da1_response_section(score_table):
    """Display a Device Attributes comparison table for the summary page."""
    display_inbound_hyperlink("device-attributes-response")
    display_title("Device Attributes", 2)
    print("This table shows the `Device Attributes`_ (``CSI c``) DEC service")
    print("class and per-extension feature support for each terminal.")
    print()

    # Collect all extensions across all terminals and check for ConPTY
    all_extensions = set()
    has_conpty = False
    terminal_data = []
    for entry in score_table:
        sw_name = entry["terminal_software_name"]
        tr = entry["data"].get("terminal_results") or {}
        da = tr.get("device_attributes")
        if not da:
            continue

        sc = da.get("service_class")
        extensions = da.get("extensions", [])

        sc_label = SERVICE_CLASS_NAMES.get(sc, f"Unknown Class {sc}") if sc is not None else "N/A"
        conpty = _is_conpty_interposed(entry["data"])
        has_conpty = has_conpty or conpty

        if conpty:
            label = f":score-warn:`{sc_label} †`"
        else:
            label = sc_label

        all_extensions.update(extensions)
        terminal_data.append({
            "sw_name": sw_name,
            "service_class": label,
            "conpty": conpty,
            "extensions": set(extensions),
        })

    if not terminal_data:
        print("No device attributes data available.")
        print()
        return

    # Sort extensions numerically, map to readable column names
    sorted_exts = sorted(all_extensions)
    ext_columns = [(ext, DA1_EXTENSION_NAMES.get(ext, f"Extension {ext}"))
                   for ext in sorted_exts]

    # Build table
    headers = ["Terminal", "Service Class"]
    for _, ext_name in ext_columns:
        headers.append(ext_name)

    table_data = []
    for td in terminal_data:
        row = {
            "Terminal": make_outbound_hyperlink(
                td["sw_name"], td["sw_name"] + "_graphics"),
            "Service Class": td["service_class"],
        }
        for ext_num, ext_name in ext_columns:
            if ext_num in td["extensions"]:
                if td["conpty"]:
                    row[ext_name] = f":score-warn:`{ext_num}`†"
                else:
                    row[ext_name] = f":score-pass:`{ext_num}`"
            else:
                row[ext_name] = ":score-fail:`no`"
        table_data.append(row)

    table_str = tabulate.tabulate(table_data, headers="keys", tablefmt="rst")
    print_datatable(table_str)
    print()

    if has_conpty:
        print()
        print(".. warning::")
        print()
        for line in CONPTY_DA_CAVEAT_LINES:
            print(f"   {line}")
        print()

    print(".. _`Device Attributes`: https://invisible-island.net/xterm/ctlseqs/ctlseqs.html")
    print()


def display_id_table(score_table, terminal_mixins):
    """Display a terminal identification methods comparison table."""
    display_title("Terminal Identification", 2)
    print("This table shows which methods can be used to identify the")
    print("terminal software name and version.  XTVERSION, XTGETTCAP")
    print("``TN``, and ``ENQ`` are active escape sequence queries (work")
    print("over SSH).  TERM_PROGRAM and TERM are environment variables;")
    print("TERM_PROGRAM is not forwarded over SSH without ``SendEnv`` /")
    print("``AcceptEnv`` configuration, while TERM is (though some")
    print("protocols such as Serial do not forward TERM).")
    print()

    def _is_subterminal(name):
        cfg = terminal_mixins.get(name.lower(), {})
        return bool((cfg.get("launch") or {}).get("subterminal"))

    table_data = []
    for entry in score_table:
        sw_name = entry["terminal_software_name"]
        tr = entry["data"].get("terminal_results") or {}
        tested = bool(tr)

        xt_has, tn_unique, tp_has, term_has, enq_has = _detect_id_methods(entry)
        if _is_subterminal(sw_name):
            term_has = False

        row = {"Terminal": make_outbound_hyperlink(sw_name, sw_name + "_identification")}

        has_ssh_method = xt_has or tn_unique or enq_has

        row["XTVERSION"] = _capability_yes_no(
            xt_has if tested else None, sw_name, "_identification")

        row["XTGETTCAP TN"] = _capability_yes_no(
            tn_unique if tested else None, sw_name, "_identification",
            contested=has_ssh_method and not tn_unique)

        row["ENQ"] = _capability_yes_no(
            enq_has if tested else None, sw_name, "_identification",
            contested=has_ssh_method and not enq_has)

        if has_ssh_method:
            row["TERM_PROGRAM"] = _capability_yes_no(
                tp_has if tested else None, sw_name, "_identification",
                contested=not tp_has)
            row["TERM"] = _capability_yes_no(
                term_has if tested else None, sw_name, "_identification",
                contested=not term_has)
        else:
            row["TERM_PROGRAM"] = _capability_yes_no(
                tp_has if tested else None, sw_name, "_identification",
                warn=tp_has, fail=not tp_has)
            row["TERM"] = _capability_yes_no(
                term_has if tested else None, sw_name, "_identification",
                contested=not term_has)

        table_data.append(row)

    if table_data:
        table_str = tabulate.tabulate(table_data, headers="keys", tablefmt="rst")
        print_datatable(table_str)
    else:
        print("No terminal identification data available.")
        print()


def display_id_summary_bullets(score_table, terminal_mixins):
    """Display a bulleted list categorizing terminal identification support."""

    def _link(name):
        return make_outbound_hyperlink(name, name + "_identification")

    def _is_subterminal(name):
        cfg = terminal_mixins.get(name.lower(), {})
        return bool((cfg.get("launch") or {}).get("subterminal"))

    xtversion = []
    tn_only = []
    enq_only = []
    term_program_only = []
    term_only = []
    unidentifiable = []

    total = len(score_table)
    for entry in score_table:
        sw_name = entry["terminal_software_name"]
        xt_has, tn_unique, tp_has, term_has, enq_has = _detect_id_methods(entry)
        if _is_subterminal(sw_name):
            term_has = False

        if xt_has:
            xtversion.append(sw_name)
        elif tn_unique:
            tn_only.append(sw_name)
        elif enq_has:
            enq_only.append(sw_name)
        elif tp_has:
            term_program_only.append(sw_name)
        elif term_has:
            term_only.append(sw_name)
        else:
            unidentifiable.append(sw_name)

    def _bullet(heading, terminals, extra=""):
        if not terminals:
            return
        n = len(terminals)
        links = ", ".join(_link(t) for t in sorted(terminals))
        print(f"* **{heading} ({n} of {total}):** {links}{extra}")

    groups = [
        ("Identifiable by XTVERSION", xtversion,
         " (active query, works over SSH)."),
        ("Identifiable by XTGETTCAP TN", tn_only,
         " (active query, works over SSH)."),
        ("Identifiable by ENQ only", enq_only,
         " (active query, works over SSH)."),
        ("Identifiable by TERM_PROGRAM only", term_program_only,
         " (environment variable, not forwarded over SSH)."),
        ("Identifiable by TERM only", term_only,
         " (environment variable, forwarded over SSH)."),
        ("Not identifiable", unidentifiable, ""),
    ]
    for heading, terminals, extra in sorted(
        (g for g in groups if g[1]),
        key=lambda g: len(g[1]) / total, reverse=True):
        _bullet(heading, terminals, extra)
        print()


def display_xtgettcap_summary_bullets(score_table):
    """Display a bulleted list categorizing XTGETTCAP support levels."""

    display_title("Terminal Capabilities (XTGETTCAP)", 2)

    def _link(name):
        return make_outbound_hyperlink(name, name + "_xtgettcap")

    full = []
    partial = []
    nosupport = []
    noncompliant = []

    for entry in score_table:
        sw_name = entry["terminal_software_name"]
        tr = entry["data"].get("terminal_results") or {}
        label, _score = _classify_xtgettcap(entry)

        if tr.get("xtgettcap-bad-screenleak"):
            noncompliant.append(sw_name)
        elif label == "full":
            full.append(sw_name)
        elif label == "partial":
            partial.append(sw_name)
        else:
            nosupport.append(sw_name)

    def _bullet(heading, terminals, pct, extra=""):
        if not terminals:
            return
        links = ", ".join(_link(t) for t in sorted(terminals))
        print(f"* **{heading} ({pct:.1f}%):** {links}{extra}")

    groups = [
        ("Full XTGETTCAP capability support", full,
         ". A full terminfo(5) database can be reconstructed "
         "from `XTGETTCAP`_ queries using ttyscan_. "
         "A preferred TERM from TN, and COLORTERM=truecolor "
         "from RGB may be derived."),
        ("Partial XTGETTCAP capability support", partial,
         ". A preferred TERM from TN, and COLORTERM=truecolor "
         "from RGB may be derived."),
        ("No Support", nosupport, ""),
        ("Non-compliant", noncompliant,
         " -- failed to parse DCS queries, "
         "displaying raw sequence output."),
    ]
    total = len(score_table)
    for heading, terminals, extra in sorted(
        (g for g in groups if g[1]),
        key=lambda g: len(g[1]) / total, reverse=True):
        _bullet(heading, terminals, len(terminals) / total * 100, extra)
        print()


def display_xtgettcap_comparison_table(score_table):
    """Display an XTGETTCAP terminfo capability comparison table.

    Shows all capabilities reported by each terminal via XTGETTCAP, grouped
    by shared values so terminals with the same capability value appear
    together.  Each terminal name links to its detailed XTGETTCAP results
    page.
    """
    from collections import OrderedDict

    print("This table shows `XTGETTCAP`_ terminfo capability values reported "
          "by each terminal. Terminals are grouped by shared values for "
          "each capability.")
    print()

    # Collect XTGETTCAP data from all terminals that support it
    xtgettcap_data = OrderedDict()  # sw_name -> dict of all capabilities
    all_cap_names = set()
    for entry in score_table:
        sw_name = entry["terminal_software_name"]
        tr = entry["data"].get("terminal_results") or {}
        xt = tr.get("xtgettcap", {})
        if xt.get("supported") and xt.get("capabilities"):
            caps = xt["capabilities"]
            xtgettcap_data[sw_name] = dict(caps)
            all_cap_names.update(caps.keys())

    if not xtgettcap_data:
        print("No XTGETTCAP data available.")
        print()
        return

    from blessed._capabilities import XTGETTCAP_CAPABILITIES
    cap_descriptions = dict(XTGETTCAP_CAPABILITIES)

    def _format_value(value):
        """Format a capability value for display, using repr for non-printable chars."""
        if value is None or value == "":
            return "(not reported)"
        raw = str(value)
        if any(ord(ch) < 32 or ord(ch) > 126 for ch in raw):
            return f"``{_escape_terminfo_value(raw)}``"
        if not raw.isalnum():
            escaped = raw.replace('`', '\\\\`')
            return f"``{escaped}``"
        return raw

    # Sort cap names: primary first, then alphabetical
    primary_caps = ["TN", "colors", "Co", "RGB"]
    sorted_caps = []
    for cap in primary_caps:
        if cap in all_cap_names:
            sorted_caps.append(cap)
            all_cap_names.discard(cap)
    sorted_caps.extend(sorted(all_cap_names))

    table_data = []
    for cap_name in sorted_caps:
        # Group terminals by value
        groups = {}
        for sw_name, caps in xtgettcap_data.items():
            value = caps.get(cap_name)
            value_display = _format_value(value)
            if value_display == "(not reported)":
                continue
            groups.setdefault(value_display, []).append(sw_name)

        # Skip capabilities that no terminal actually reports
        if not groups:
            continue

        # Build one cell per capability with RST line blocks for line breaks
        lines = []
        for value_display, terminals in sorted(groups.items()):
            terminal_links = ", ".join(
                make_outbound_hyperlink(t, t + "_xtgettcap")
                for t in sorted(terminals)
            )
            lines.append(f"{terminal_links}\\: {value_display}")
        table_data.append({
            "Capability": cap_name,
            "Description": cap_descriptions.get(cap_name, ""),
            "Terminals and Values": "\n".join(lines),
        })

    if table_data:
        table_str = tabulate.tabulate(table_data, headers="keys", tablefmt="rst")
        print_datatable(table_str)
    else:
        print("No XTGETTCAP data available.")
        print()


def display_performance_section(score_table):
    """Display the Test Performance section on the main results page."""
    display_title("Performance", 2)

    valid = [e for e in score_table
             if not math.isnan(e.get("score_resource", float('NaN')))]

    if not valid:
        print("No performance data available.")
        print()
        return

    print("  .. note::")
    print()
    print("     Test duration and resources used is not an indicator of software quality.")
    print()
    print("     We make a best effort to track CPU and System Memory for linux systems,")
    print("     only. Docker and cgroups are used to enforce a 2 CPU limit but it is not")
    print("     reliable.  Many terminals use GPU memory not tracked.  Some terminals")
    print("     perform differently under docker. Further, some have complex process")
    print("     groups, chrome, or OS-integration of shared resources that may not")
    print("     be accurately reflected here.")
    print()
    print()
    print("The Resources score combines CPU, memory, and runtime into a single "
          "0-100 metric.  See per-terminal pages for calculation details.")
    print()

    headers = ["Terminal", "Score", "CPU %", "RSS (MB)", "Time (s)"]
    rows = []
    valid_sorted = sorted(valid,
                          key=lambda e: e["score_resource"],
                          reverse=True)
    for e in valid_sorted:
        sw_name = e["terminal_software_name"]
        rp = e["data"].get("resource_profile") or {}
        elapsed = rp.get("elapsed_s", [])
        cpu = rp.get("cpu_pct", [])
        rss = rp.get("rss_mb", [])
        if not elapsed:
            continue
        duration = elapsed[-1]
        mean_cpu = sum(cpu) / len(cpu) if cpu else 0
        mean_rss = sum(rss) / len(rss) if rss else 0
        score = int(e["score_resource_scaled"] * 100)
        rows.append([
            make_outbound_hyperlink(sw_name, sw_name + "_time"),
            wrap_score_with_hyperlink(
                f"{score:.0f}", e["score_resource_scaled"],
                sw_name, "_resources"),
            f"{mean_cpu:.1f}",
            f"{mean_rss:.1f}",
            f"{duration:.1f}",
        ])

    print_datatable(tabulate.tabulate(rows, headers=headers, tablefmt="rst"))
    print()
    print(".. figure:: _static/profiles/all_cpu.png")
    print("   :alt: CPU usage across all terminals")
    print(f"   :width: {GRAPH_WIDTH_ALL_PX}px")
    print()
    print("   CPU usage during test execution, all terminals overlaid.")
    print()
    print(".. figure:: _static/profiles/all_rss.png")
    print("   :alt: RSS memory usage across all terminals")
    print(f"   :width: {GRAPH_WIDTH_ALL_PX}px")
    print()
    print("   RSS memory usage during test execution, all terminals overlaid.")
    print()
    print(".. figure:: _static/profiles/all_cpu_vs_time.png")
    print("   :alt: CPU % vs Duration trade-off across all terminals")
    print(f"   :width: {GRAPH_WIDTH_ALL_PX}px")
    print()
    print("   Trade-off between mean CPU % and total test duration. Dots near the")
    print("   origin use less CPU and less time. Dashed contours show equal")
    print("   CPU × time product (lower percentile = better).")
    print()
    print(".. figure:: _static/profiles/all_time.png")
    print("   :alt: Duration across all terminals")
    print(f"   :width: {GRAPH_WIDTH_ALL_PX}px")
    print()
    print("   Total test duration for each terminal, sorted fastest to slowest.")
    print("   Log scale on the X axis.")
    print()


def show_score_breakdown(sw_name, entry, plot_filename_scaled):
    """Display the detailed score breakdown for a single terminal."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_scores")
    display_title("Score Breakdown", 3)
    print(f"Detailed breakdown of how scores are calculated for *{sw_name}*:")
    print()

    # Create table showing raw scores, scaled scores, and how they're calculated
    def format_raw_score(score):
        return "N/A" if math.isnan(score) else f'{score * 100:0.2f}%'

    score_breakdown = [
        {
            "#": 1,
            "Score Type": make_outbound_hyperlink("WIDE", sw_name + "_wide"),
            "Raw Score": format_raw_score(entry["score_wide"]),
            "Final Scaled Score": format_score_pct(entry["score_wide_scaled"]),
        },
        {
            "#": 2,
            "Score Type": make_outbound_hyperlink("NARROW", sw_name + "_narrow"),
            "Raw Score": format_raw_score(entry["score_narrow"]),
            "Final Scaled Score": format_score_pct(entry["score_narrow_scaled"]),
        },
        {
            "#": 3,
            "Score Type": make_outbound_hyperlink("ZWJ", sw_name + "_zwj"),
            "Raw Score": format_raw_score(entry["score_zwj"]),
            "Final Scaled Score": format_score_pct(entry["score_zwj_scaled"]),
        },
        {
            "#": 4,
            "Score Type": make_outbound_hyperlink("LANG", sw_name + "_lang"),
            "Raw Score": format_raw_score(entry["score_language"]),
            "Final Scaled Score": format_score_pct(entry["score_language_scaled"]),
        },
        {
            "#": 5,
            "Score Type": make_outbound_hyperlink("VS16", sw_name + "_vs16"),
            "Raw Score": format_raw_score(entry["score_emoji_vs16"]),
            "Final Scaled Score": format_score_pct(entry["score_emoji_vs16_scaled"]),
        },
        {
            "#": 6,
            "Score Type": make_outbound_hyperlink("VS15", sw_name + "_vs15"),
            "Raw Score": format_raw_score(entry["score_emoji_vs15"]),
            "Final Scaled Score": "*(excluded)*",
        },
        {
            "#": 7,
            "Score Type": make_outbound_hyperlink("SRI", sw_name + "_sri"),
            "Raw Score": format_raw_score(entry["score_sri"]),
            "Final Scaled Score": (format_score_pct(entry["score_sri_scaled"])
                                   if not math.isnan(entry["score_sri"]) else "*(excluded)*"),
        },
        {
            "#": 8,
            "Score Type": make_outbound_hyperlink("SFZ", sw_name + "_sfz"),
            "Raw Score": format_raw_score(entry["score_sfz"]),
            "Final Scaled Score": (format_score_pct(entry["score_sfz_scaled"])
                                   if not math.isnan(entry["score_sfz"]) else "*(excluded)*"),
        },
        {
            "#": 9,
            "Score Type": make_outbound_hyperlink("RI", sw_name + "_ri"),
            "Raw Score": format_raw_score(entry["score_ri"]),
            "Final Scaled Score": (format_score_pct(entry["score_ri_scaled"])
                                   if not math.isnan(entry["score_ri"]) else "*(excluded)*"),
        },
        {
            "#": 10,
            "Score Type": make_outbound_hyperlink("FEAT", sw_name + "_features_details"),
            "Raw Score": format_raw_score(entry["score_features"]),
            "Final Scaled Score": format_score_pct(entry["score_features_scaled"]),
        },
        {
            "#": 11,
            "Score Type": make_outbound_hyperlink("Graphics", sw_name + "_graphics"),
            "Raw Score": f"{entry['score_graphics']*100:.0f}%",  # noqa: E226
            "Final Scaled Score": format_score_pct(entry["score_graphics_scaled"]),
        },
        {
            "#": 12,
            "Score Type": make_outbound_hyperlink("Resources", sw_name + "_resources"),
            "Raw Score": format_score_pct(entry["score_resource_norm"]) if not math.isnan(entry["score_resource"]) else "N/A",
            "Final Scaled Score": format_score_pct(entry["score_resource_scaled"]),
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
    print(f"   :width: {SCORE_PLOT_WIDTH_PX}px")
    print()
    print("   Scaled scores comparison across all metrics (normalized 0-100%)")
    print()

    print("**Final Scaled Score Calculation:**")
    print()
    print(f"- Raw Final Score: {format_raw_score(entry['score_final'])}")
    print("  (weighted average: WIDE + NARROW + ZWJ + LANG + VS16 + 0.33 * SRI + 0.33 * SFZ + RI + CAP + 0.5 * GFX + 0.5 * RSC)")
    print("  the categorized 'average' absolute support level of this terminal.")
    print()
    print("  .. note::")
    print()
    print("     RSC (Resources) is a composite CPU, memory, and runtime score.")
    print("     RSC is weighted at 0.5 (half as powerful as other metrics).")
    print("     FEAT (Features) is the fraction of notable features supported.")
    print("     GFX (Graphics) scores 100% for modern protocols (iTerm2, Kitty),")
    print("     50% for legacy only (Sixel, ReGIS), 0% for none.")
    print()
    print(f"- Final Scaled Score: {format_score_pct(entry['score_final_scaled'])}")
    print("  (normalized across all terminals tested).")
    print("  *Final Scaled scores* are normalized (0-100%) relative to all terminals tested")
    print()

    # Add detailed score breakdowns for each type
    print("**WIDE Score Details:**")
    print()
    n_total, n_errors = contested_width_counts(
        entry["data"], "unicode_wide_results", _CONTESTED_WIDE)
    if n_total:
        n_success = n_total - n_errors
        print("Wide character support calculation:")
        print()
        print(f"- Total successful contested codepoints: {n_success}")
        print(f"- Total contested codepoints tested: {n_total}")
        print(f"- Formula: {n_success} / {n_total}")
        print(f"- Result: {entry['score_wide']*100:.2f}%")  # noqa: E226
    else:
        print("No WIDE character support detected.")
    print()

    print("**NARROW Score Details:**")
    print()
    n_total, n_errors = contested_width_counts(
        entry["data"], "narrow_results", _CONTESTED_NARROW)
    if n_total:
        n_success = n_total - n_errors
        print("Narrow character support calculation:")
        print()
        print(f"- Total successful contested codepoints: {n_success}")
        print(f"- Total contested codepoints tested: {n_total}")
        print(f"- Formula: {n_success} / {n_total}")
        print(f"- Result: {entry['score_narrow']*100:.2f}%")  # noqa: E226
    else:
        print("No NARROW character support detected.")
    print()

    print("**ZWJ Score Details:**")
    print()
    zwj_results = entry["data"]["test_results"].get("emoji_zwj_results") or {}
    if zwj_results:
        result = next(iter(zwj_results.values()))
        n_total = result["n_total"]
        n_success = n_total - result["n_errors"]
        print("Emoji ZWJ (Zero-Width Joiner) support calculation:")
        print()
        print(f"- Total successful sequences: {n_success}")
        print(f"- Total sequences tested: {n_total}")
        print(f"- Formula: {n_success} / {n_total}")
        print(f"- Result: {entry['score_zwj']*100:.2f}%")  # noqa: E226
    else:
        print("No ZWJ support detected.")
    print()

    print("**VS16 Score Details:**")
    print()
    _vs16_base = entry["data"]["test_results"].get("emoji_vs16_results", {})
    if _vs16_base:
        vs16_results = next(iter(_vs16_base.values()))
        n_errors = vs16_results["n_errors"]
        n_total = vs16_results["n_total"]
        pct_success = vs16_results["pct_success"]

        print("Variation Selector-16 support calculation:")
        print()
        print(f"- Errors: {n_errors} of {n_total} codepoints tested")
        print(f"- Success rate: {pct_success:.1f}%")
        print(f"- Formula: {pct_success:.1f} / 100")
        print(f"- Result: {entry['score_emoji_vs16']*100:.2f}%")  # noqa: E226
    else:
        print("VS16 results not available.")
    print()

    print("**Variation Selector-15 support:**")
    print()
    print(".. note:: Interpretation of VS-15 is `contested <https://github.com/jquast/wcwidth/issues/211>`_.\n"
          "   Its width behavior is not consistently implemented across terminals;\n"
          "   this measurement is informational and excluded from final scoring.")
    print()
    vs15_base = entry["data"]["test_results"].get("emoji_vs15_results",
                                                   entry["data"]["test_results"].get("emoji_vs15_type_a_results"))  # noqa: E127
    if vs15_base:
        vs15_results = next(iter(vs15_base.values()))
        n_errors = vs15_results["n_errors"]
        n_total = vs15_results["n_total"]
        pct_success = vs15_results["pct_success"]

        print("Variation Selector-15 support calculation:")
        print()
        print(f"- Errors: {n_errors} of {n_total} codepoints tested")
        print(f"- Success rate: {pct_success:.1f}%")
        print(f"- Formula: {pct_success:.1f} / 100")
        print(f"- Result: {entry['score_emoji_vs15']*100:.2f}%"
              + (" † (Text Sizing protocol)"
                 if entry.get("has_text_sizing") else ""))  # noqa: E226
    else:
        print("VS15 results not available.")
    print()

    _UNTESTED_NOTE = ("This terminal has not yet been tested with the latest version "
                       "of ucs-detect. This score is excluded from the final score.")  # noqa: E127

    print("**SRI Score Details:**")
    print()
    sri_results = entry["data"]["test_results"].get("sri_results") or {}
    if sri_results:
        result = next(iter(sri_results.values()))
        n_total = result["n_total"]
        n_success = n_total - result["n_errors"]
        print("Standalone Regional Indicator support calculation:")
        print()
        print(f"- Total successful codepoints: {n_success}")
        print(f"- Total codepoints tested: {n_total}")
        print(f"- Formula: {n_success} / {n_total}")
        print(f"- Result: {entry['score_sri']*100:.2f}%")  # noqa: E226
    else:
        print(f".. note:: {_UNTESTED_NOTE}")
    print()

    print("**SFZ Score Details:**")
    print()
    sfz_results = entry["data"]["test_results"].get("sfz_results") or {}
    if sfz_results:
        result = next(iter(sfz_results.values()))
        n_total = result["n_total"]
        n_success = n_total - result["n_errors"]
        print("Standalone Fitzpatrick skin tone modifier support calculation:")
        print()
        print(f"- Total successful codepoints: {n_success}")
        print(f"- Total codepoints tested: {n_total}")
        print(f"- Formula: {n_success} / {n_total}")
        print(f"- Result: {entry['score_sfz']*100:.2f}%")  # noqa: E226
    else:
        print(f".. note:: {_UNTESTED_NOTE}")
    print()

    print("**RI Score Details:**")
    print()
    ri_results = entry["data"]["test_results"].get("ri_results") or {}
    if ri_results:
        result = next(iter(ri_results.values()))
        n_total = result["n_total"]
        n_success = n_total - result["n_errors"]
        print("Regional Indicator flag sequence support calculation:")
        print()
        print(f"- Total successful sequences: {n_success}")
        print(f"- Total sequences tested: {n_total}")
        print(f"- Formula: {n_success} / {n_total}")
        print(f"- Result: {entry['score_ri']*100:.2f}%")  # noqa: E226
    else:
        print(f".. note:: {_UNTESTED_NOTE}")
    print()

    display_inbound_hyperlink(sw_name + "_features_details")
    print("**Features Score Details:**")
    print()
    if not math.isnan(entry["score_features"]):
        tr = entry["data"].get("terminal_results") or {}
        modes = tr.get("modes") or {}
        xt_label, xt_score = _classify_xtgettcap(entry)
        xt_has, dq_has, ct_has = _detect_truecolor_methods(entry)
        if xt_has or dq_has:
            tc_score = 1.0
        elif ct_has:
            tc_score = 0.5
        else:
            tc_score = 0.0

        cap_checks = [
            (_fmt_mode(_DPM.BRACKETED_PASTE),
             float(_get_dec_mode_supported(modes, _DPM.BRACKETED_PASTE)),
             "_dec_modes"),
            (_fmt_mode(_DPM.SYNCHRONIZED_OUTPUT),
             float(_get_dec_mode_supported(modes, _DPM.SYNCHRONIZED_OUTPUT)),
             "_dec_modes"),
            (_fmt_mode(_DPM.FOCUS_IN_OUT_EVENTS),
             float(_get_dec_mode_supported(modes, _DPM.FOCUS_IN_OUT_EVENTS)),
             "_dec_modes"),
            (_fmt_mode(_DPM.MOUSE_EXTENDED_SGR),
             float(_get_dec_mode_supported(modes, _DPM.MOUSE_EXTENDED_SGR)),
             "_dec_modes"),
            (_fmt_mode(_DPM.GRAPHEME_CLUSTERING),
             float(_get_dec_mode_supported(modes, _DPM.GRAPHEME_CLUSTERING)),
             "_dec_modes"),
            (_fmt_mode(_DPM.BRACKETED_PASTE_MIME),
             float(_get_dec_mode_supported(modes, _DPM.BRACKETED_PASTE_MIME)),
             "_dec_modes"),
            ("Kitty Keyboard (Full)" if _classify_kitty_keyboard(tr)[0] == "full"
             else "Kitty Keyboard (Partial)" if _classify_kitty_keyboard(tr)[0]
             else "Kitty Keyboard",
             _classify_kitty_keyboard(tr)[1],
             "_kitty_kbd"),
            ("XTGETTCAP (Full)" if xt_label == "full"
             else "XTGETTCAP (Partial)" if xt_label
             else "XTGETTCAP",
             xt_score,
             "_xtgettcap"),
            ("Text Sizing (OSC 66)",
             float(tr.get("text_sizing", {}).get("width")
              or tr.get("text_sizing", {}).get("scale")
              or False),
             "_text_sizing"),
            ("Tofu Detection",
             _classify_tofu(tr)[1],
             "_tofu"),
            ("Kitty Clipboard Protocol",
             float(tr.get("kitty_clipboard_protocol", False)),
             "_dec_modes"),
            ("OSC 52 Clipboard",
             float(tr.get("osc52_clipboard", False)),
             "_osc52"),
            ("Kitty Pointer Shapes (OSC 22)",
             float(isinstance(tr.get("kitty_pointer_shapes"), dict)
             and tr.get("kitty_pointer_shapes", {}).get("supported", False)),
             "_dec_modes"),
            ("Kitty Notifications (OSC 99)",
             float(isinstance(tr.get("kitty_notifications"), dict)
             and tr.get("kitty_notifications", {}).get("supported", False)),
             "_dec_modes"),
            ("Color Report (OSC 10/11)",
             float(bool(tr.get("foreground_color_hex") or tr.get("background_color_hex"))),
             "_dec_modes"),
            ("Terminal Identification (XTVERSION)"
             if tr.get("software_method") == "XTVERSION"
             else "Terminal Identification (XTGETTCAP TN)"
             if _tn_unique_from_tr(tr)
             else "Terminal Identification (TERM_PROGRAM)"
             if tr.get("software_method") == "TERM_PROGRAM"
             else "Terminal Identification",
             (1.0 if tr.get("software_method") == "XTVERSION"
              else 1.0 if _tn_unique_from_tr(tr)
              else 0.5 if tr.get("software_method") == "TERM_PROGRAM"
              else 0.0),
             "_identification"),
            ("Truecolor Detection", tc_score, "_truecolor"),
        ]
        cap_count = sum(v for _, v, _ in cap_checks)
        print(f"Notable terminal features ({cap_count} / {len(cap_checks)}):")
        print()
        for name, score, section_suffix in cap_checks:
            if score == 0.5:
                status = "partial"
            elif score:
                status = "yes"
            else:
                status = "no"
            link_text = make_outbound_hyperlink(name, sw_name + section_suffix)
            print(f"- {link_text}: **{status}**")
        print()
        print(f"Raw score: {entry['score_features']*100:.2f}%")  # noqa: E226
    else:
        print("Features results not available.")
    print()

    print("**Graphics Score Details:**")
    print()
    tr = entry["data"].get("terminal_results") or {}
    gfx_score = entry["score_graphics"]
    gfx_protocols = []
    if tr.get("sixel", False):
        gfx_protocols.append(("Sixel", True))
    else:
        gfx_protocols.append(("Sixel", False))
    da_ext = tr.get("device_attributes", {}).get("extensions", [])
    gfx_protocols.append(("ReGIS", 3 in da_ext))
    iterm2 = tr.get("iterm2_features") or {}
    gfx_protocols.append(("iTerm2", iterm2.get("supported", False)))
    gfx_protocols.append(("Kitty", tr.get("kitty_graphics", False)))
    supported = [name for name, v in gfx_protocols if v]
    print(f"Graphics protocol support ({int(gfx_score * 100)}%):")
    print()
    for name, detected in gfx_protocols:
        status = "yes" if detected else "no"
        print(f"- {name}: **{status}**")
    print()
    print("Scoring: 100% for modern (iTerm2/Kitty), 50% for legacy only (Sixel/ReGIS), 0% for none")
    print()

    print("**Resource Score Details:**")
    print()
    if not math.isnan(entry["score_resource"]):
        rp = entry["data"].get("resource_profile") or {}
        elapsed_data = rp.get("elapsed_s", [])
        cpu_data = rp.get("cpu_pct", [])
        rss_data = rp.get("rss_mb", [])
        mean_cpu = sum(cpu_data) / len(cpu_data) if cpu_data else 0
        mean_rss = sum(rss_data) / len(rss_data) if rss_data else 0
        duration = elapsed_data[-1] if elapsed_data else 0

        print()
        print(f"- Duration: {duration:.1f}s")
        print(f"- Mean CPU: {mean_cpu:.1f}%")
        print(f"- Mean RSS: {mean_rss:.1f} MB")
        print(f"- Resources Score: {entry['score_resource_scaled']*100:.0f}/100")
        print("- Note: log-scale composite cost = log(CPU+1) + log(RSS+1) + log(time+1)")
        print(f"- Scaled result: {format_score_pct(entry['score_resource_scaled'])}")
    else:
        print("Resource profiling data not available.")
    print()

    print("**LANG Score Details (Geometric Mean):**")
    print()
    percentages = contested_language_percentages(entry["data"])
    if percentages:
        n = len(percentages)
        geo_mean = entry["score_language"]

        print("Geometric mean calculation:")
        print()
        print(f"- Formula: (p₁ × p₂ × ... × pₙ)^(1/n) where n = {n} contested languages")
        print("- About `geometric mean <https://en.wikipedia.org/wiki/Geometric_mean>`_")
        print(f"- Result: {geo_mean * 100:.2f}%")
    print()


def show_software_header(entry, sw_name, terminal_mixins):
    """Display the header block for a terminal's detail page."""
    display_inbound_hyperlink(entry["terminal_software_name"])
    display_title(sw_name, 2)
    print()
    print(f'Tested Software version {entry["terminal_software_version"]} on {entry["os_system"]}.')

    # Look up homepage URL and description from terminal_mixins (case-insensitive)
    sw_name_lower = entry["terminal_software_name"].lower()
    if sw_name_lower in terminal_mixins:
        description = terminal_mixins[sw_name_lower].get('description')
        if description:
            print(f'{description}')
        homepage = terminal_mixins[sw_name_lower].get('homepage')
        if homepage:
            print(f'The homepage URL of this terminal is {homepage}.')

    print('Full results available at ucs-detect_ repository path')
    print(f"`data/{entry['fname']} <{GITHUB_DATA_LINK.format(fname=entry['fname'])}>`_.")
    print()

    # A terminal measured in a non-default runtime environment describes it here,
    # e.g. mintty, which only answers queries itself outside of ConPTY.
    if sw_name_lower in terminal_mixins:
        env_notes = terminal_mixins[sw_name_lower].get('test_environment_notes')
        if env_notes:
            print(env_notes)
            print()

    # If this is a subterminal (terminal multiplexer), note the host terminal
    if sw_name_lower in terminal_mixins:
        tcfg = terminal_mixins[sw_name_lower]
        if (tcfg.get("launch") or {}).get("subterminal"):
            host_name = "ghostty"
            host_link = make_link(host_name)
            host_cfg = terminal_mixins.get(host_name.lower(), {})
            host_desc = host_cfg.get("description", "")
            host_homepage = host_cfg.get("homepage", "")
            print(f"*{sw_name}* is a terminal multiplexer. "
                  f"These tests were executed in host terminal "
                  f"`:ref:`{host_name} <{host_link}xtgettcap>`_.")
            if host_desc:
                print(f"{host_desc}")
            if host_homepage:
                print(f"The homepage URL of this host terminal is {host_homepage}.")
            print()


def show_wide_character_support(sw_name, entry):
    """Display the wide character support results for a terminal."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_wide")
    display_title("Wide character support", 3)
    wide_results = entry.get("data", {}).get("test_results", {}).get("unicode_wide_results") or {}
    if wide_results:
        result = next(iter(wide_results.values()))
        pct = result["pct_success"]
        print(
            f"Wide character support of *{sw_name}* "
            f"is **{pct:0.1f}%** ({result['n_errors']} errors "
            f"of {result['n_total']} codepoints tested)."
        )
        print()
        if result["n_errors"] > 0:
            fail_record = find_best_failure(result["failed_codepoints"])
            show_record_failure(
                sw_name, "of a WIDE character,", fail_record,
                category="wide",
            )
    else:
        print(f"Wide character results for *{sw_name}* are not available.")
        print()


def show_narrow_results(sw_name, entry):
    """Display the narrow character support results for a terminal."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_narrow")
    display_title("Narrow character support", 3)
    narrow_results = entry.get("data", {}).get("test_results", {}).get("narrow_results") or {}
    if narrow_results:
        result = next(iter(narrow_results.values()))
        pct = result["pct_success"]
        print(
            f"Narrow character support of *{sw_name}* "
            f"is **{pct:0.1f}%** ({result['n_errors']} errors "
            f"of {result['n_total']} codepoints tested)."
        )
        print()
        if result["n_errors"] > 0:
            fail_record = find_best_failure(result["failed_codepoints"])
            show_record_failure(
                sw_name, "of a NARROW character,", fail_record,
                category="narrow",
            )
    else:
        print(f"Narrow character results for *{sw_name}* are not available.")
        print()


def show_emoji_zwj_results(sw_name, entry):
    """Display the emoji ZWJ sequence results for a terminal."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_zwj")
    display_title("Emoji ZWJ support", 3)
    zwj_results = entry["data"]["test_results"].get("emoji_zwj_results") or {}
    if not zwj_results:
        print(f"Emoji ZWJ results for *{sw_name}* are not available.")
        print()
        return
    result = next(iter(zwj_results.values()))
    n_errors = result["n_errors"]
    n_total = result["n_total"]
    pct = ((n_total - n_errors) / n_total * 100) if n_total else 0
    print(
        f"Compatibility of *{sw_name}* with the Unicode Emoji ZWJ sequence "
        f"table is **{pct:0.1f}%** ({n_errors} errors "
        f"of {n_total} sequences tested)."
    )
    print()
    if n_errors > 0:
        fail_record = find_best_failure(result["failed_codepoints"])
        show_record_failure(sw_name, "of an Emoji ZWJ Sequence,", fail_record,
                            category="zwj")


def show_vs_results(sw_name, entry, variation_str):
    """Display VS-15 and VS-16 variation selector results for a terminal."""
    display_inbound_hyperlink(entry["terminal_software_name"] + f"_vs{variation_str}")
    display_title(f"Variation Selector-{variation_str} support", 3)

    # Check if the VS results exist (e.g., VS15 might not be available for all terminals)
    vs_results_key = f"emoji_vs{variation_str}_results"
    vs_data = entry["data"]["test_results"].get(vs_results_key, {})
    if not vs_data:
        print(f"Emoji VS-{variation_str} results for *{sw_name}* are not available.")
        print()
        return

    records = next(iter(vs_data.values()))
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
        show_record_failure(sw_name, whatis, failure_record,
                            test_type=f"vs{variation_str}",
                            category=f"vs{variation_str}")
    print()


def show_device_attributes(sw_name, entry):
    """Display device attributes with raw response and extension breakdown."""
    sw_link = make_link(sw_name) + "_device_attributes"
    display_inbound_hyperlink(sw_link)
    display_title("Device Attributes", 3)

    tr = entry["data"].get("terminal_results") or {}
    da = tr.get("device_attributes")
    if not da:
        print("No Device Attributes response available.")
        print()
        return

    raw = da.get("raw", "")
    service_class = da.get("service_class")
    extensions = da.get("extensions", [])

    if raw:
        print(f"- **Raw response:** ``{repr(raw)}``")
    if service_class is not None:
        sc_name = SERVICE_CLASS_NAMES.get(service_class, f"Unknown Class {service_class}")
        print(f"- **Service class:** {service_class} ({sc_name})")
    print()

    if extensions:
        print("**Detected Extensions:**")
        print()
        table_data = []
        for ext in sorted(extensions):
            desc = DA1_EXTENSION_NAMES.get(ext, "unknown")
            table_data.append({"Code": str(ext), "Description": desc})
        table_str = tabulate.tabulate(table_data, headers="keys", tablefmt="rst")
        for line in table_str.split('\n'):
            if line.strip():
                print(f"   {line}")
            else:
                print()
        print()
    else:
        print("No extensions reported.")
        print()

    if _is_conpty_interposed(entry["data"]):
        print(".. note::")
        print()
        for line in CONPTY_DA_CAVEAT_LINES:
            print(f"   {line}")
        print()


def show_graphics_results(sw_name, entry):
    """Display graphics protocol support results."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_graphics")
    display_title("Graphics Protocol Support", 3)

    tr = entry["data"].get("terminal_results") or {}
    sixel_supported = tr.get("sixel", False)
    da_ext = tr.get("device_attributes", {}).get("extensions", [])
    regis_supported = 3 in da_ext
    kitty_supported = tr.get("kitty_graphics", False)
    iterm2_supported = (tr.get("iterm2_features") or {}).get("supported", False)

    protocols = []
    if sixel_supported:
        sixel_label = "Sixel_"
        if _sixel_support_notes_for(sw_name):
            sixel_label = "Sixel_ \u2020"
        protocols.append(sixel_label)
    if regis_supported:
        protocols.append("ReGIS_")
    if iterm2_supported:
        protocols.append("`iTerm2 inline images`_")
    if kitty_supported:
        protocols.append("`Kitty graphics`_")

    if protocols:
        print(f"*{sw_name}* supports the following graphics protocols: "
              f"{', '.join(protocols)}.")
    else:
        print(f"*{sw_name}* does not report support for any graphics protocols.")
    print()

    if _sixel_support_notes_for(sw_name):
        notes = load_mixins()[sw_name.lower()]['sixel_support_notes']
        print(f"**Note:** {notes}")
        print()

    print("**Detection Methods:**")
    print()

    sixel_detected = 4 in da_ext
    regis_detected = 3 in da_ext
    if sixel_detected and regis_detected:
        da1_status = "**Detected**"
    elif sixel_detected or regis_detected:
        parts = []
        if sixel_detected:
            parts.append("Sixel: **Detected**")
        else:
            parts.append("Sixel: Not detected")
        if regis_detected:
            parts.append("ReGIS: **Detected**")
        else:
            parts.append("ReGIS: Not detected")
        da1_status = "; ".join(parts)
    else:
        da1_status = "**Not detected**"

    sixel_indicator = "present" if sixel_detected else "not present"
    regis_indicator = "present" if regis_detected else "not present"
    da_link = make_link(sw_name) + "_device_attributes"
    print(f"- **Sixel** and **ReGIS**: {da1_status} via the"
          f" :ref:`Device Attributes <{da_link}>` (DA1) query"
          f" ``CSI c`` (``\\x1b[c``)."
          f" Sixel indicator (``4``): {sixel_indicator},"
          f" ReGIS indicator (``3``): {regis_indicator}.")

    kitty_status = "**Detected**" if kitty_supported else "Not detected"
    print(f"- **Kitty graphics**: {kitty_status} by sending a"
          f" Kitty graphics query and checking for an ``OK`` response.")

    iterm2_status = "**Detected**" if iterm2_supported else "Not detected"
    print(f"- **iTerm2 inline images**: {iterm2_status} via the"
          f" iTerm2 capabilities query ``OSC 1337 ; Capabilities``.")
    print()

    print('.. _Sixel: https://en.wikipedia.org/wiki/Sixel')
    print('.. _ReGIS: https://en.wikipedia.org/wiki/ReGIS')
    print('.. _`iTerm2 inline images`: https://iterm2.com/documentation-images.html')
    print()


def display_title(text, depth):
    """Write an RST section heading at the given nesting depth."""
    print(text)
    print(RST_DEPTH[depth] * len(text))
    print()


def show_language_results(sw_name, entry):
    """Display the language grapheme cluster support results for a terminal."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_lang")
    display_title("Language Support", 3)
    lang_results = entry["data"]["test_results"].get("language_results") or {}
    if not lang_results:
        print(f"Language results for *{sw_name}* are not available.")
        print()
        return
    languages_successful = [
        lang for lang in lang_results
        if lang_results[lang]["n_errors"] == 0
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
        for lang in lang_results
        if lang_results[lang]["n_errors"] > 0
    ]
    languages_failed.sort(
        key=lambda lang: lang_results[lang]["pct_success"]
    )
    tabulated_failed_language_results = [
        {
            "lang": make_outbound_hyperlink(lang, sw_name + "_lang_" + lang),
            "n_errors": lang_results[lang]["n_errors"],
            "n_total": lang_results[lang]["n_total"],
            "pct_success": f'{lang_results[lang]["pct_success"]:0.1f}%',
        }
        for lang in languages_failed
    ]

    if not languages_failed:
        print("All tested languages are fully supported.")
        print()
        return
    print(f"The following {len(languages_failed)} languages are not fully supported:")
    print()
    table_str = tabulate.tabulate(tabulated_failed_language_results, headers="keys", tablefmt="rst")
    print_datatable(table_str)
    for failed_lang in languages_failed:
        fail_record = lang_results[failed_lang]["failed"][0]
        safe_lang = safe_name(failed_lang)
        display_inbound_hyperlink(sw_name + "_lang_" + failed_lang)
        display_title(failed_lang, 4)
        show_record_failure(sw_name, f"of language *{failed_lang}*", fail_record,
                            category=f"lang_{safe_lang}")


def show_dec_modes_results(sw_name, entry):
    """
    Display detailed DEC private mode support results.
    """
    display_inbound_hyperlink(entry["terminal_software_name"] + "_dec_modes")
    display_title("DEC Private Modes Support", 3)

    if "terminal_results" not in entry["data"] or "modes" not in entry["data"]["terminal_results"]:
        print("This Terminal does not appear capable of reporting about any DEC Private modes.")
        print()
        return

    modes = entry["data"]["terminal_results"]["modes"]
    total_modes = len(modes)

    if total_modes == 0:
        print("This Terminal does not appear capable of reporting about any DEC Private modes.")
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
          f"({(supported_modes/total_modes * 100):0.1f}% support, "  # noqa: E226
          f"{(changeable_modes/total_modes * 100):0.1f}% changeable).")  # noqa: E226
    print()

    # Check if terminal reports supporting all modes tested (likely an error)
    if supported_modes == total_modes and total_modes == 159:
        print(".. warning::")
        print()
        print(f"   This terminal reports to support all {total_modes} modes tested, but this")
        print("   is probably an error.")
        print()

    # Check if many modes are supported but not enabled or changeable
    if supported_but_inactive > 50:
        print(".. note::")
        print()
        print(f"   This terminal reports {supported_but_inactive} modes as supported, but these modes")
        print("   are neither enabled nor changeable. This may sometimes be interpreted as")
        print("   not truly supporting these modes, as they cannot be toggled or utilized.")
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


def show_kitty_keyboard_results(sw_name, entry):
    """Display Kitty keyboard protocol detection results."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_kitty_kbd")
    display_title("Kitty Keyboard Protocol", 3)

    tr = entry["data"].get("terminal_results") or {}
    kitty_kb = tr.get("kitty_keyboard")

    if kitty_kb is None or "supported_flags" not in kitty_kb:
        print(f"*{sw_name}* does not support the `Kitty keyboard protocol`_.")
        print()
        print('.. _`Kitty keyboard protocol`: '
              'https://sw.kovidgoyal.net/kitty/keyboard-protocol/')
        print()
        return

    print(f"*{sw_name}* supports the `Kitty keyboard protocol`_.")
    print()

    flags = [
        ("disambiguate", "Disambiguate escape codes"),
        ("report_events", "Report event types"),
        ("report_alternates", "Report alternate keys"),
        ("report_all_keys", "Report all keys as escape codes"),
        ("report_text", "Report associated text"),
    ]

    tabulated_flags = []
    for idx, (key, description) in enumerate(flags, start=1):
        value = kitty_kb.get(key, False)
        tabulated_flags.append({
            "#": idx,
            "Flag": description,
            "Key": f"``{key}``",
            "Supported": "Yes" if value else "No",
        })

    table_str = tabulate.tabulate(tabulated_flags, headers="keys", tablefmt="rst")
    print_datatable(table_str)

    if kitty_kb.get("supported_flags") != (1 << len(KITTY_KB_FLAG_KEYS)) - 1:
        # known instance: alacritty (stale state reporting, upstream fix rejected)
        print()
        print(".. note::")
        print()
        print("   Although this terminal supports the ``CSI ? u`` state request,")
        print("   it does not report all progressive enhancement modes as enabled")
        print("   when set.  This may reflect a bug in the terminal emulator; it")
        print("   may in fact support some or all of these modes.")
        print()

    print("Detection is performed by enabling all progressive enhancement")
    print("modes by set (``CSI = 31 ; 1 u``) and re-querying with ``CSI ? u``")
    print("to confirm which modes the terminal honors, before restoring its")
    print("original flags.")
    print()
    print('.. _`Kitty keyboard protocol`: '
          'https://sw.kovidgoyal.net/kitty/keyboard-protocol/')
    print()


def show_xtgettcap_results(sw_name, entry):
    """Display XTGETTCAP terminfo capability query results."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_xtgettcap")
    display_title("XTGETTCAP (Terminfo Capabilities)", 3)

    tr = entry["data"].get("terminal_results") or {}
    xtgettcap = tr.get("xtgettcap", {})

    if not xtgettcap.get("supported", False):
        print(f"*{sw_name}* does not support the ``XTGETTCAP`` sequence.")
        print()
        if tr.get("xtgettcap-bad-screenleak"):
            print(".. warning::")
            print("   This terminal fails to parse VT100 Mode DCS Sequences at"
                  " all, and displays XTGETTCAP queries as screen output")
            print()
        return

    capabilities = xtgettcap.get("capabilities", {})
    if not capabilities:
        print(f"*{sw_name}* supports the ``XTGETTCAP`` sequence but returned no capabilities.")
        print()
        return

    label, _score = _classify_xtgettcap(entry)
    qualifier = " (Full)" if label == "full" else " (Partial)"
    print(f"*{sw_name}* supports the ``XTGETTCAP`` sequence and reports "
          f"**{len(capabilities)}** terminfo capabilities{qualifier}.")
    print()

    from blessed._capabilities import XTGETTCAP_CAPABILITIES
    cap_descriptions = dict(XTGETTCAP_CAPABILITIES)

    tabulated_caps = []
    for idx, (key, value) in enumerate(sorted(capabilities.items()), start=1):
        display_value = _escape_terminfo_value(str(value))
        if len(display_value) > 60:
            display_value = display_value[:57] + "..."
        tabulated_caps.append({
            "#": idx,
            "Capability": key,
            "Description": cap_descriptions.get(key, ""),
            "Value": f"``{display_value}``" if display_value else "*(empty)*",
        })

    table_str = tabulate.tabulate(tabulated_caps, headers="keys", tablefmt="rst")
    print_datatable(table_str)

    print("The ``XTGETTCAP`` sequence (``DCS + q Pt ST``) allows applications to query")
    print("terminfo capabilities directly from the terminal emulator, rather than relying")
    print("on the system terminfo database.")
    print()


def show_text_sizing_results(sw_name, entry):
    """Display Text Sizing protocol (OSC 66) detection results."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_text_sizing")
    display_title("Text Sizing Protocol (OSC 66)", 3)

    tr = entry["data"].get("terminal_results") or {}
    text_sizing = tr.get("text_sizing", {})
    has_width = text_sizing.get("width", False)
    has_scale = text_sizing.get("scale", False)

    if not has_width and not has_scale:
        print(f"*{sw_name}* does not support the `Text Sizing protocol`_.")
        print()
        print('.. _`Text Sizing protocol`: '
              'https://sw.kovidgoyal.net/kitty/text-sizing-protocol/')
        print()
        return

    features = []
    if has_width:
        features.append("explicit width (``w``)")
    if has_scale:
        features.append("scale (``s``)")
    print(f"*{sw_name}* supports the `Text Sizing protocol`_: "
          f"{', '.join(features)}.")
    print()
    print("The Text Sizing protocol (OSC 66) allows terminal programs to display text")
    print("at different sizes and to explicitly specify the cell width of characters.")
    print("Detection is performed by measuring cursor movement after sending")
    print("``ESC ] 66 ; w=2 ; <space> BEL`` and ``ESC ] 66 ; s=2 ; <space> BEL``.")
    print()
    print("Because this terminal supports the `Text Sizing protocol`_, any application")
    print("can programmatically set the displayed cell width of any character.")
    print("This means that width errors for complex languages, emoji, variation")
    print("selectors (VS15, VS16), standalone regional indicators and Fitzpatrick")
    print("modifiers, and other problematic codepoints can be fully remediated")
    print("at the application level. For this reason, *{}* scores **100%** on the WIDE,".format(sw_name))
    print("LANG, ZWJ, VS16, VS15, SRI, SFZ, and RI width tests.")
    print()
    print('.. _`Text Sizing protocol`: '
          'https://sw.kovidgoyal.net/kitty/text-sizing-protocol/')
    print()


def _tofu_excluded_ranges():
    """
    Describe the ranges a default tofu sweep leaves out.

    Returns ``[(start, end, [block names], n_codepoints)]`` for each range of
    :data:`UNCOMMON_WIDE_RANGES` that holds testable codepoints, and the totals
    ``(n_excluded, n_all)`` over the whole table.
    """
    described, n_excluded, n_all = [], 0, 0
    per_range = {(start, end): {} for start, end in UNCOMMON_WIDE_RANGES}
    for _ver, ranges in TOFU_CODEPOINTS:
        for start, end, block_name in ranges:
            n_all += end - start + 1
            for bounds in per_range:
                low, high = max(start, bounds[0]), min(end, bounds[1])
                if low <= high:
                    per_range[bounds][block_name] = (
                        per_range[bounds].get(block_name, 0) + high - low + 1)
    for (start, end), blocks in per_range.items():
        n_codepoints = sum(blocks.values())
        if n_codepoints:
            described.append((start, end, sorted(blocks), n_codepoints))
            n_excluded += n_codepoints
    described.sort()
    return described, n_excluded, n_all


def _show_tofu_exclusions():
    """Print the note detailing what a default tofu sweep leaves out."""
    described, n_excluded, n_all = _tofu_excluded_ranges()
    print(".. note::")
    print()
    print("   These ranges are left out of the sweep, and of the count above: they are")
    print("   a tofu in all but a few specialist CJK and historic script fonts, and a")
    print("   font meant for terminal use is not worse for lacking them.  They account")
    print(f"   for {n_excluded:,} of the {n_all:,} codepoints that could be tested;"
          f" pass")
    print("   ``ucs-detect --include-uncommon-codepoints`` to sweep them as well.")
    print()
    for start, end, blocks, n_codepoints in described:
        print(f"   - ``U+{start:04X}``..``U+{end:04X}`` \u2014 {', '.join(blocks)}"
              f" ({n_codepoints:,} codepoints)")
    print()


def _tofu_protocol_phrase(protocol):
    """Return a sentence fragment naming the font glyph coverage *protocol*."""
    if protocol == "mintty":
        return "mintty's `Font Glyph Coverage Enquiry`_, ``OSC 7771``"
    if protocol == "glyph":
        return "the `Glyph Protocol`_ ``q`` verb, ``APC 25a1``"
    return f"``{protocol}``"


def _tofu_escape(codepoint):
    """Return *codepoint* as a python escape sequence, for :func:`show_wchar`."""
    if codepoint > 0xFFFF:
        return f"\\U{codepoint:08x}"
    return f"\\u{codepoint:04x}"


def show_tofu_results(sw_name, entry):
    """Display font glyph coverage ("tofu") detection and sweep results."""
    TOFU_BLOCK_CODEPOINT_LIMIT = 32
    TOFU_BLOCK_RANGE_LIMIT = 32
    display_inbound_hyperlink(entry["terminal_software_name"] + "_tofu")
    display_title("Tofu Detection", 3)

    tr = entry["data"].get("terminal_results") or {}
    tofu = tr.get("tofu") or {}
    protocol = tofu.get("protocol") if tofu.get("supported") else None

    print("A *tofu* is the \u25a1 ``U+25A1`` WHITE SQUARE placeholder box drawn in place of")
    print("a codepoint the terminal's font has no glyph for.  Two protocols allow a")
    print("program to ask which codepoints may 'tofu': mintty's `Font")
    print("Glyph Coverage Enquiry`_ and the `Glyph Protocol`_ implemented first by Rio.")
    print()

    if protocol is None:
        print(f"*{sw_name}* does **not** answer a font glyph coverage enquiry by either")
        print("protocol, 'tofus' cannot be determined by automatic code.")
        print()
        return

    print(f"*{sw_name}* answers by {_tofu_protocol_phrase(protocol)}.")
    print()
    print(f"- Protocol: **{protocol}**")
    print()

    print(".. warning::")
    print()
    print("   Both protocols answer about *single codepoints* only.  They are without")
    print("   support for grapheme clusters: ligatures, mark positioning, ``ZWJ`` joining,")
    print("   VS-15 and VS-16 presentation, contextual forms, etc. ")
    print()
    print("   What is measured below is a property of the *font* this terminal was")
    print("   configured with when tested, and not of the terminal emulator: it is")
    print("   reported, but is not scored. GNU's Unifont is sometimes configured for use.")
    print()

    tofu_results = entry["data"].get("test_results", {}).get("tofu_results") or {}
    if not tofu_results:
        print(f"No codepoint sweep was recorded for *{sw_name}*.")
        print()
        return

    ver, result = next(iter(tofu_results.items()))
    n_errors, n_total = result["n_errors"], result["n_total"]
    print(f"Every assigned codepoint of Unicode version {ver} that occupies a cell")
    # a sweep without --include-uncommon-codepoints skips the ranges the WIDE
    # test skips by default; data recorded before the option is a full sweep.
    if result.get("include_uncommon", True):
        print("of its own is tested, the ideographic extension and historic script")
        print("ranges that no general-purpose font carries included.")
    else:
        print("of its own is tested, less the ideographic extension and historic")
        print("script ranges that no general-purpose font is known to carry.")
    print()
    print(f"Tofus were detected for **{n_errors:,}** out of **{n_total:,}** codepoints")
    print("tested.")
    print()

    if not result.get("include_uncommon", True):
        _show_tofu_exclusions()

    if n_unknown := (result.get("n_unknown") or 0):
        print(f"{n_unknown:,} codepoints went unanswered by the terminal, and are assumed")
        print("renderable.")
        print()

    blocks = result.get("blocks") or {}
    if not blocks:
        print("No Unicode block holds a tofu: every codepoint tested has a glyph.")
        print()
        return

    offenders = sorted(blocks.items(), key=lambda kv: (-kv[1]["n_errors"], kv[0]))
    tabulated_blocks = [
        {
            "Block": make_outbound_hyperlink(block_name,
                                             sw_name + "_tofu_" + block_name),
            "Tofus": block["n_errors"],
            "Total": block["n_total"],
            "Pct": "{:0.1f}%".format(
                block["n_errors"] / block["n_total"] * 100
                if block["n_total"] else 0),
        }
        for block_name, block in offenders
    ]
    print(f"Tofus were found in the following {len(offenders)} Unicode blocks:")
    print()
    table_str = tabulate.tabulate(tabulated_blocks, headers="keys", tablefmt="rst")
    print_datatable(table_str)

    for block_name, block in offenders:
        display_inbound_hyperlink(sw_name + "_tofu_" + block_name)
        display_title(block_name, 4)
        n_block_errors, n_block_total = block["n_errors"], block["n_total"]
        if n_block_errors == n_block_total:
            print(f"All {n_block_total:,} codepoints tested of the *{block_name}* block")
            print(f"have no glyph in the font of *{sw_name}*.")
        else:
            print(f"{n_block_errors:,} of the {n_block_total:,} codepoints tested of the")
            print(f"*{block_name}* block have no glyph in the font of *{sw_name}*.")
        print()

        codepoint_ranges = block["codepoint_ranges"]
        if n_block_errors > TOFU_BLOCK_CODEPOINT_LIMIT:
            # a table of thousands of rows helps nobody, and there may be
            # hundreds of such blocks: name the ranges, they say as much.
            for start, end in codepoint_ranges[:TOFU_BLOCK_RANGE_LIMIT]:
                if start == end:
                    print(f"- {make_unicode_codepoint(chr(start))}")
                else:
                    print(f"- {make_unicode_codepoint(chr(start))} through"
                          f" {make_unicode_codepoint(chr(end))},"
                          f" {end - start + 1:,} codepoints")
            if len(codepoint_ranges) > TOFU_BLOCK_RANGE_LIMIT:
                print(f"- \u2026 and {len(codepoint_ranges) - TOFU_BLOCK_RANGE_LIMIT:,}"
                      " further ranges")
            print()
            continue

        show_wchar("".join(_tofu_escape(codepoint)
                           for start, end in codepoint_ranges
                           for codepoint in range(start, end + 1)))


def show_truecolor_results(sw_name, entry):
    """Display truecolor detection method results."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_truecolor")
    display_title("Truecolor Support", 3)

    tr = entry["data"].get("terminal_results") or {}
    env = entry["data"].get("environment") or {}

    xt_has, dq_has, ct_has = _detect_truecolor_methods(entry)
    ncolors = tr.get("number_of_colors", 0)

    if xt_has or dq_has or ct_has:
        print(f"*{sw_name}* supports 24-bit truecolor, detectable via:")
    elif ncolors == 16777216:
        print(f"*{sw_name}* supports 24-bit truecolor")
        print(f"({ncolors} colors), but is **not detectable** by")
        print("XTGETTCAP, DECRQSS, or COLORTERM methods.")
    else:
        print(f"*{sw_name}* does not support 24-bit truecolor.")
        print(f"(Reports {ncolors} colors.)")
    print()

    if tr:
        xt_status = "yes (RGB)" if xt_has else "no"
        dq_probe = tr.get("decrqss_truecolor_probe")
        if dq_probe is True:
            dq_status = "yes (probe)"
        elif dq_probe is False:
            dq_status = "no"
        else:
            dq_status = "N/A (untested)"
        ct_status = "yes (truecolor)" if ct_has else (
            env.get("COLORTERM", "unset") if "COLORTERM" in (env or {}) else "N/A")
        print(f"- XTGETTCAP (RGB capability): **{xt_status}**")
        print(f"- DECRQSS (truecolor probe): **{dq_status}**")
        print(f"- COLORTERM: **{ct_status}**")
    print()

    if ct_has and not xt_has and not dq_has:
        print(".. warning::")
        print()
        print("   COLORTERM is an environment variable, not a terminal query."
              " It is not forwarded over SSH without ``SendEnv`` / ``AcceptEnv``"
              " configuration, so detection via COLORTERM alone may be unreliable"
              " on remote hosts.")
        print()


def show_osc52_results(sw_name, entry):
    """Display OSC 52 clipboard detection method results."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_osc52")
    display_title("OSC 52 Clipboard Support", 3)

    tr = entry["data"].get("terminal_results") or {}

    osc52 = tr.get("osc52_clipboard", False)
    methods = tr.get("osc52_detection") or {}
    da1_has = methods.get("da1_extension_52", False)
    ms_has = methods.get("xtgettcap_ms", False)

    if osc52:
        parts = []
        if da1_has:
            parts.append("DA1 extension 52")
        if ms_has:
            parts.append("XTGETTCAP Ms")
        method_str = " + ".join(parts) if parts else "unknown method"
        print(f"*{sw_name}* supports OSC 52 clipboard operations")
        print(f"(detected via {method_str}).")
    else:
        print(f"*{sw_name}* does **not** advertise OSC 52 clipboard support")
        print("via DA1 extension 52 or XTGETTCAP Ms.")
    print()

    if tr:
        print(f"- DA1 extension 52: **{'yes' if da1_has else 'no'}**")
        print(f"- XTGETTCAP Ms: **{'yes' if ms_has else 'no'}**")
    print()


def _show_tn_line(tr):
    """Print XTGETTCAP TN status line, if available."""
    xt = tr.get("xtgettcap", {})
    if xt.get("supported"):
        tn_val = xt.get("capabilities", {}).get("TN", "")
        if tn_val:
            print(f"- XTGETTCAP TN: **yes** ({tn_val})")
            return
    print("- XTGETTCAP TN: **no**")


def show_id_results(sw_name, entry, terminal_mixins):
    """Display terminal identification method results with raw values."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_identification")
    display_title("Terminal Identification", 3)

    tr = entry["data"].get("terminal_results") or {}
    env = entry["data"].get("environment") or {}

    xt_has, tn_unique, tp_has, term_has, enq_has = _detect_id_methods(entry)
    cfg = terminal_mixins.get(sw_name.lower(), {})
    is_sub = bool((cfg.get("launch") or {}).get("subterminal"))

    sw_name_final = entry["data"].get("software_name", "")
    sw_version = entry["data"].get("software_version", "")
    xtversion_raw = tr.get("xtversion_raw", "")
    term_program = env.get("TERM_PROGRAM", "")
    term = env.get("TERM", "")

    if xt_has or tn_unique or tp_has or enq_has:
        methods = []
        if xt_has:
            methods.append("XTVERSION")
        if tn_unique:
            methods.append("XTGETTCAP TN")
        if enq_has and not xt_has and not tn_unique:
            methods.append("ENQ")
        if tp_has and not xt_has and not tn_unique and not enq_has:
            methods.append("TERM_PROGRAM")
        method_label = " + ".join(methods)
        print(f"*{sw_name}* is identified as **{sw_name_final}**")
        if sw_version:
            print(f"version **{sw_version}**")
        print(f"(detected via {method_label}).")
    else:
        print(f"*{sw_name}* could not be identified via XTVERSION,")
        print("XTGETTCAP TN, ENQ, or TERM_PROGRAM.")
    print()

    if xtversion_raw:
        print(f"- XTVERSION (raw): **{xtversion_raw}**")
    elif tr.get("software_method") == "XTVERSION":
        print("- XTVERSION (raw): (not recorded for this run)")
    print(f"- XTVERSION: **{'yes' if xt_has else 'no'}**")

    _show_tn_line(tr)
    print(f"- ENQ: **{'yes' if enq_has else 'no'}**")
    if term_program:
        print(f"- TERM_PROGRAM: **yes** ({term_program})")
    else:
        print(f"- TERM_PROGRAM: **{'yes' if tp_has else 'no'}**")
    suffix = " (inherited from host terminal)" if is_sub and term else ""
    print(f"- TERM: **{'yes' if term_has else 'no'}**"
          f"{f' ({term})' if term else ''}{suffix}")
    print()

    if tp_has and not xt_has and not tn_unique and not is_sub:
        print(".. warning::")
        print()
        print("   TERM_PROGRAM is an environment variable, not a terminal"
              " query. It is not forwarded over SSH without ``SendEnv`` /"
              " ``AcceptEnv`` configuration, so identification via"
              " TERM_PROGRAM alone may be unreliable on remote hosts.")
        print()


def show_sri_results(sw_name, entry):
    """Display standalone Regional Indicator results."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_sri")
    display_title("Standalone Regional Indicator support", 3)
    sri_results = entry["data"]["test_results"].get("sri_results") or {}
    if not sri_results:
        print(f"Standalone Regional Indicator results for *{sw_name}* are not available.")
        print()
        return
    result = next(iter(sri_results.values()))
    n_errors = result["n_errors"]
    n_total = result["n_total"]
    pct = ((n_total - n_errors) / n_total * 100) if n_total else 0
    print(
        f"Standalone Regional Indicator support of *{sw_name}* "
        f"is **{pct:0.1f}%** ({n_errors} errors "
        f"of {n_total} codepoints tested)."
    )
    print()
    if n_errors > 0 and result.get("failed_codepoints"):
        fail_record = find_best_failure(result["failed_codepoints"])
        show_record_failure(
            sw_name, "of a standalone Regional Indicator,", fail_record,
            category="sri",
        )


def show_sfz_results(sw_name, entry):
    """Display standalone Fitzpatrick skin tone modifier results."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_sfz")
    display_title("Standalone Fitzpatrick modifier support", 3)
    sfz_results = entry["data"]["test_results"].get("sfz_results") or {}
    if not sfz_results:
        print(f"Standalone Fitzpatrick modifier results for *{sw_name}* are not available.")
        print()
        return
    result = next(iter(sfz_results.values()))
    n_errors = result["n_errors"]
    n_total = result["n_total"]
    pct = ((n_total - n_errors) / n_total * 100) if n_total else 0
    print(
        f"Standalone Fitzpatrick skin tone modifier support of *{sw_name}* "
        f"is **{pct:0.1f}%** ({n_errors} errors "
        f"of {n_total} codepoints tested)."
    )
    print()
    if n_errors > 0 and result.get("failed_codepoints"):
        fail_record = find_best_failure(result["failed_codepoints"])
        show_record_failure(
            sw_name, "of a standalone Fitzpatrick modifier,", fail_record,
            category="sfz",
        )


def show_ri_results(sw_name, entry):
    """Display Regional Indicator flag sequence results."""
    display_inbound_hyperlink(entry["terminal_software_name"] + "_ri")
    display_title("Regional Indicator flag sequence support", 3)
    ri_results = entry["data"]["test_results"].get("ri_results") or {}
    if not ri_results:
        print(f"Regional Indicator flag sequence results for *{sw_name}* are not available.")
        print()
        return
    result = next(iter(ri_results.values()))
    n_errors = result["n_errors"]
    n_total = result["n_total"]
    pct = ((n_total - n_errors) / n_total * 100) if n_total else 0
    print(
        f"Regional Indicator flag sequence support of *{sw_name}* "
        f"is **{pct:0.1f}%** ({n_errors} errors "
        f"of {n_total} sequences tested)."
    )
    print()
    if n_errors > 0 and result.get("failed_codepoints"):
        fail_record = find_best_failure(result["failed_codepoints"])
        show_record_failure(
            sw_name, "of a Regional Indicator flag sequence,", fail_record,
            category="ri",
        )


def show_reproduce_command(sw_name, entry):
    """
    Display command to reproduce the test results.
    """
    display_inbound_hyperlink(entry["terminal_software_name"] + "_reproduce")
    display_title("Reproduction", 3)

    # Get session arguments to reconstruct the command
    _session_args = entry["data"].get("session_arguments", {})  # noqa: F841
    fname = entry["fname"]

    print(f"To reproduce these results for *{sw_name}*, install and run ucs-detect_")
    print("with the following commands::")
    print()
    print(f"    uvx ucs-detect --rerun data/{fname}")

    print()


def show_time_elapsed_results(sw_name, entry):
    """
    Display test performance results.
    """
    display_inbound_hyperlink(entry["terminal_software_name"] + "_time")
    display_inbound_hyperlink(entry["terminal_software_name"] + "_resources")
    display_title("Test Performance", 3)

    rp = (entry["data"].get("resource_profile") or {})
    elapsed_data = rp.get("elapsed_s", [])
    cpu_data = rp.get("cpu_pct", [])
    rss_data = rp.get("rss_mb", [])

    if not elapsed_data or not cpu_data or not rss_data:
        print(f"Performance data for *{sw_name}* is not available.")
        print()
        return

    duration = elapsed_data[-1]
    mean_cpu = sum(cpu_data) / len(cpu_data)
    mean_rss = sum(rss_data) / len(rss_data)
    resource_score = entry["data"].get("resource_score", None)

    print(f"The test suite completed in **{duration:.2f} seconds** "
          f"({int(duration)}s).")
    print()
    if resource_score is not None:
        print(f"- **Resources Score**: {resource_score:.1f}/100")
    print(f"- **Mean CPU**: {mean_cpu:.1f}%")
    print(f"- **Mean RSS**: {mean_rss:.1f} MB")
    print(f"- **Total time**: {duration:.1f}s")

    safe = safe_name(sw_name)

    cpu_graph = f"../_static/profiles/{safe}_cpu.png"
    rss_graph = f"../_static/profiles/{safe}_rss.png"

    print()
    print(f".. figure:: {cpu_graph}")
    print("   :alt: CPU usage over time")
    print(f"   :width: {GRAPH_WIDTH_PX}px")
    print()
    print(f"   CPU usage during test execution for *{sw_name}*.")
    print()
    print(f".. figure:: {rss_graph}")
    print("   :alt: RSS memory over time")
    print(f"   :width: {GRAPH_WIDTH_PX}px")
    print()
    print(f"   RSS memory usage during test execution for *{sw_name}*.")
    print()

    time_graph = f"../_static/profiles/{safe}_time.png"
    cpu_vs_time_graph = f"../_static/profiles/{safe}_cpu_vs_time.png"

    if os.path.exists(os.path.join(_ROOT, "docs", "_static", "profiles", f"{safe}_time.png")):
        print(f".. figure:: {time_graph}")
        print("   :alt: Duration comparison")
        print(f"   :width: {GRAPH_WIDTH_PX}px")
        print()
        print(f"   Test duration for *{sw_name}* compared to all other terminals.")
        print()
    if os.path.exists(os.path.join(_ROOT, "docs", "_static", "profiles", f"{safe}_cpu_vs_time.png")):
        print(f".. figure:: {cpu_vs_time_graph}")
        print("   :alt: CPU % vs Duration")
        print(f"   :width: {GRAPH_WIDTH_PX}px")
        print()
        print(f"   CPU % vs duration trade-off for *{sw_name}*.")
        print()


def show_record_failure(sw_name, whatis, fail_record, test_type=None, category=None):
    """Display details of a test failure record for a terminal."""
    num_bars = "1234567890" * ((fail_record.get("measured_by_wcwidth", 0) // 10) + 1)
    ruler = num_bars[: fail_record.get("measured_by_wcwidth", 0)]
    wchars = fail_record.get("wchar", fail_record.get("wchars"))
    assert wchars
    as_printf_hex = make_printf_hex(decode_wchars(wchars))
    print(f"Sequence {whatis} from midpoint of alignment failure records:")
    print()
    show_wchar(wchars)
    print()
    print("- Shell test using `printf(1)`_, ``'|'`` should align in output::")
    print()
    print(rf'        $ printf "{as_printf_hex}|\\n{ruler}|\\n"')
    print(f'        {bytes(wchars, "utf8").decode("unicode-escape")}|')
    print(f"        {ruler}|")
    print()

    # Example file cross-reference
    if category:
        decoded = decode_wchars(wchars)
        measured_width = fail_record.get('measured_by_wcwidth')
        info = _example_file_link(decoded, category, measured_width)
        if info:
            basename, lineno, url = info
            print()
            print(f"- See Line {lineno} of `{basename} <{url}>`_"
                  " for this sequence in the example file.")

    # Screenshot reference
    if category:
        safe_sw = safe_name(sw_name)
        screenshot_path = f"../_static/screenshots/{safe_sw}/{category}.png"
        abs_screenshot = os.path.join(_ROOT, "docs", "_static", "screenshots",
                                      safe_sw, f"{category}.png")
        if not os.path.exists(abs_screenshot):
            print(f"warning: Screenshot missing: {abs_screenshot}",
                  file=sys.stderr)
        else:
            print()
            print("Screenshot:")
            print()
            print(f".. image:: {screenshot_path}")
            print("   :alt: Terminal screenshot of the rendering discrepancy")
            w, h = Image.open(abs_screenshot).size
            print(f"   :width: {w}px")
            print(f"   :height: {h}px")
            print()

    if fail_record.get("delta_ypos", 0) != 0:
        print(f"- Cursor Y-Position moved {fail_record['delta_ypos']} rows"
              " where no movement is expected.")
    elif "measured_by_terminal" in fail_record and (
            fail_record.get("measured_by_wcwidth", 0) != fail_record["measured_by_terminal"]):
        print("- python `wcwidth.wcswidth()`_ measures width"
              f" {fail_record['measured_by_wcwidth']},")
        print(f"  while *{sw_name}* measures width"
              f" {fail_record['measured_by_terminal']}.")
    print()


if __name__ == "__main__":
    main()
