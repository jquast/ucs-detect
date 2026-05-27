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
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import NamedTuple
import uuid

import yaml

from ucs_detect.accessories import find_best_failure, safe_name

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
SCREENSHOTS_DIR = PROJECT_DIR / "docs" / "_static" / "screenshots"
DOCKER_IMAGE = "ucs-detect:latest"
_IS_DOCKER = os.path.exists("/.dockerenv")


class DiscoveredYAML(NamedTuple):
    """A YAML data file discovered by discover_yamls."""
    path: Path
    software_name: str


_RE_SYSTEM = re.compile(r'^system:\s*(\S+)', re.MULTILINE)
_RE_SOFTWARE_NAME = re.compile(r'^software_name:\s*(.+)', re.MULTILINE)
_RE_PAUSE = re.compile(r'^\\p(\d+)$')

_KEY_INJECT_LOCK = threading.RLock()

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


def load_mixins():
    """Load terminals.yaml, returning a dict keyed by lowercased software_name."""
    mixins_path = PROJECT_DIR / "terminals.yaml"
    if not mixins_path.exists():
        return {}
    with open(mixins_path) as f:
        data = yaml.safe_load(f) or {}
    terminals = data.get("terminals", {})
    result = {}
    for key, value in terminals.items():
        result[key.lower()] = value
    return result


def discover_yamls(target_system):
    """Yield (yaml_path, software_name) for each data YAML matching *target_system*."""
    target_lower = target_system.lower()
    for yaml_path in sorted(DATA_DIR.glob("*.yaml")):
        if yaml_path.name in ("terminals.yaml",):
            continue
        try:
            file_size = yaml_path.stat().st_size
            if file_size < 200:
                continue
            with open(yaml_path) as f:
                head = f.read(4096)
        except OSError:
            continue

        m = _RE_SYSTEM.search(head)
        if not m or m.group(1).lower() != target_lower:
            continue

        sw_name = (m.group(1).strip()
                   if (m := _RE_SOFTWARE_NAME.search(head))
                   else yaml_path.stem)

        yield DiscoveredYAML(yaml_path, sw_name)


def get_launch_config(sw_name, mixins):
    """Return (launch_config, is_explicit) for *sw_name*."""
    key = sw_name.lower()
    raw_entry = mixins.get(key, {})
    launch = raw_entry.get("launch", {}) if raw_entry else {}

    if _IS_DOCKER and raw_entry.get("launch_docker"):
        launch = raw_entry["launch_docker"]
    elif not _IS_DOCKER and raw_entry.get("launch_system"):
        launch = raw_entry["launch_system"]

    is_explicit = bool(launch)

    skip_docker = raw_entry.get("skip_docker", False)

    cfg = {
        "program": launch.get("program", key),
        "args": launch.get("args", ["-e"]),
        "subterminal": launch.get("subterminal", False),
        "wrapper": launch.get("wrapper", []),
        "skip": launch.get("skip", False),
        "skip_docker": skip_docker,
        "skip_reason": raw_entry.get("skip_reason", ""),
        "wm_class": launch.get("wm_class", None),
        "post_launch_delay_ms": launch.get("post_launch_delay_ms", 0),
        "post_launch_keys": launch.get("post_launch_keys", []),
    }
    return cfg, is_explicit


def extract_failures(yaml_path):
    """Extract all failure records from a YAML data file.

    Returns a list of (category, wchars, expected_width, measured_width) tuples.
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

    return failures


def build_launch_args(launch_cfg, script_path):
    """Build the full argv list for launching a terminal that executes *script_path*."""
    argv = list(launch_cfg["wrapper"])
    argv.append(launch_cfg["program"])
    script_str = str(script_path)
    has_placeholder = False
    for arg in launch_cfg["args"]:
        if "{script}" in arg:
            has_placeholder = True
            argv.append(arg.replace("{script}", script_str))
        else:
            argv.append(arg)
    if not has_placeholder and not launch_cfg.get("post_launch_keys"):
        argv.extend(["/bin/sh", script_str])
    return argv


def build_subterminal_launch_args(launch_cfg, host_launch_cfg, script_path):
    """Build launch args for a subterminal, wrapping inside a host terminal."""
    script_str = str(script_path)
    inner_parts = [launch_cfg["program"]] + launch_cfg["args"]
    has_placeholder = any("{script}" in a for a in launch_cfg["args"])
    if not has_placeholder and not launch_cfg.get("post_launch_keys"):
        inner_parts.extend(["/bin/sh", script_str])
    else:
        inner_parts = [p.replace("{script}", script_str) for p in inner_parts]

    inner_cmd = " ".join(shlex.quote(a) for a in inner_parts)
    inner_cmd = f"unset TERM_PROGRAM TERM_PROGRAM_VERSION; {inner_cmd}"
    argv = list(host_launch_cfg.get("wrapper", []))
    argv.append(host_launch_cfg["program"])
    argv.extend(host_launch_cfg.get("args", ["-e"]))
    argv.extend(["sh", "-c", inner_cmd])
    return argv


def build_batch_script(script_path, sentinel_path, batch_json_path):
    """Write a shell script that runs make_screenshot.py batch mode."""
    script_rel = "scripts/make_screenshot.py"
    parts = [
        "#!/bin/sh",
        "export LANG=en_US.UTF-8",
        f"cd {shlex.quote(str(PROJECT_DIR))} || exit 1",
        f"python {shlex.quote(script_rel)}"
        f" --batch {shlex.quote(str(batch_json_path))}",
        "RC=$?",
        "echo $RC > " + shlex.quote(str(sentinel_path)),
        "if [ $RC -ne 0 ]; then",
        '    read -p "Press enter to exit... " _',
        "fi",
    ]
    script_path.write_text("\n".join(parts) + "\n")
    script_path.chmod(0o755)


def find_window_for_command(launch_cfg, pid, timeout=8):
    """Find X11 window ID for a launched process, by PID then by class name."""
    deadline = time.monotonic() + timeout

    # Strategy 1: search by PID
    pid_deadline = time.monotonic() + min(timeout / 2, 5)
    while time.monotonic() < pid_deadline:
        try:
            result = subprocess.run(
                ["xdotool", "search", "--onlyvisible", "--pid", str(pid)],
                capture_output=True, text=True, timeout=3,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().split("\n")[-1]
        except (subprocess.TimeoutExpired, OSError):
            pass
        time.sleep(0.3)

    # Strategy 2: search by class name
    wm_class = launch_cfg.get("wm_class") or os.path.basename(
        launch_cfg.get("program", "")
    ).lower()
    while time.monotonic() < deadline:
        for flag in ("--class", "--classname"):
            try:
                result = subprocess.run(
                    ["xdotool", "search", "--onlyvisible", flag, wm_class],
                    capture_output=True, text=True, timeout=3,
                )
                if result.returncode == 0 and result.stdout.strip():
                    return result.stdout.strip().split("\n")[-1]
            except (subprocess.TimeoutExpired, OSError):
                pass
        time.sleep(0.3)

    return None


def inject_keys(window_id, keys):
    """Send keystrokes to a window via xdotool.

    Special tokens:
      ``\\n``       press Return
      ``\\pNNN``    pause for NNN milliseconds
    """
    subprocess.run(
        ["xdotool", "windowfocus", "--sync", str(window_id)],
        capture_output=True, timeout=2,
    )
    time.sleep(0.3)
    merged = []
    for key in keys:
        if key == "\n" or _RE_PAUSE.match(key):
            if merged:
                combined = "".join(merged)
                subprocess.run(
                    ["xdotool", "type", "--delay", "30", combined],
                    capture_output=True, timeout=120,
                )
                merged = []
            if key == "\n":
                subprocess.run(
                    ["xdotool", "key", "Return"],
                    capture_output=True, timeout=5,
                )
            else:
                ms = int(_RE_PAUSE.match(key).group(1))
                time.sleep(ms / 1000.0)
        else:
            merged.append(key)
    if merged:
        combined = "".join(merged)
        subprocess.run(
            ["xdotool", "type", "--delay", "30", combined],
            capture_output=True, timeout=120,
        )


def _docker_image_exists():
    try:
        result = subprocess.run(
            ["docker", "images", "-q", DOCKER_IMAGE],
            capture_output=True, text=True, timeout=10,
        )
        return bool(result.stdout.strip())
    except (subprocess.TimeoutExpired, OSError, FileNotFoundError):
        return False


def _docker_build():
    print(f"Building Docker image {DOCKER_IMAGE} ...", flush=True)
    subprocess.check_call(
        ["docker", "build", "-f", str(PROJECT_DIR / "Dockerfile"),
         "-t", DOCKER_IMAGE, str(PROJECT_DIR)],
    )


def _docker_per_terminal_run(args):
    system_name = platform.system()
    all_terminals = list(discover_yamls(system_name))
    if not all_terminals:
        print(f"No terminal YAML files found for {system_name}", file=sys.stderr)
        sys.exit(0)

    mixins = load_mixins()
    run_only = set(n.strip().lower() for n in args.run_only.split(",") if n.strip()) if args.run_only else set()

    jobs = []
    for d in all_terminals:
        launch_cfg, _ = get_launch_config(d.software_name, mixins)
        if launch_cfg["skip"] or launch_cfg["skip_docker"]:
            continue
        if run_only:
            if d.software_name.lower() not in run_only and launch_cfg.get("program", "").lower() not in run_only:
                continue
        jobs.append(d.software_name)

    n_cpus = os.cpu_count() or 2
    parallel = max(1, min(n_cpus * 3 // 8, 16))

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
            except Exception as exc:
                print(f"[{sw_name}] EXCEPTION: {exc}", flush=True)


def main():
    parser = argparse.ArgumentParser(
        description="Generate terminal screenshots of unicode width discrepancies")
    parser.add_argument(
        "--parallel", "-p", type=int, default=1,
        help="Number of terminals to run in parallel (default: 1)")
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
        if not _docker_image_exists():
            _docker_build()
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

    run_only = set()
    if args.run_only:
        run_only = set(n.strip().lower() for n in args.run_only.split(",") if n.strip())

    # Group failures by terminal (one launch per terminal)
    terminal_jobs = {}  # sw_name -> (launch_cfg, list of failure dicts)
    skipped = []

    for d in all_terminals:
        launch_cfg, is_explicit = get_launch_config(d.software_name, mixins)

        if run_only:
            name_lower = d.software_name.lower()
            prog_lower = launch_cfg.get("program", "").lower()
            if (name_lower not in run_only and prog_lower not in run_only):
                skipped.append((d.software_name, "not in --run-only"))
                continue

        if launch_cfg["skip"]:
            reason = launch_cfg.get("skip_reason") or "marked skip in mixins"
            skipped.append((d.software_name, reason))
            continue

        if _IS_DOCKER and launch_cfg.get("skip_docker"):
            reason = launch_cfg.get("skip_reason") or "marked skip_docker in mixins"
            skipped.append((d.software_name, reason))
            continue

        if launch_cfg["subterminal"] and not is_explicit:
            skipped.append((d.software_name, "subterminal, no launch config"))
            continue

        failures = extract_failures(d.path)
        if not failures:
            skipped.append((d.software_name, "no width failures found"))
            continue

        safe = safe_name(d.software_name)
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
            })

        terminal_jobs[d.software_name] = (launch_cfg, records)

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

            # Key injection for terminals that don't support -e
            if post_keys:
                with _KEY_INJECT_LOCK:
                    time.sleep(0.5)
                    time.sleep(post_delay / 1000.0)
                    window_cfg = (host_launch_cfg
                                  if launch_cfg["subterminal"]
                                  else launch_cfg)
                    window_id = find_window_for_command(window_cfg, proc.pid)
                    if window_id is not None:
                        script_str = str(script_path)
                        resolved_keys = [
                            key.replace("${SCRIPT}", script_str)
                            for key in post_keys
                        ]
                        text_keys = [k for k in resolved_keys
                                     if k != "\n" and not _RE_PAUSE.match(k)]
                        print(f"injecting: {''.join(text_keys)} ... ",
                              end="", flush=True)
                        inject_keys(window_id, resolved_keys)
                        time.sleep(1.5)
                    else:
                        proc.kill()
                        msg = (
                            "key injection failed: could not find window "
                            f"for {window_cfg['program']} (PID {proc.pid})")
                        print(f"FAILED: {msg}")
                        failures_list.append((sw_name, -4, msg))
                        continue

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
