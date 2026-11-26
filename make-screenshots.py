#!/usr/bin/env python3
"""Generate terminal screenshots, color measurements, spillover, and BiDi evidence.

Each terminal is started once.  The ``all`` stage runs
``scripts/make_screenshot.py`` in batch mode, then ``scripts/font_test.py``,
``scripts/color_test.py``, ``scripts/bidi_scan.py``, and
``scripts/spillover_scan.py`` in the same launch.  The ``screenshots``,
``colors``, ``bidi``, and ``spillover`` stages run one command alone.  The
screenshot command writes one PNG per width failure.  The color command paints
the 16 configurable colors and records their RGB values.  The spillover command
renders contested graphemes over truecolor blocks, captures each page, and
records cell overflow counts.  The BiDi command requests a right to left
character path, captures the probe page, and records where the glyphs landed.

All stages share terminal discovery, launch, window lookup, key injection,
and Docker orchestration through :mod:`ucs_detect.stage`.
"""
import argparse
import atexit
import functools
import json
import os
import platform
import shutil
import sys
import tempfile
import time
from pathlib import Path

from ucs_detect import fonts, imaging, stage, spillover
from ucs_detect.accessories import (
    _IS_DOCKER,
    find_best_failure,
    get_data_dir,
    get_launch_config,
    load_document,
    load_mixins,
    safe_name,
)
from ucs_detect.spillover import contested_graphemes
from ucs_detect.tasks import default_workers

PROJECT_DIR = stage.PROJECT_DIR
DATA_DIR = get_data_dir()
SCREENSHOTS_DIR = PROJECT_DIR / "docs" / "_static" / "screenshots"

#: Seconds allowed for the font test in one terminal launch.
FONT_TEST_TIMEOUT = 120

#: Seconds allowed for the color measurement in one terminal launch.
COLOR_TEST_TIMEOUT = 240

#: Seconds allowed for the BiDi probe in one terminal launch.
BIDI_TIMEOUT = 120

# Categories that have failed_codepoints in their results
_CATEGORY_YAML_KEYS = [
    ("unicode_wide_results", "wide"),
    ("narrow_results", "narrow"),
    ("emoji_zwj_results", "zwj"),
    ("emoji_vs16_results", "vs16"),
    ("emoji_vs15_results", "vs15"),
    ("sri_results", "sri"),
    ("sfz_results", "sfz"),
    ("ri_results", "ri"),
]


@functools.lru_cache(maxsize=None)
def terminal_document(yaml_path):
    """Return the parsed terminal data YAML, read once per process."""
    return load_document(yaml_path)


@functools.lru_cache(maxsize=None)
def extract_failures(yaml_path):
    """Extract all failure records from a YAML data file."""
    data = terminal_document(yaml_path)
    tr = data.get("test_results", {})
    failures = []

    for yaml_key, cat_name in _CATEGORY_YAML_KEYS:
        if not (cat_data := (tr.get(yaml_key) or {})):
            continue
        for _ver, result in cat_data.items():
            fps = result.get("failed_codepoints", [])
            if not fps:
                continue
            if (best := find_best_failure(fps)) is None:
                continue
            if (wchars := best.get("wchar") or best.get("wchars")) is None:
                continue
            failures.append((
                cat_name,
                wchars,
                best.get("measured_by_wcwidth", 0),
                best.get("measured_by_terminal", 0),
            ))
            break  # only first version

    lang_results = tr.get("language_results") or {}
    for lang_name, lang_data in sorted(lang_results.items()):
        if not (failed := lang_data.get("failed", [])):
            continue
        if (best := failed[0]) is None:
            continue
        if (wchars := best.get("wchar") or best.get("wchars")) is None:
            continue
        failures.append((
            f"lang_{safe_name(lang_name)}",
            wchars,
            best.get("measured_by_wcwidth", 0),
            best.get("measured_by_terminal", 0),
        ))

    return failures, data.get("software_version", "")


def effective_software_name(job, software_version):
    """Return the name used for wcwidth ``term_program`` correction lookup."""
    if software_version and "VTE" in software_version:
        return "vte"
    return job.software_name


def screenshot_records(job):
    """Return batch records for the screenshot stage of *job*."""
    failures, software_version = extract_failures(job.yaml_path)
    if not failures:
        return []
    directory = SCREENSHOTS_DIR / safe_name(job.display_name)
    directory.mkdir(parents=True, exist_ok=True)
    name = effective_software_name(job, software_version)
    title_suffix = stage.unique_title('ucs-shot', job.software_name)
    records = []
    for category, wchars, expected_width, measured_width in failures:
        records.append({
            "wchars": wchars,
            "expected_width": expected_width,
            "measured_width": measured_width,
            "output": str(directory / f"{category}.png"),
            "title": f"{title_suffix}-{category}",
            "software_name": name,
        })
    return records


def remove_stale(directory, pattern, keep_prefix=()):
    """Remove files matching *pattern*, skipping names in *keep_prefix*."""
    if not directory.is_dir():
        return
    for stale in directory.glob(pattern):
        if any(stale.name.startswith(prefix) for prefix in keep_prefix):
            continue
        stale.unlink()


def remove_stale_screenshots(job):
    """Remove width failure screenshots, keeping color and spillover evidence."""
    directory = SCREENSHOTS_DIR / safe_name(job.display_name)
    remove_stale(directory, "*.png", keep_prefix=("spillover_", "colors-"))
    remove_stale(directory, "*.xwd")


def font_test_arguments(job, window_id_path):
    """Return the font test argv for *job*."""
    capture = (PROJECT_DIR / "fonts" / "captures"
               / f"{safe_name(job.software_name)}.png")
    return [
        sys.executable, "scripts/font_test.py",
        "--yaml", str(job.yaml_path.relative_to(PROJECT_DIR)),
        "--title", stage.unique_title('ucs-font', job.software_name),
        "--window-id-file", str(window_id_path),
        "--capture", str(capture),
    ] + capture_delay_arguments(job)


def cursor_arguments(job):
    """Return the pointer guard flag for *job*, empty when the terminal has none."""
    rows = job.launch_cfg.get("cursor_center_rows") or 0
    if not rows:
        return []
    return ["--cursor-center-rows", str(rows)]


def capture_delay_arguments(job):
    """Return the renderer pause flag for *job*, empty when it needs none."""
    delay = job.launch_cfg.get("screenshot_delay_ms") or 0
    if not delay:
        return []
    return ["--capture-delay-ms", str(delay)]


def draw_delay_arguments(args):
    """Return the page draw pause flag for *args*, empty when not overridden."""
    if args.draw_delay is None:
        return []
    return ["--draw-delay", str(args.draw_delay)]


def color_test_arguments(job, window_id_path):
    """Return the color measurement argv for *job*."""
    capture = SCREENSHOTS_DIR / safe_name(job.display_name)
    capture.mkdir(parents=True, exist_ok=True)
    return [
        sys.executable, "scripts/color_test.py",
        "--yaml", str(job.yaml_path.relative_to(PROJECT_DIR)),
        "--title", stage.unique_title('ucs-color', job.software_name),
        "--window-id-file", str(window_id_path),
        "--capture-dir", str(capture),
    ] + cursor_arguments(job) + capture_delay_arguments(job)


def build_screenshot_script(temp_dir, job, records, log_path=None,
                            status_path=None, workers=1):
    """Return the script path and sentinel path for the screenshot stage."""
    safe = safe_name(job.software_name)
    batch_path = temp_dir / f"batch-{safe}.json"
    batch_path.write_text(json.dumps(records))
    script_path = temp_dir / f"screenshot-{safe}.sh"
    sentinel_path = temp_dir / f"screenshot-{safe}.rc"
    window_id_path = temp_dir / f"screenshot-{safe}.id"
    commands = []
    if records:
        command = [
            sys.executable, "scripts/make_screenshot.py",
            "--batch", str(batch_path),
            "--window-id-file", str(window_id_path),
            "--workers", str(workers)] + capture_delay_arguments(job)
        if status_path is not None:
            command.extend(["--status-file", str(status_path)])
        commands.append(command)
    commands.append(font_test_arguments(job, window_id_path))
    stage.write_commands(
        script_path, commands, sentinel_path, stop_on_error=False,
        log_path=log_path)
    return script_path, sentinel_path, window_id_path


def verify_font_test_output(job):
    """Return an error string when the YAML font test section is missing."""
    section = terminal_document(job.yaml_path).get("font_test_results")
    if not section:
        return "YAML has no font_test_results section"
    if not section.get("ascii"):
        return "font test recorded no ASCII rows"
    return None


def verify_color_output(job):
    """Return an error string when the YAML color section is incomplete."""
    section = terminal_document(job.yaml_path).get("color_results")
    if not section:
        return "YAML has no color_results section"
    colors = (section.get("sixteen") or {}).get("colors") or []
    if len(colors) != 16:
        return f"color test recorded {len(colors)} of 16 colors"
    return None


def missing_outputs(records):
    """Return the names of records whose output is absent or empty."""
    return [Path(record["output"]).name for record in records
            if not Path(record["output"]).is_file()
            or Path(record["output"]).stat().st_size == 0]


def read_image_errors(status_path):
    """Return the recoverable image errors recorded by the inner script."""
    try:
        payload = json.loads(status_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    return payload.get("errors") or []


def collect_image_errors(status_path, records):
    """Return the image errors of one launch, including outputs never written."""
    errors = read_image_errors(status_path)
    reported = {Path(error.get("output") or "").name for error in errors}
    for name in missing_outputs(records):
        if name not in reported:
            errors.append({"output": name, "error": "not written"})
    return errors


def run_screenshot_stage(job, host_cfg, args, temp_dir):
    """Run the screenshot stage for one terminal."""
    records = screenshot_records(job)
    remove_stale_screenshots(job)
    stderr_path = temp_dir / f"screenshot-{safe_name(job.software_name)}.log"
    status_path = temp_dir / f"screenshot-{safe_name(job.software_name)}.status"
    script_path, sentinel_path, window_id_path = build_screenshot_script(
        temp_dir, job, records, log_path=stderr_path, status_path=status_path,
        workers=args.workers)
    exit_code, message = stage.run_stage(
        job.launch_cfg, host_cfg, script_path, sentinel_path, stderr_path,
        window_id_path,
        stage.scaled_timeout(args.timeout, len(records)) + FONT_TEST_TIMEOUT,
        max_window_size=imaging.SCREENSHOT_MAX_SIZE)
    terminal_document.cache_clear()
    errors = collect_image_errors(status_path, records)
    if exit_code != 0 and not status_path.is_file():
        return message, errors
    return verify_font_test_output(job), errors


def evidence_directory(job, args):
    """Return the absolute spillover evidence directory for *job*, or None."""
    if not args.evidence_dir:
        return None
    base = Path(args.evidence_dir).expanduser()
    if not base.is_absolute():
        base = PROJECT_DIR / base
    return base / safe_name(job.display_name)


def spillover_script_arguments(job, args, window_id_path, workers=1):
    """Return the spillover scan argv for *job*."""
    directory = evidence_directory(job, args)
    arguments = [
        sys.executable, "scripts/spillover_scan.py",
        "--yaml", str(job.yaml_path.relative_to(PROJECT_DIR)),
        "--title", stage.unique_title('ucs-spillover', job.software_name),
        "--window-id-file", str(window_id_path),
        "--workers", str(workers),
    ]
    if args.limit:
        arguments.extend(["--limit", str(args.limit)])
    if directory is not None:
        arguments.extend(["--evidence-dir", str(directory)])
    if not job.launch_cfg.get("spillover_rtl", True):
        arguments.append("--exclude-rtl")
    return (arguments + cursor_arguments(job) + capture_delay_arguments(job)
            + draw_delay_arguments(args))


def build_spillover_script(temp_dir, job, args, log_path=None, workers=1):
    """Return the script path, sentinel path, and window id path."""
    safe = safe_name(job.software_name)
    script_path = temp_dir / f"spillover-{safe}.sh"
    sentinel_path = temp_dir / f"spillover-{safe}.rc"
    window_id_path = temp_dir / f"spillover-{safe}.id"
    stage.write_script(
        script_path,
        spillover_script_arguments(job, args, window_id_path, workers),
        sentinel_path, log_path=log_path)
    return script_path, sentinel_path, window_id_path


def bidi_script_arguments(job, args, window_id_path):
    """Return the BiDi scan argv for *job*."""
    arguments = [
        sys.executable, "scripts/bidi_scan.py",
        "--yaml", str(job.yaml_path.relative_to(PROJECT_DIR)),
        "--title", stage.unique_title('ucs-bidi', job.software_name),
        "--window-id-file", str(window_id_path),
    ]
    return arguments + cursor_arguments(job) + capture_delay_arguments(job)


def run_bidi_stage(job, host_cfg, args, temp_dir):
    """Run the BiDi probe for one terminal, returning an error or None."""
    safe = safe_name(job.software_name)
    stderr_path = temp_dir / f"bidi-{safe}.log"
    script_path = temp_dir / f"bidi-{safe}.sh"
    sentinel_path = temp_dir / f"bidi-{safe}.rc"
    window_id_path = temp_dir / f"bidi-{safe}.id"
    stage.write_script(
        script_path, bidi_script_arguments(job, args, window_id_path),
        sentinel_path, log_path=stderr_path)
    exit_code, message = stage.run_stage(
        job.launch_cfg, host_cfg, script_path, sentinel_path, stderr_path,
        window_id_path, BIDI_TIMEOUT)
    terminal_document.cache_clear()
    if exit_code != 0:
        return message, []
    section = terminal_document(job.yaml_path).get("bidi_results")
    if not section:
        return "YAML has no bidi_results section", []
    return None, []


def build_combined_script(temp_dir, job, args, records, run_spillover,
                          run_font=True, run_colors=True, run_bidi=True,
                          log_path=None, status_path=None, workers=1):
    """Return one script that runs every stage of *job* in one launch."""
    safe = safe_name(job.software_name)
    script_path = temp_dir / f"stage-{safe}.sh"
    sentinel_path = temp_dir / f"stage-{safe}.rc"
    window_id_path = temp_dir / f"stage-{safe}.id"
    commands = []
    if records:
        batch_path = temp_dir / f"batch-{safe}.json"
        batch_path.write_text(json.dumps(records))
        command = [
            sys.executable, "scripts/make_screenshot.py",
            "--batch", str(batch_path),
            "--window-id-file", str(window_id_path),
            "--workers", str(workers)] + capture_delay_arguments(job)
        if status_path is not None:
            command.extend(["--status-file", str(status_path)])
        commands.append(command)
    if run_font:
        commands.append(font_test_arguments(job, window_id_path))
    if run_colors:
        commands.append(color_test_arguments(job, window_id_path))
    if run_bidi:
        commands.append(bidi_script_arguments(job, args, window_id_path))
    if run_spillover:
        commands.append(spillover_script_arguments(
            job, args, window_id_path, workers))
    stage.write_commands(
        script_path, commands, sentinel_path, stop_on_error=False,
        log_path=log_path)
    return script_path, sentinel_path, window_id_path


def page_error_summary(section):
    """Return the first recorded page error, or an empty string."""
    errors = section.get("errors") or []
    if not errors:
        return ""
    return (f"; {len(errors)} page(s) not captured, first page "
            f"{errors[0].get('page')}: {errors[0].get('message')}")


def stage_log_tail(log_path, limit=4):
    """Return the last few non-empty lines of a stage log, or an empty string."""
    if log_path is None:
        return ""
    try:
        lines = [line.strip()
                 for line in log_path.read_text(
                     encoding="utf-8", errors="replace").splitlines()
                 if line.strip()]
    except OSError:
        return ""
    if not lines:
        return ""
    return "; last output: " + " | ".join(lines[-limit:])


def verify_spillover_output(job, args, started_at, log_path=None):
    """Return an error string when the YAML spillover section is incomplete."""
    section = terminal_document(job.yaml_path).get("spillover_results")
    if not section:
        return ("YAML has no spillover_results section"
                + stage_log_tail(log_path))
    candidates = contested_graphemes()
    if not job.launch_cfg.get("spillover_rtl", True):
        candidates = spillover.without_rtl(candidates)
    expected = len(candidates)
    if args.limit:
        expected = min(expected, args.limit)
    if section.get("n_tested") != expected:
        return (f"YAML reports {section.get('n_tested')} tested, "
                f"expected {expected}{page_error_summary(section)}")
    if spillover.is_stale(section, started_at):
        return ("YAML spillover_results is stale: "
                f"{section.get('scanned_datetime')}"
                f"{page_error_summary(section)}")
    return None


def run_spillover_stage(job, host_cfg, args, temp_dir):
    """Run the spillover stage for one terminal, returning an error or None."""
    stderr_path = temp_dir / f"spillover-{safe_name(job.software_name)}.log"
    script_path, sentinel_path, window_id_path = build_spillover_script(
        temp_dir, job, args, log_path=stderr_path, workers=args.workers)
    budget = job.launch_cfg.get("timeout") or args.spillover_timeout
    started_at = time.time()
    exit_code, message = stage.run_stage(
        job.launch_cfg, host_cfg, script_path, sentinel_path, stderr_path,
        window_id_path, budget)
    terminal_document.cache_clear()
    if exit_code != 0:
        return message, []
    return verify_spillover_output(
        job, args, started_at, stderr_path), []


def run_color_stage(job, host_cfg, args, temp_dir):
    """Run the color measurement stage for one terminal, returning an error."""
    safe = safe_name(job.software_name)
    stderr_path = temp_dir / f"colors-{safe}.log"
    script_path = temp_dir / f"colors-{safe}.sh"
    sentinel_path = temp_dir / f"colors-{safe}.rc"
    window_id_path = temp_dir / f"colors-{safe}.id"
    stage.write_script(
        script_path, color_test_arguments(job, window_id_path),
        sentinel_path, log_path=stderr_path)
    exit_code, message = stage.run_stage(
        job.launch_cfg, host_cfg, script_path, sentinel_path, stderr_path,
        window_id_path, COLOR_TEST_TIMEOUT)
    terminal_document.cache_clear()
    if exit_code != 0:
        return message, []
    return verify_color_output(job), []


def run_combined_stage(job, host_cfg, args, temp_dir):
    """Run every stage of *job* in one terminal launch."""
    run_screens = not job.launch_cfg.get("skip_screenshots")
    run_font = not job.launch_cfg.get("skip_screenshots")
    run_colors = not job.launch_cfg.get("skip_colors")
    run_bidi = not job.launch_cfg.get("skip_bidi")
    run_spillover = not job.launch_cfg.get("skip_spillover")
    records = screenshot_records(job) if run_screens else []
    if run_screens:
        remove_stale_screenshots(job)
    if not records:
        run_screens = False
    if not any((run_screens, run_font, run_colors, run_bidi, run_spillover)):
        return None, []
    stderr_path = temp_dir / f"stage-{safe_name(job.software_name)}.log"
    status_path = temp_dir / f"stage-{safe_name(job.software_name)}.status"
    script_path, sentinel_path, window_id_path = build_combined_script(
        temp_dir, job, args, records, run_spillover, run_font, run_colors,
        run_bidi, log_path=stderr_path, status_path=status_path,
        workers=args.workers)
    budget = 0.0
    if run_screens:
        budget += stage.scaled_timeout(args.timeout, len(records))
    if run_font:
        budget += FONT_TEST_TIMEOUT
    if run_colors:
        budget += COLOR_TEST_TIMEOUT
    if run_bidi:
        budget += BIDI_TIMEOUT
    if run_spillover:
        budget += job.launch_cfg.get("timeout") or args.spillover_timeout
    started_at = time.time()
    exit_code, message = stage.run_stage(
        job.launch_cfg, host_cfg, script_path, sentinel_path, stderr_path,
        window_id_path, budget,
        max_window_size=imaging.SCREENSHOT_MAX_SIZE)
    terminal_document.cache_clear()
    errors = collect_image_errors(status_path, records) if run_screens else []
    if exit_code != 0 and not (run_screens and status_path.is_file()):
        return message, errors
    if run_font:
        font_error = verify_font_test_output(job)
        if font_error:
            return font_error, errors
    if run_colors:
        color_error = verify_color_output(job)
        if color_error:
            return color_error, errors
    if run_bidi:
        bidi_section = terminal_document(job.yaml_path).get("bidi_results")
        if not bidi_section:
            return "YAML has no bidi_results section", errors
    if run_spillover:
        return verify_spillover_output(
            job, args, started_at, stderr_path), errors
    return None, errors


def host_launch_config(args):
    """Return the launch config of the subterminal host."""
    host_cfg, _ = get_launch_config(args.host_terminal, load_mixins())
    if host_cfg.get("subterminal"):
        raise SystemExit(
            f"Error: --host-terminal '{args.host_terminal}' is a subterminal")
    return host_cfg


def docker_args(args):
    """Return the outer ``docker run`` arguments for the current settings."""
    arguments = []
    if args.stage in ("screenshots", "all"):
        source = os.environ.get("UCS_DETECT_WCWIDTH_SOURCE")
        if source:
            root = Path(source).expanduser()
            root = (PROJECT_DIR / root).resolve() if not root.is_absolute() \
                else root.resolve()
            if (root / "wcwidth" / "__init__.py").is_file():
                arguments.extend(["-v", f"{root}:/wcwidth:ro"])
    return arguments


def screenshot_skip_reason(job):
    """Return the reason *job* is excluded from the screenshot stage."""
    return (job.launch_cfg.get("skip_screenshots_reason")
            or job.launch_cfg.get("skip_reason")
            or "skip_screenshots")


def screenshot_allowed(job, args):
    """Return True when *job* should run the screenshot stage."""
    if not job.launch_cfg.get("skip_screenshots"):
        return True
    if not args.dry_run:
        print(f"[{job.software_name}] screenshots: skipped, "
              f"{screenshot_skip_reason(job)}")
    return False


def split_screenshot_jobs(jobs):
    """Return ``(allowed, skipped)`` jobs for the screenshot stage."""
    allowed = []
    skipped = []
    for job in jobs:
        if job.launch_cfg.get("skip_screenshots"):
            skipped.append(job)
        else:
            allowed.append(job)
    return allowed, skipped


def spillover_skip_reason(job):
    """Return the reason *job* is excluded from the spillover stage."""
    return (job.launch_cfg.get("skip_spillover_reason")
            or job.launch_cfg.get("skip_reason")
            or "skip_spillover")


def spillover_allowed(job, args):
    """Return True when *job* should run the spillover stage."""
    if not job.launch_cfg.get("skip_spillover"):
        return True
    if not args.dry_run:
        print(f"[{job.software_name}] spillover: skipped, "
              f"{spillover_skip_reason(job)}")
    return False


def split_spillover_jobs(jobs):
    """Return ``(allowed, skipped)`` jobs for the spillover stage."""
    allowed = []
    skipped = []
    for job in jobs:
        if job.launch_cfg.get("skip_spillover"):
            skipped.append(job)
        else:
            allowed.append(job)
    return allowed, skipped


def bidi_skip_reason(job):
    """Return the reason *job* is excluded from the BiDi stage."""
    return (job.launch_cfg.get("skip_bidi_reason")
            or job.launch_cfg.get("skip_reason")
            or "skip_bidi")


def bidi_allowed(job, args):
    """Return True when *job* should run the BiDi stage."""
    if not job.launch_cfg.get("skip_bidi"):
        return True
    if not args.dry_run:
        print(f"[{job.software_name}] bidi: skipped, "
              f"{bidi_skip_reason(job)}")
    return False


def split_bidi_jobs(jobs):
    """Return ``(allowed, skipped)`` jobs for the BiDi stage."""
    allowed = []
    skipped = []
    for job in jobs:
        if job.launch_cfg.get("skip_bidi"):
            skipped.append(job)
        else:
            allowed.append(job)
    return allowed, skipped


def color_skip_reason(job):
    """Return the reason *job* is excluded from the color stage."""
    return (job.launch_cfg.get("skip_colors_reason")
            or job.launch_cfg.get("skip_reason")
            or "skip_colors")


def color_allowed(job, args):
    """Return True when *job* should run the color stage."""
    if not job.launch_cfg.get("skip_colors"):
        return True
    if not args.dry_run:
        print(f"[{job.software_name}] colors: skipped, "
              f"{color_skip_reason(job)}")
    return False


def split_color_jobs(jobs):
    """Return ``(allowed, skipped)`` jobs for the color stage."""
    allowed = []
    skipped = []
    for job in jobs:
        if job.launch_cfg.get("skip_colors"):
            skipped.append(job)
        else:
            allowed.append(job)
    return allowed, skipped


def container_budget(job, args):
    """Return the seconds a container needs for the stages it will run."""
    total = 0.0
    if (args.stage in ("screenshots", "all")
            and not job.launch_cfg.get("skip_screenshots")):
        total += stage.scaled_timeout(
            args.timeout, max(1, len(screenshot_records(job))))
        total += FONT_TEST_TIMEOUT
    if args.stage in ("colors", "all"):
        if not job.launch_cfg.get("skip_colors"):
            total += COLOR_TEST_TIMEOUT
    if args.stage in ("bidi", "all"):
        if not job.launch_cfg.get("skip_bidi"):
            total += BIDI_TIMEOUT
    if args.stage in ("spillover", "all"):
        if not job.launch_cfg.get("skip_spillover"):
            total += job.launch_cfg.get("timeout") or args.spillover_timeout
    return total


def docker_stage(args, jobs, extra_args):
    """Run one container per terminal, executing *extra_args* inside it."""
    parallel = stage.default_parallel(args.parallel)
    print(f"Per-terminal {args.stage}: {len(jobs)} terminals, "
          f"{parallel} parallel")
    timeout = max(container_budget(job, args) for job in jobs) + 300
    failures = stage.run_containers(
        [job.software_name for job in jobs], extra_args, parallel,
        "ucs-shots", timeout, docker_args(args))
    if failures:
        print("\nFailures:", file=sys.stderr)
        for name, code in failures:
            print(f"  {name}: exit={code}", file=sys.stderr)
        return 1
    return 0


def print_skipped(skipped):
    """Print the terminals that were not staged."""
    if not skipped:
        return
    print(f"Skipping {len(skipped)} terminals:")
    for name, reason in skipped:
        print(f"  [{name}] {reason}")
    print()


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(
        description="Generate terminal screenshots, colors, and spillover "
                    "evidence")
    parser.add_argument(
        "--stage", choices=("screenshots", "colors", "bidi", "spillover",
                            "all"),
        default="all", help="Which stage to run (default: all)")
    parser.add_argument(
        "--parallel", "-p", type=int, default=0,
        help="Number of Docker containers to stage at once (default: 4); "
             "the host stages one terminal at a time")
    parser.add_argument(
        "--workers", type=int, default=None,
        help="Processes cropping images and analysing pages inside each "
             "terminal (default: none in Docker, CPU count minus two on the "
             "host)")
    parser.add_argument(
        "--timeout", "-t", type=float, default=600,
        help="Base timeout per screenshot stage in seconds (default: 600). "
             "Scaled by the number of screenshots.")
    parser.add_argument(
        "--spillover-timeout", type=float, default=7200,
        help="Timeout per spillover stage in seconds (default: 7200)")
    parser.add_argument(
        "--limit", type=int, default=0,
        help="Test only the first N spillover candidates")
    parser.add_argument(
        "--draw-delay", type=float, default=None,
        help="Seconds between painting spillover page bars and drawing "
             "glyphs (default: 0.15)")
    parser.add_argument(
        "--evidence-dir", default=str(SCREENSHOTS_DIR),
        help="Base directory for full page spillover images")
    parser.add_argument(
        "--dry-run", "-n", action="store_true",
        help="Print what would be executed without actually running")
    parser.add_argument(
        "--run-only", type=str, default="",
        help="Comma separated terminal names to run")
    parser.add_argument(
        "--force", action="store_true",
        help="Run terminals whose launch config is reserved for the other "
             "environment (for example a Docker-preferred terminal on the host)")
    parser.add_argument(
        "--keep-temp", action="store_true",
        help="Keep temporary files on exit (for debugging)")
    parser.add_argument(
        "--host-terminal", default="ghostty",
        help="Terminal used to host subterminals (default: ghostty)")
    parser.add_argument(
        "--use-docker", action="store_true",
        help="Launch each terminal in its own Docker container (--cpus=2)")
    parser.add_argument(
        "--use-system", action="store_true",
        help="Run directly on the host system instead of inside Docker")
    args = parser.parse_args()

    container_mode = args.use_docker or _IS_DOCKER
    launch_containers = args.use_docker and not _IS_DOCKER
    if args.workers is None:
        args.workers = 1 if container_mode else default_workers()
    if args.use_system and not _IS_DOCKER and platform.system().lower() == 'linux':
        try:
            os.environ['FONTCONFIG_FILE'] = fonts.ensure_system_fonts(
                str(PROJECT_DIR))
        except OSError as error:
            print(f'Warning: system font setup failed: {error}',
                  file=sys.stderr)
    jobs, skipped = stage.selected_terminals(args, is_docker=container_mode)

    if launch_containers:
        if not args.dry_run:
            stage.prepare_docker()
        print_skipped(skipped)
        if args.stage == "screenshots":
            jobs, screenshot_skipped = split_screenshot_jobs(jobs)
            print_skipped([
                (job.software_name, screenshot_skip_reason(job))
                for job in screenshot_skipped])
        if args.stage == "spillover":
            jobs, spillover_skipped = split_spillover_jobs(jobs)
            print_skipped([
                (job.software_name, spillover_skip_reason(job))
                for job in spillover_skipped])
        if args.stage == "bidi":
            jobs, bidi_skipped = split_bidi_jobs(jobs)
            print_skipped([
                (job.software_name, bidi_skip_reason(job))
                for job in bidi_skipped])
        if args.stage == "colors":
            jobs, color_skipped = split_color_jobs(jobs)
            print_skipped([
                (job.software_name, color_skip_reason(job))
                for job in color_skipped])
        if args.stage == "all":
            active = []
            inactive = []
            for job in jobs:
                if (job.launch_cfg.get("skip_screenshots")
                        and job.launch_cfg.get("skip_spillover")
                        and job.launch_cfg.get("skip_bidi")
                        and job.launch_cfg.get("skip_colors")):
                    inactive.append(job)
                else:
                    active.append(job)
            jobs = active
            print_skipped([
                (job.software_name,
                 f"screenshots, colors, bidi, and spillover skipped, "
                 f"{screenshot_skip_reason(job)}")
                for job in inactive])
        if not jobs:
            print("No terminal jobs found.", file=sys.stderr)
            return 0
        extra_args = ["--stage", args.stage,
                      "--timeout", str(args.timeout),
                      "--spillover-timeout", str(args.spillover_timeout)]
        if args.force:
            extra_args.append("--force")
        if args.limit:
            extra_args.extend(["--limit", str(args.limit)])
        if args.draw_delay is not None:
            extra_args.extend(["--draw-delay", str(args.draw_delay)])
        if args.stage in ("spillover", "bidi", "all"):
            relative = stage.evidence_relative(args.evidence_dir)
            if relative:
                extra_args.extend(["--evidence-dir", relative])
        if args.dry_run:
            print(f"Would run stage '{args.stage}' in {len(jobs)} "
                  f"containers:")
            for job in sorted(jobs, key=lambda item: item.software_name):
                skip_screen = job.launch_cfg.get("skip_screenshots")
                skip_spill = job.launch_cfg.get("skip_spillover")
                skip_bidi = job.launch_cfg.get("skip_bidi")
                skip_colors = job.launch_cfg.get("skip_colors")
                if args.stage == "colors":
                    detail = ("colors skipped"
                              if skip_colors else "colors")
                elif args.stage == "bidi":
                    detail = ("bidi skipped"
                              if skip_bidi else "bidi probe")
                elif skip_screen and skip_spill and skip_bidi and skip_colors:
                    detail = "every stage skipped"
                elif skip_spill and skip_bidi and skip_colors:
                    detail = "screenshots and font test"
                elif skip_screen and skip_colors:
                    detail = "bidi and spillover only"
                elif skip_spill:
                    detail = "screenshots, font test, colors, and bidi"
                elif skip_screen:
                    detail = "colors, bidi, and spillover"
                else:
                    detail = ("screenshots, font test, colors, bidi, then "
                              "spillover")
                print(f"  [{job.software_name}] {detail}")
            return 0
        return docker_stage(args, jobs, extra_args)

    if platform.system().lower() not in ("linux", "darwin"):
        print(f"Error: unsupported OS '{platform.system()}'", file=sys.stderr)
        return 1
    if not imaging.require_capture_tools():
        print("Error: the capture tools for this platform are missing",
              file=sys.stderr)
        return 1

    print_skipped(skipped)
    host_cfg = host_launch_config(args)

    if not jobs:
        print("No terminal jobs found.", file=sys.stderr)
        return 0
    if args.dry_run:
        print(f"Would run stage '{args.stage}' for {len(jobs)} terminals:")
        for job in sorted(jobs, key=lambda item: item.software_name):
            skip_screen = job.launch_cfg.get("skip_screenshots")
            skip_colors = job.launch_cfg.get("skip_colors")
            skip_spill = job.launch_cfg.get("skip_spillover")
            skip_bidi = job.launch_cfg.get("skip_bidi")
            if args.stage == "screenshots":
                detail = f"{len(screenshot_records(job))} screenshots"
                if skip_screen:
                    detail = (f"screenshots skipped, "
                              f"{screenshot_skip_reason(job)}")
            elif args.stage == "colors":
                detail = "16 colors"
                if skip_colors:
                    detail = f"colors skipped, {color_skip_reason(job)}"
            elif args.stage == "bidi":
                detail = "bidi probe"
                if skip_bidi:
                    detail = f"bidi skipped, {bidi_skip_reason(job)}"
            elif args.stage == "spillover":
                detail = f"{len(contested_graphemes())} candidates"
                if skip_spill:
                    detail = (f"spillover skipped, "
                              f"{spillover_skip_reason(job)}")
            else:
                parts = []
                if not skip_screen:
                    parts.append(f"{len(screenshot_records(job))} screenshots")
                    parts.append("font test")
                if not skip_colors:
                    parts.append("colors")
                if not skip_bidi:
                    parts.append("bidi probe")
                if not skip_spill:
                    parts.append(f"{len(contested_graphemes())} candidates")
                detail = ", ".join(parts) if parts else "all stages skipped"
            print(f"  [{job.software_name}] {detail}")
        return 0

    temp_dir = Path(tempfile.mkdtemp(prefix="ucs-stages-"))
    if args.keep_temp:
        print(f"Temp directory: {temp_dir}")
    else:
        atexit.register(shutil.rmtree, str(temp_dir), ignore_errors=True)

    print(f"Per-terminal {args.stage}: {len(jobs)} terminals, "
          f"{args.workers} image workers each")

    def stage_one(job):
        """Run one terminal's stage, returning ``(label, message, errors)``."""
        if args.stage == "all":
            if (job.launch_cfg.get("skip_screenshots")
                    and job.launch_cfg.get("skip_spillover")
                    and job.launch_cfg.get("skip_bidi")
                    and job.launch_cfg.get("skip_colors")):
                return None
            error, errors = run_combined_stage(job, host_cfg, args, temp_dir)
            return "all", error, errors
        if args.stage == "screenshots":
            if not screenshot_allowed(job, args):
                return None
            if not screenshot_records(job):
                print(f"[{job.software_name}] screenshots: no failures found")
                if not args.dry_run:
                    remove_stale_screenshots(job)
                return None
            error, errors = run_screenshot_stage(
                job, host_cfg, args, temp_dir)
            return "screenshots", error, errors
        if args.stage == "colors":
            if not color_allowed(job, args):
                return None
            error, errors = run_color_stage(job, host_cfg, args, temp_dir)
            return "colors", error, errors
        if args.stage == "bidi":
            if not bidi_allowed(job, args):
                return None
            error, errors = run_bidi_stage(job, host_cfg, args, temp_dir)
            return "bidi", error, errors
        if not spillover_allowed(job, args):
            return None
        error, errors = run_spillover_stage(job, host_cfg, args, temp_dir)
        return "spillover", error, errors

    failures = []
    recoverable = []
    attempted = 0
    started = time.monotonic()
    for job in sorted(jobs, key=lambda item: item.software_name):
        try:
            outcome = stage_one(job)
        except Exception as error:  # pylint: disable=broad-except
            attempted += 1
            print(f"[{job.software_name}] {args.stage}: EXCEPTION: {error}")
            failures.append((job.software_name, args.stage, str(error)))
            continue
        if outcome is None:
            continue
        label, message, errors = outcome
        attempted += 1
        if message:
            print(f"[{job.software_name}] {label}: FAILED: {message}")
            failures.append((job.software_name, label, message))
        else:
            print(f"[{job.software_name}] {label}: OK")
        for error in errors:
            recoverable.append((job.software_name, error))
        if errors:
            print(f"[{job.software_name}] {label}: "
                  f"{len(errors)} recoverable image error(s)")

    elapsed = time.monotonic() - started
    print(f"\n--- Done in {elapsed:.1f}s: "
          f"{attempted - len(failures)}/{attempted} stages OK, "
          f"{len(recoverable)} recoverable image error(s) ---")
    if failures:
        print("\nFailures:")
        for name, label, message in failures:
            print(f"  {name} [{label}]: {message}")
    if recoverable:
        print("\nRecoverable image errors:")
        for name, error in recoverable:
            print(f"  [{name}] {error.get('output')}: {error.get('error')}")
    if failures or recoverable:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
