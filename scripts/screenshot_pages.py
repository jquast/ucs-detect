"""Group terminal screenshots by test type and render one RST page per type."""

from __future__ import annotations

import os
from pathlib import Path

from PIL import Image

from ucs_detect.accessories import safe_name

#: Screenshot groups, in display order: page label and terminal page anchor suffix.
SCREENSHOT_GROUPS = (
    ("Score", "scores"),
    ("WIDE", "wide"),
    ("NARROW", "narrow"),
    ("ZWJ", "zwj"),
    ("LANG", "lang"),
    ("VS16", "vs16"),
    ("VS15", "vs15"),
    ("SRI", "sri"),
    ("SFZ", "sfz"),
    ("RI", "ri"),
    ("SPILL", "spillover"),
)

#: Groups whose images live in a ``_static`` subdirectory of their own, keyed to
#: that directory, rather than in ``screenshots/<terminal>/``.
STATIC_SUBDIRS = {"Score": "plots"}

#: File name suffix of the score comparison plot of a terminal.
SCORE_PLOT_SUFFIX = "_scores_scaled.png"

#: Hyperlinked phrase used by the page intros.
WCWIDTH_SPEC_REF = "`wcwidth specification`_"

#: Target of the ``wcwidth specification`` hyperlink used by the page intros.
WCWIDTH_SPEC_URL = "https://wcwidth.readthedocs.io/en/latest/specs.html"


def _spec_line(expansion):
    return (f"{expansion}: Screenshots when terminals disagree with "
            f"python {WCWIDTH_SPEC_REF}.")


#: One-line introduction of each page, keyed by page label.
GROUP_INTROS = {
    "Score": "Final scaled score of each terminal against every other.",
    "WIDE": _spec_line("Wide (2-cell) East Asian characters"),
    "NARROW": _spec_line("Narrow (1-cell) characters"),
    "ZWJ": _spec_line("Zero-Width Joiner emoji sequences"),
    "LANG": _spec_line("Language scripts"),
    "VS16": _spec_line("Variation Selector-16 emoji made wide"),
    "VS15": _spec_line("Variation Selector-15 emoji made narrow"),
    "SRI": _spec_line("Standalone Regional Indicator symbols"),
    "SFZ": _spec_line("Standalone Fitzpatrick skin tone modifiers"),
    "RI": _spec_line("Regional Indicator flag sequences"),
    "SPILL": _spec_line("Spillover, pixels painted outside the cursor advance"),
}

#: Maximum rendered width of a screenshot on a Screenshots page.
SCREENSHOT_PAGE_WIDTH_PX = 720


def screenshot_image_names(screenshots_dir, safe_sw, label):
    """Return the screenshot file names of *label* recorded for *safe_sw*."""
    directory = Path(screenshots_dir) / safe_sw
    try:
        names = sorted(os.listdir(directory))
    except OSError:
        return []
    if label == "LANG":
        return [name for name in names
                if name.startswith("lang_") and name.endswith(".png")]
    if label == "SPILL":
        return [name for name in names
                if "spillover_" in name and name.endswith(".gif")]
    return [name for name in names if name == f"{label.lower()}.png"]


def score_plot_names(plots_dir, link):
    """Return the score comparison plot file name of the terminal linked as *link*."""
    name = f"{link}{SCORE_PLOT_SUFFIX}"
    return [name] if (Path(plots_dir) / name).is_file() else []


def collect_screenshot_groups(score_table, screenshots_dir, plots_dir, link_name):
    """Return ``(label, [(sw_name, image_names), ...])`` for non-empty groups."""
    groups = []
    for label, _anchor in SCREENSHOT_GROUPS:
        entries = []
        seen = set()
        for entry in score_table:
            sw_name = entry["terminal_software_name"]
            safe_sw = safe_name(sw_name)
            if safe_sw in seen:
                continue
            seen.add(safe_sw)
            if label in STATIC_SUBDIRS:
                image_names = score_plot_names(plots_dir, link_name(sw_name))
            else:
                image_names = screenshot_image_names(screenshots_dir, safe_sw, label)
            if image_names:
                entries.append((sw_name, image_names))
        if entries:
            entries.sort(key=lambda item: item[0].casefold())
            groups.append((label, entries))
    return groups


def screenshot_toc_lines(groups):
    """Return RST lines for the Screenshots section toctree."""
    if not groups:
        return []
    lines = ["Screenshots", "-----------", "", ".. toctree::", "   :maxdepth: 1", ""]
    lines.extend(f"   screenshots/{label.lower()}" for label, _entries in groups)
    lines.append("")
    return lines


def _image_path(label, screenshots_dir, plots_dir, safe_sw, filename):
    if label in STATIC_SUBDIRS:
        return Path(plots_dir) / filename
    return Path(screenshots_dir) / safe_sw / filename


def _image_reference(label, safe_sw, filename):
    if label in STATIC_SUBDIRS:
        return f"../_static/{STATIC_SUBDIRS[label]}/{filename}"
    return f"../_static/screenshots/{safe_sw}/{filename}"


def _image_alt(label, sw_name):
    kind = "comparison plot" if label in STATIC_SUBDIRS else "screenshot"
    return f"{label} {kind} of {sw_name}"


def write_screenshot_pages(groups, screenshots_dir, plots_dir, pages_dir, link_name):
    """Write one Screenshots page per group into *pages_dir*."""
    pages = Path(pages_dir)
    pages.mkdir(parents=True, exist_ok=True)
    known = {label.lower() for label, _anchor in SCREENSHOT_GROUPS}
    for stale in pages.glob("*.rst"):
        if stale.stem in known:
            stale.unlink()

    anchors = dict(SCREENSHOT_GROUPS)
    for label, entries in groups:
        intro = GROUP_INTROS[label]
        lines = [label, "-" * len(label), "", intro, ""]
        if WCWIDTH_SPEC_REF in intro:
            lines.extend([f".. _`wcwidth specification`: {WCWIDTH_SPEC_URL}", ""])
        for sw_name, image_names in entries:
            safe_sw = safe_name(sw_name)
            target = f"{link_name(sw_name)}_{anchors[label]}"
            heading = f":ref:`{sw_name} <{target}>`"
            lines.append(heading)
            lines.append("~" * len(heading))
            lines.append("")
            for filename in image_names:
                image_path = _image_path(label, screenshots_dir, plots_dir,
                                        safe_sw, filename)
                with Image.open(image_path) as image:
                    width, _height = image.size
                lines.append(
                    f".. figure:: {_image_reference(label, safe_sw, filename)}")
                lines.append(f"   :alt: {_image_alt(label, sw_name)}")
                lines.append(f"   :width: {min(width, SCREENSHOT_PAGE_WIDTH_PX)}px")
                lines.append("   :loading: lazy")
                lines.append("")
        (pages / f"{label.lower()}.rst").write_text(
            "\n".join(lines), encoding="utf-8")
