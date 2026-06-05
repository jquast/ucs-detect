#!/usr/bin/env python3
"""Generate terminal screenshots of unicode width discrepancies for all terminals.

Reads YAML test result files from ``data/``, extracts the midpoint failure for
each test category, launches each terminal once scripts/make_screenshot.py
in batch mode, and collects the resulting PNG screenshots.
"""
import argparse
import atexit
import json
import os
import platform
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import uuid

import yaml

from ucs_detect.accessories import (
    DiscoveredYAML,
    _IS_DOCKER,
    _KEY_INJECT_LOCK,
    _RE_PAUSE,
    build_launch_args,
    build_subterminal_launch_args,
    check_unmatched_run_only,
    discover_yamls,
    docker_build,
    docker_image_exists,
    find_best_failure,
    find_window_for_command,
    get_launch_config,
    inject_keys,
    load_mixins,
    parse_run_only,
    run_kill_command,
    safe_name,
    should_skip,
    get_project_dir,
    get_data_dir,
)

PROJECT_DIR = get_project_dir()
DATA_DIR = get_data_dir()
SCREENSHOTS_DIR = PROJECT_DIR / "docs" / "_static" / "screenshots"
DOCKER_IMAGE = "ucs-detect:latest"

# Categories that have failed_codepoints in their results
_CATEGORY_YAML_KEYS = [
    ("unicode_wide_results", "wide"),
    ("emoji_zwj_results", "zwj"),
    ("emoji_vs16_results", "vs16"),
    ("emoji_vs15_results", "vs15"),
    ("sri_results", "sri"),
    ("sfz_results", "sfz"),
    ("ri_results", "ri"),
]


def extract_failures(yaml_path):
    """Extract all failure records from a YAML data file.

    Returns (failures, software_version) where failures is a list of
    (category, wchars, expected_width, measured_width) tuples.
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
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

    # Language results have a different structure
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


def build_batch_script(script_path, sentinel_path, batch_json_path, window_id=None):
    """Write a shell script that runs make_screenshot.py batch mode."""
    script_rel = "scripts/make_screenshot.py"
    wid_arg = f" --window-id {shlex.quote(str(window_id))}" if window_id else ""
    py_bin = shlex.quote(os.path.dirname(sys.executable))
    parts = [
        "#!/bin/sh",
        "export LANG=en_US.UTF-8",
        f"export PATH={py_bin}:$PATH",
        f"cd {shlex.quote(str(PROJECT_DIR))} || exit 1",
        f"{shlex.quote(sys.executable)} {shlex.quote(script_rel)}"
        f" --batch {shlex.quote(str(batch_json_path))}{wid_arg}",
        "RC=$?",
        "echo $RC > " + shlex.quote(str(sentinel_path)),
        "if [ $RC -ne 0 ]; then",
        '    read -p "Press enter to exit... " _',
        "fi",
    ]
    script_path.write_text("\n".join(parts) + "\n")
    script_path.chmod(0o755)


def _docker_per_terminal_run(args):
    system_name = platform.system()
    all_terminals = list(discover_yamls(system_name))
    if not all_terminals:
        print(f"No terminal YAML files found for {system_name}", file=sys.stderr)
        sys.exit(0)

    mixins = load_mixins()
    run_only = parse_run_only(args.run_only)
    matched_run_only = set()

    jobs = []
    for d in all_terminals:
        if d.error_msg:
            continue
        launch_cfg, _ = get_launch_config(d.software_name, mixins)
        if launch_cfg["skip"] or launch_cfg["skip_docker"]:
            launch_cfg, _ = get_launch_config(d.path.stem, mixins)
        if launch_cfg["skip"] or launch_cfg["skip_docker"]:
            continue
        if run_only:
            name_lower = d.software_name.lower()
            prog_lower = launch_cfg.get("program", "").lower()
            if name_lower not in run_only and prog_lower not in run_only:
                continue
            for candidate in (name_lower, prog_lower):
                if candidate in run_only:
                    matched_run_only.add(candidate)
        jobs.append(d.software_name)

    if run_only:
        check_unmatched_run_only(run_only, matched_run_only)

    n_cpus = os.cpu_count() or 2
    parallel = args.parallel or max(1, (n_cpus - 2) // 4)

    print(f"Per-terminal Docker screenshots: {len(jobs)} terminals, {parallel} parallel")

    with ThreadPoolExecutor(max_workers=parallel) as executor:
        futures = {}
        for sw_name in jobs:
            cmd = [
                "docker", "run", "--rm", "--cpus=2",
                "-e", "DISPLAY=:99",
                "-v", f"{PROJECT_DIR}:/app",
                DOCKER_IMAGE,
                "python", "make-screenshots.py", "--use-system",
                "--timeout", str(args.timeout),
                "--run-only", sw_name,
            ]
            print(f"[{sw_name}] docker run ...", flush=True)
            future = executor.submit(subprocess.run, cmd, capture_output=True,
                                     text=True, timeout=args.timeout + 60)
            futures[future] = sw_name

        for future in as_completed(futures):
            sw_name = futures[future]
            try:
                result = future.result()
                status = "OK" if result.returncode == 0 else f"exit={result.returncode}"
                print(f"[{sw_name}] {status}", flush=True)
                if result.returncode != 0:
                    if result.stderr:
                        print(f"[{sw_name}] stderr: {result.stderr.strip()}", flush=True)
                    if result.stdout:
                        print(f"[{sw_name}] stdout: {result.stdout.strip()}", flush=True)
            except Exception as exc:
                print(f"[{sw_name}] EXCEPTION: {exc}", flush=True)


def main():
    parser = argparse.ArgumentParser(
        description="Generate terminal screenshots of unicode width discrepancies")
    parser.add_argument(
        "--parallel", "-p", type=int, default=0,
        help="Number of terminals to run in parallel (default: auto)")
    parser.add_argument(
        "--timeout", "-t", type=float, default=600,
        help="Base timeout per terminal in seconds (default: 600). "
             "Scaled by number of screenshots: timeout * max(1, n_screenshots / 10).")
    parser.add_argument(
        "--dry-run", "-n", action="store_true",
        help="Print what would be executed without actually running")
    parser.add_argument(
        "--run-only", type=str, default="",
        help="Comma-separated list of terminal names to run; all others are skipped")
    parser.add_argument(
        "--keep-temp", action="store_true",
        help="Keep temporary files on exit (for debugging)")
    parser.add_argument(
        "--host-terminal", default="ghostty",
        help="Terminal used to host subterminals (screen, tmux, etc.) "
             "(default: ghostty)")
    parser.add_argument(
        "--use-docker", action="store_true",
        help="Launch each terminal in its own Docker container (--cpus=2)")
    parser.add_argument(
        "--use-system", action="store_true",
        help="Run directly on the host system instead of inside Docker")
    args = parser.parse_args()

    if args.use_docker and not _IS_DOCKER:
        if not docker_image_exists():
            docker_build(PROJECT_DIR / "Dockerfile", PROJECT_DIR)
        _docker_per_terminal_run(args)
        return

    system_name = platform.system()
    if system_name.lower() not in ("linux",):
        print(f"Error: unsupported OS '{system_name}'. Only Linux is supported.",
              file=sys.stderr)
        sys.exit(1)

    if not shutil.which("xdotool") or not shutil.which("xwd"):
        print("Error: xdotool and xwd are required", file=sys.stderr)
        sys.exit(1)

    mixins = load_mixins()

    # Build host terminal launch config for subterminals
    host_launch_cfg, _ = get_launch_config(args.host_terminal, mixins)
    if host_launch_cfg.get("subterminal"):
        print(f"Error: --host-terminal '{args.host_terminal}' is a subterminal",
              file=sys.stderr)
        sys.exit(1)

    all_terminals = list(discover_yamls(system_name))

    if not all_terminals:
        print(f"No terminal YAML files found for {system_name}", file=sys.stderr)
        sys.exit(0)

    run_only = parse_run_only(args.run_only)
    matched_run_only = set()

    # Group failures by terminal (one launch per terminal)
    terminal_jobs = {}  # sw_name -> (launch_cfg, list of failure dicts)
    skipped = []

    for d in all_terminals:
        if d.error_msg:
            continue
        launch_cfg, is_explicit = get_launch_config(d.software_name, mixins)
        if not is_explicit:
            launch_cfg, is_explicit = get_launch_config(d.path.stem, mixins)

        if run_only:
            name_lower = d.software_name.lower()
            prog_lower = launch_cfg.get("program", "").lower()
            if (name_lower not in run_only and prog_lower not in run_only):
                skipped.append((d.software_name, "not in --run-only"))
                continue
            for candidate in (name_lower, prog_lower):
                if candidate in run_only:
                    matched_run_only.add(candidate)

        if launch_cfg["skip"]:
            reason = launch_cfg.get("skip_reason") or "marked skip in mixins"
            skipped.append((d.software_name, reason))
            continue

        if should_skip(launch_cfg, is_docker=_IS_DOCKER):
            reason = launch_cfg.get("skip_reason") or "excluded by should_skip"
            skipped.append((d.software_name, reason))
            continue

        if launch_cfg["subterminal"] and not is_explicit:
            skipped.append((d.software_name, "subterminal, no launch config"))
            continue

        if not is_explicit and launch_cfg["program"] == d.software_name.lower():
            skipped.append((d.software_name, "no terminals.yaml entry"))
            continue

        failures, software_version = extract_failures(d.path)
        if not failures:
            skipped.append((d.software_name, "no width failures found"))
            continue

        # Determine effective software_name for wcwidth term_program matching.
        # VTE-based terminals (GNOME Terminal, XFCE Terminal, etc.) report
        # software_name different from wcwidth's canonical "vte" — detect
        # them via software_version and map to "vte".
        effective_sw_name = d.software_name
        if software_version and "VTE" in software_version:
            effective_sw_name = "vte"

        entry = mixins.get(d.software_name.lower(), {})
        if not entry:
            entry = mixins.get(d.path.stem.lower(), {})
        sw_display = entry.get("display_name", d.software_name)
        safe = safe_name(sw_display)
        unique_id = uuid.uuid4().hex[:8]

        records = []
        for category, wchars, expected_width, measured_width in failures:
            out_dir = SCREENSHOTS_DIR / safe
            out_path = out_dir / f"{category}.png"
            records.append({
                "wchars": wchars,
                "expected_width": expected_width,
                "measured_width": measured_width,
                "output": str(out_path),
                "title": f"ucs-shot-{safe}-{category}-{unique_id}",
                "software_name": effective_sw_name,
            })

        terminal_jobs[sw_display] = (launch_cfg, records)

    if run_only:
        check_unmatched_run_only(run_only, matched_run_only)

    if skipped:
        print(f"Skipping {len(skipped)} terminals:")
        for name, reason in skipped:
            print(f"  [{name}] {reason}")
        print()

    if not terminal_jobs:
        print("No screenshot jobs found.", file=sys.stderr)
        sys.exit(0)

    total_screenshots = sum(len(records) for _, records in terminal_jobs.values())

    if args.dry_run:
        print(f"Would launch {len(terminal_jobs)} terminals"
              f" to generate {total_screenshots} screenshots:\n")
        for sw_name, (_launch_cfg, records) in sorted(terminal_jobs.items()):
            safe = safe_name(sw_name)
            print(f"  [{sw_name}] {len(records)} screenshots:")
            for rec in records:
                cat = os.path.basename(rec["output"]).replace(".png", "")
                print(f"    {cat}: {rec['wchars']} "
                      f"(term={rec['measured_width']}, wcwidth={rec['expected_width']})")
        return

    # Create output directories
    for sw_name in terminal_jobs:
        out_dir = SCREENSHOTS_DIR / safe_name(sw_name)
        out_dir.mkdir(parents=True, exist_ok=True)

    temp_dir = Path(tempfile.mkdtemp(prefix="ucs-screenshots-"))
    if args.keep_temp:
        print(f"Temp directory: {temp_dir}")
    else:
        atexit.register(shutil.rmtree, str(temp_dir), ignore_errors=True)

    print(f"Launching {len(terminal_jobs)} terminals"
          f" to generate {total_screenshots} screenshots"
          f" (timeout={args.timeout}s)")
    print()

    failures_list = []
    t0 = time.monotonic()

    for sw_name, (launch_cfg, records) in sorted(terminal_jobs.items()):
        safe = safe_name(sw_name)
        n_records = len(records)
        print(f"[{sw_name}] {n_records} screenshots ... ", end="", flush=True)

        # Remove old screenshots for this terminal
        out_dir = SCREENSHOTS_DIR / safe
        if out_dir.exists():
            for old_png in out_dir.glob("*.png"):
                old_png.unlink()
            for old_png in out_dir.glob("*.xwd"):
                old_png.unlink()

        # Write batch JSON
        batch_json_path = temp_dir / f"batch-{safe}.json"
        batch_json_path.write_text(json.dumps(records))

        script_path = temp_dir / f"screenshot-{safe}.sh"
        sentinel_path = temp_dir / f"exit-{safe}.rc"
        stderr_path = temp_dir / f"stderr-{safe}.log"

        # Build batch script now so the file exists before launch.
        # Direct-launch terminals (konsole, etc.) reference the script
        # path in their argv.  Key-inject terminals inject the path
        # later.  We'll rebuild with --window-id once we have one.
        build_batch_script(script_path, sentinel_path, batch_json_path)

        try:
            if not launch_cfg["subterminal"]:
                argv = build_launch_args(launch_cfg, script_path)
            else:
                argv = build_subterminal_launch_args(
                    launch_cfg, host_launch_cfg, script_path)

            post_keys = launch_cfg.get("post_launch_keys", [])
            post_delay = launch_cfg.get("post_launch_delay_ms", 0)

            with open(stderr_path, "w") as stderr_file:
                env = os.environ.copy()
                env.pop("TERM_PROGRAM", None)
                env.pop("TERM_PROGRAM_VERSION", None)
                proc = subprocess.Popen(
                    argv,
                    env=env,
                    stdout=subprocess.DEVNULL,
                    stderr=stderr_file,
                    stdin=subprocess.DEVNULL,
                )

            # Find the X11 window.  Key-inject terminals need it for
            # xdotool; all terminals benefit from passing --window-id to
            # the batch script so find_own_window (unreliable inside
            # sandboxes and subterminals) is never called.
            captured_wid = None
            window_cfg = (host_launch_cfg
                          if launch_cfg["subterminal"]
                          else launch_cfg)
            snapshot_pre_windows = None
            try:
                result = subprocess.run(
                    ["xdotool", "search", "--onlyvisible", ""],
                    capture_output=True, text=True, timeout=3,
                )
                if result.returncode == 0:
                    snapshot_pre_windows = set(result.stdout.strip().split("\n"))
            except (subprocess.TimeoutExpired, OSError):
                pass

            if post_keys:
                with _KEY_INJECT_LOCK:
                    time.sleep(0.5)
                    time.sleep(post_delay / 1000.0)
                    captured_wid = find_window_for_command(
                        window_cfg, proc.pid,
                        pre_windows=snapshot_pre_windows)
            else:
                captured_wid = find_window_for_command(
                    window_cfg, proc.pid,
                    pre_windows=snapshot_pre_windows)

            # For key-inject terminals: rebuild script with --window-id
            # BEFORE injection so the injected shell command sees it.
            # Direct-launch terminals must NOT be rebuilt, they are
            # already executing the first build.
            if post_keys and captured_wid is not None:
                build_batch_script(script_path, sentinel_path,
                                   batch_json_path, captured_wid)

            if post_keys:
                if captured_wid is None:
                    proc.kill()
                    msg = (
                        "key injection failed: could not find window "
                        f"for {window_cfg['program']} (PID {proc.pid})")
                    print(f"FAILED: {msg}")
                    failures_list.append((sw_name, -4, msg))
                    continue
                script_str = str(script_path)
                resolved_keys = [
                    key.replace("${SCRIPT}", script_str)
                    for key in post_keys
                ]
                text_keys = [k for k in resolved_keys
                             if k != "\n" and not _RE_PAUSE.match(k)]
                print(f"injecting: {''.join(text_keys)} ... ",
                      end="", flush=True)
                inject_keys(captured_wid, resolved_keys)
                time.sleep(1.5)

            # Wait for sentinel or timeout (scaled by screenshot count).
            # Key-inject terminals may fork/detach, so don't collapse the
            # deadline based on the launcher process exiting.
            scaled_timeout = args.timeout * max(1, n_records / 10)
            deadline = time.monotonic() + scaled_timeout
            exit_code = -99
            proc_dead = False
            while time.monotonic() < deadline:
                if sentinel_path.exists():
                    try:
                        exit_code = int(sentinel_path.read_text().strip())
                    except (ValueError, OSError):
                        exit_code = -2
                    break
                if not post_keys and not proc_dead and proc.poll() is not None:
                    proc_dead = True
                    deadline = min(deadline, time.monotonic() + 30)
                time.sleep(0.3)

            if exit_code == -99:
                try:
                    proc.kill()
                except OSError:
                    pass
                print("TIMEOUT")
                failures_list.append((sw_name, -1, "timeout"))
                continue

            run_kill_command(launch_cfg)

            if exit_code != 0:
                stderr_text = ""
                if stderr_path.exists():
                    try:
                        stderr_text = stderr_path.read_text().strip()
                    except OSError:
                        pass
                msg = f"exit code {exit_code}"
                if stderr_text:
                    msg += f" ({stderr_text})"
                print(f"FAILED: {msg}")
                failures_list.append((sw_name, exit_code, msg))
                continue

            # Verify all outputs exist
            missing = []
            for rec in records:
                out_path = Path(rec["output"])
                if not out_path.exists() or out_path.stat().st_size == 0:
                    missing.append(out_path.name)
            if missing:
                print(f"PARTIAL: missing {missing}")
                failures_list.append((sw_name, -2,
                                      f"missing: {', '.join(missing)}"))
            else:
                total_bytes = sum(Path(r["output"]).stat().st_size for r in records)
                print(f"OK ({total_bytes} bytes)")

        except FileNotFoundError:
            msg = f"executable not found: {launch_cfg['program']}"
            print(f"FAILED: {msg}")
            failures_list.append((sw_name, -4, msg))
        except OSError as exc:
            print(f"FAILED: {exc}")
            failures_list.append((sw_name, -4, str(exc)))

    elapsed = time.monotonic() - t0
    n_ok = len(terminal_jobs) - len(failures_list)
    print(f"\n--- Done in {elapsed:.1f}s: {n_ok}/{len(terminal_jobs)} terminals OK"
          f" ({total_screenshots} screenshots) ---")

    if failures_list:
        print("\nFailures:")
        for item in failures_list:
            name = item[0]
            msg = item[-1]
            print(f"  {name}: {msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
