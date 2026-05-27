#!/usr/bin/env python3
"""Run ucs-detect re-run.py for each terminal YAML of the current OS, in series or parallel.

Default mode runs inside a Docker container (Arch Linux + Xvfb).
Use --use-system to run directly on the host.
"""
import argparse
import atexit
import os
import platform
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import NamedTuple
import threading

import yaml

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
DOCKER_IMAGE = "ucs-detect:latest"
DOCKERFILE = PROJECT_DIR / "Dockerfile"

_RE_SYSTEM = re.compile(r'^system:\s*(\S+)', re.MULTILINE)
_RE_SOFTWARE_NAME = re.compile(r'^software_name:\s*(.+)', re.MULTILINE)
_RE_SECONDS_ELAPSED = re.compile(r'^seconds_elapsed:\s*([\d.]+)', re.MULTILINE)
_RE_PAUSE = re.compile(r'^\\p(\d+)$')

_KEY_INJECT_LOCK = threading.RLock()
_KEY_INJECT_PRE_DELAY = 0.5
_KEY_INJECT_POST_DELAY = 1.5

_IS_DOCKER = os.path.exists("/.dockerenv")


class DiscoveredYAML(NamedTuple):
    """A YAML data file discovered by discover_yamls."""
    path: Path
    software_name: str
    seconds_elapsed: float
    error_msg: str | None


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
    """Yield (yaml_path, software_name, seconds_elapsed, error_msg) for each data YAML
    matching *target_system*.  *error_msg* is None for valid data files."""
    target_lower = target_system.lower()
    for yaml_path in sorted(DATA_DIR.glob("*.yaml")):
        if yaml_path.name == "terminals.yaml":
            continue
        try:
            file_size = yaml_path.stat().st_size
            if file_size < 200:
                yield DiscoveredYAML(yaml_path, yaml_path.stem, 0.0,
                    f"file too small ({file_size} bytes)")
                continue
            with open(yaml_path) as f:
                data = yaml.safe_load(f) or {}
        except (OSError, yaml.YAMLError):
            continue

        system = data.get("system", "")
        if system.lower() != target_lower:
            continue

        sw_name = data.get("software_name", yaml_path.stem)
        seconds_elapsed = data.get("seconds_elapsed", 0.0)

        error_msg = None
        if data.get("test_results") == {} and "error" in data:
            error_msg = "previous run failed (empty test_results)"

        yield DiscoveredYAML(yaml_path, sw_name, seconds_elapsed, error_msg)


def get_launch_config(sw_name, mixins):
    """Return (launch_config, is_explicit) for *sw_name*.

    In Docker mode, clears the wrapper for terminals marked ``skip_system``
    (the wrapper was only needed for bare-metal X11 without a WM)."""
    key = sw_name.lower()
    raw_entry = mixins.get(key, {})
    launch = raw_entry.get("launch", {}) if raw_entry else {}

    if _IS_DOCKER and raw_entry.get("launch_docker"):
        launch = raw_entry["launch_docker"]
    elif not _IS_DOCKER and raw_entry.get("launch_system"):
        launch = raw_entry["launch_system"]

    is_explicit = bool(launch)

    skip_system = raw_entry.get("skip_system", False) or launch.get("skip_system", False)
    skip_docker = raw_entry.get("skip_docker", False) or launch.get("skip_docker", False)
    skip_any = launch.get("skip", False)

    wrapper = list(launch.get("wrapper", []))
    if _IS_DOCKER and skip_system and wrapper:
        wrapper = []

    cfg = {
        "program": launch.get("program", key),
        "args": launch.get("args", ["-e"]),
        "subterminal": launch.get("subterminal", False),
        "wrapper": wrapper,
        "skip": skip_any,
        "skip_system": skip_system,
        "skip_docker": skip_docker,
        "skip_reason": raw_entry.get("skip_reason", ""),
        "post_launch_delay_ms": launch.get("post_launch_delay_ms", 0),
        "post_launch_keys": launch.get("post_launch_keys", []),
        "env": launch.get("env", {}),
        "profile_processes": raw_entry.get("profile_processes", []),
        "wm_class": launch.get("wm_class", None),
    }
    return cfg, is_explicit


def _should_skip(launch_cfg, is_docker=None):
    """Return True if the config should be skipped in the current environment.

    If *is_docker* is None, uses the process environment (_IS_DOCKER)."""
    if is_docker is None:
        is_docker = _IS_DOCKER
    if launch_cfg["skip"]:
        return True
    if is_docker and launch_cfg["skip_docker"]:
        return True
    if not is_docker and launch_cfg["skip_system"]:
        return True
    return False


def write_run_script(script_path, yaml_path, sentinel_path,
                     pause_exit=False):
    """Write a shell script that runs re-run.py and records the exit code."""
    yaml_rel = yaml_path.relative_to(PROJECT_DIR)
    parts = [
        "#!/bin/sh",
        f"cd {shlex.quote(str(PROJECT_DIR))} || exit 1",
        f"python re-run.py {shlex.quote(str(yaml_rel))}",
        f"echo $? > {shlex.quote(str(sentinel_path))}",
    ]
    if pause_exit:
        parts.append('read -p "Press enter to exit..." _')
    script_path.write_text("\n".join(parts) + "\n")
    script_path.chmod(0o755)


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


def find_window_for_command(launch_cfg, pid, timeout=8, pre_windows=None):
    """Find X11 window ID for a launched process, by PID then by class name.

    If *pre_windows* is a set of window IDs that existed before the
    process was launched, any new window (not in the set) is returned
    as a last-resort fallback."""
    deadline = time.monotonic() + timeout

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

    if pre_windows is not None:
        while time.monotonic() < deadline:
            try:
                result = subprocess.run(
                    ["xdotool", "search", "--onlyvisible", ""],
                    capture_output=True, text=True, timeout=3,
                )
                if result.returncode == 0:
                    current = set(result.stdout.strip().split("\n"))
                    new = current - pre_windows
                    if new:
                        return max(new, key=int)
            except (subprocess.TimeoutExpired, OSError):
                pass
            time.sleep(0.3)

    return None


def inject_keys(window_id, keys):
    """Send keystrokes to a window via xdotool."""
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


def _launch_and_inject(yaml_path, sw_name, launch_cfg, host_launch_cfg,
                       temp_dir, pause_exit=False):
    """Launch a terminal and inject keys. Does not wait for completion.

    Returns (proc, sentinel_path, stderr_path, error_msg).
    """
    safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in sw_name)
    script_path = temp_dir / f"run-{safe_name}.sh"
    sentinel_path = temp_dir / f"exit-{safe_name}.rc"
    stderr_path = temp_dir / f"stderr-{safe_name}.log"
    write_run_script(script_path, yaml_path, sentinel_path,
                     pause_exit=pause_exit)

    post_delay = launch_cfg.get("post_launch_delay_ms", 0)
    post_keys = launch_cfg.get("post_launch_keys", [])

    try:
        if not launch_cfg["subterminal"]:
            argv = build_launch_args(launch_cfg, script_path)
        else:
            argv = build_subterminal_launch_args(launch_cfg, host_launch_cfg,
                                                 script_path)

        snapshot_pre_windows = None
        if post_keys:
            try:
                result = subprocess.run(
                    ["xdotool", "search", "--onlyvisible", ""],
                    capture_output=True, text=True, timeout=3,
                )
                if result.returncode == 0:
                    snapshot_pre_windows = set(result.stdout.strip().split("\n"))
            except (subprocess.TimeoutExpired, OSError):
                pass

        with open(stderr_path, "w") as stderr_file:
            env = os.environ.copy()
            env.pop("TERM_PROGRAM", None)
            env.pop("TERM_PROGRAM_VERSION", None)
            for key, value in launch_cfg.get("env", {}).items():
                if value == "":
                    env.pop(key, None)
                else:
                    env[key] = value
            proc = subprocess.Popen(
                argv,
                env=env,
                stdout=subprocess.DEVNULL,
                stderr=stderr_file,
                stdin=subprocess.DEVNULL,
            )

        if post_keys:
            with _KEY_INJECT_LOCK:
                time.sleep(_KEY_INJECT_PRE_DELAY)
                time.sleep(post_delay / 1000.0)
                window_cfg = host_launch_cfg if launch_cfg["subterminal"] else launch_cfg
                window_id = find_window_for_command(window_cfg, proc.pid, pre_windows=snapshot_pre_windows)
                if window_id is not None:
                    script_str = str(script_path)
                    resolved_keys = [
                        key.replace("${SCRIPT}", script_str) for key in post_keys
                    ]
                    text_keys = [k for k in resolved_keys
                                 if k != "\n" and not _RE_PAUSE.match(k)]
                    print(f"[{sw_name}] injecting: {''.join(text_keys)}", flush=True)
                    inject_keys(window_id, resolved_keys)
                else:
                    proc.kill()
                    error_msg = (
                        "key injection failed: could not find window "
                        f"for {window_cfg['program']} (PID {proc.pid})"
                    )
                    print(f"[{sw_name}] {error_msg}", flush=True)
                    return (None, sentinel_path, stderr_path, error_msg)
                time.sleep(_KEY_INJECT_POST_DELAY)

        return (proc, sentinel_path, stderr_path, None)

    except FileNotFoundError:
        return (None, None, None, f"executable not found: {launch_cfg['program']}")
    except OSError as exc:
        return (None, None, None, str(exc))


def _poll_sentinel(sw_name, proc, sentinel_path, stderr_path, timeout):
    """Wait for sentinel file.  Returns (sw_name, exit_code, error_msg)."""
    error_msg = None
    exit_code = -99

    deadline = time.monotonic() + timeout
    proc_dead = False
    while time.monotonic() < deadline:
        if sentinel_path.exists():
            try:
                text = sentinel_path.read_text().strip()
                exit_code = int(text)
            except (ValueError, OSError):
                exit_code = -2
            break

        if not proc_dead and proc.poll() is not None:
            proc_dead = True
            deadline = min(deadline, time.monotonic() + 30)

        time.sleep(0.5)

    if exit_code == -99:
        if proc.poll() is not None:
            exit_code = -3
            error_msg = (
                f"process exited with code {proc.returncode} "
                f"but no sentinel file was written"
            )
        else:
            exit_code = -1
            error_msg = f"timeout after {timeout}s"
            try:
                proc.kill()
            except OSError:
                pass

    if error_msg and stderr_path.exists():
        try:
            stderr_text = stderr_path.read_text().strip()
            if stderr_text:
                error_msg += f"\nstderr: {stderr_text}"
        except OSError:
            pass

    return (sw_name, exit_code, error_msg)


def _docker_image_exists():
    """Check if the Docker image is already built."""
    try:
        result = subprocess.run(
            ["docker", "images", "-q", DOCKER_IMAGE],
            capture_output=True, text=True, timeout=10,
        )
        return bool(result.stdout.strip())
    except (subprocess.TimeoutExpired, OSError, FileNotFoundError):
        return False


def _docker_build():
    """Build the Docker image."""
    print(f"Building Docker image {DOCKER_IMAGE} ...", flush=True)
    subprocess.check_call(
        ["docker", "build", "-f", str(DOCKERFILE), "-t", DOCKER_IMAGE,
         str(PROJECT_DIR)],
    )


def _docker_self_run(argv):
    """Re-execute run-series.py inside the Docker container."""
    docker_args = [
        "docker", "run", "--rm",
        "-v", f"{PROJECT_DIR}:/app",
        "-e", "DISPLAY=:99",
        DOCKER_IMAGE,
        "python", "run-series.py",
    ]
    docker_args.extend(argv)
    sys.exit(subprocess.call(docker_args))


def _embed_profile_in_yaml(yaml_path, sw_name, session):
    """Append resource_profile data to the terminal's YAML file."""
    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except (OSError, yaml.YAMLError):
        return
    if data is None:
        return
    data["resource_profile"] = session.to_dict()
    from ucs_detect.profiler import hardware_info
    data["resource_profile"]["hardware"] = hardware_info()
    try:
        with open(yaml_path, "w") as f:
            yaml.safe_dump(data, f, default_flow_style=False,
                           allow_unicode=True)
    except OSError:
        pass


def _fixup_yaml(yaml_path, sw_name, mixins, program):
    """Fix up software_name in YAML from raw XTVERSION values to display names.

    When ucs-detect runs without operator override, the auto-detected
    ``software_name`` is the raw XTVERSION response (e.g. ``VTE`` for
    VTE-based terminals).  This function reads the freshly-written YAML
    and corrects ``software_name`` to the display name from
    ``terminals.yaml``.  If a ``version_template`` is present, the
    ``software_version`` is also composed.

    When auto-detection yields no name at all, *program* (the launch
    binary basename from ``terminals.yaml``) is used as the fallback.
    """
    key = sw_name.lower()
    entry = mixins.get(key, {})
    display_name = entry.get("display_name")
    version_template = entry.get("version_template")

    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except (OSError, yaml.YAMLError):
        return
    if data is None:
        return

    current_name = data.get("software_name", "")
    current_version = data.get("software_version", "")

    if display_name:
        data["software_name"] = display_name
    elif not current_name:
        data["software_name"] = os.path.basename(program) if program else sw_name

    if version_template:
        tr = data.get("terminal_results") or {}
        raw_name = tr.get("software_name", "")
        raw_version = tr.get("software_version", "")
        raw_xtversion = tr.get("xtversion_raw", "")
        if raw_xtversion:
            parts = raw_xtversion.split(None, 1)
            xt_name = parts[0] if parts else ""
            xt_version = parts[1] if len(parts) > 1 else raw_version
        else:
            xt_name = raw_name
            xt_version = raw_version
        version_str = version_template.format(
            sw_name=raw_name,
            sw_version=raw_version,
            xt_name=xt_name,
            xt_version=xt_version,
            xtversion_raw=raw_xtversion,
            release=entry.get("version_release", ""),
        )
        data["software_version"] = version_str

    version_manual = entry.get("version_manual")
    if version_manual and not data.get("software_version"):
        data["software_version"] = version_manual

    try:
        with open(yaml_path, "w") as f:
            yaml.safe_dump(data, f, default_flow_style=False, allow_unicode=True)
    except OSError:
        pass


def _docker_per_terminal_run(args):
    """Run each terminal in its own Docker container, with --cpus=2 each."""
    system_name = platform.system()
    all_terminals = list(discover_yamls(system_name))
    if not all_terminals:
        print(f"No terminal YAML files found for {system_name}", file=sys.stderr)
        sys.exit(0)

    mixins = load_mixins()
    run_only = set(n.strip().lower() for n in args.run_only.split(",") if n.strip()) if args.run_only else set()

    jobs = []
    for d in all_terminals:
        if d.error_msg:
            continue
        launch_cfg, _ = get_launch_config(d.software_name, mixins)
        if run_only:
            name_lower = d.software_name.lower()
            prog_lower = launch_cfg.get("program", "").lower()
            if name_lower not in run_only and prog_lower not in run_only:
                continue
        if _should_skip(launch_cfg, is_docker=True):
            continue
        if launch_cfg.get("subterminal") and not launch_cfg.get("program"):
            continue
        jobs.append((d.software_name, d.seconds_elapsed))

    jobs.sort(key=lambda j: j[1], reverse=True)

    n_cpus = os.cpu_count() or 2
    parallel = max(1, min(n_cpus * 3 // 8, 16))

    print(f"Per-terminal Docker: {len(jobs)} terminals, {parallel} parallel "
          f"(cpus={n_cpus}, timeout={args.timeout}s)")

    with ThreadPoolExecutor(max_workers=parallel) as executor:
        futures = {}
        for sw_name, _prev_time in jobs:
            cmd = [
                "docker", "run", "--rm", "--cpus=2",
                "-e", "DISPLAY=:99",
                "-v", f"{PROJECT_DIR}:/app",
                DOCKER_IMAGE,
                "python", "run-series.py", "--use-system",
                "--continue-after-failure",
                "--timeout", str(args.timeout),
                "--run-only", sw_name,
            ]
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
        description="Run ucs-detect re-run.py for each terminal YAML of the current OS")
    parser.add_argument(
        "--parallel", "-p", type=int, default=None,
        help="Number of terminals to run in parallel (default: auto)")
    parser.add_argument(
        "--timeout", "-t", type=float, default=900,
        help="Timeout per terminal in seconds (default: 900)")
    parser.add_argument(
        "--continue-after-failure", "-c", action="store_true",
        help="Continue running remaining terminals after a failure")
    parser.add_argument(
        "--host-terminal", default="ghostty",
        help="Terminal used to host subterminals (screen, tmux, etc.) "
             "(default: ghostty)")
    parser.add_argument(
        "--dry-run", "-n", action="store_true",
        help="Print what would be executed without actually running")
    parser.add_argument(
        "--keep-temp", action="store_true",
        help="Keep temporary files on exit (for debugging)")
    parser.add_argument(
        "--run-only", type=str, default="",
        help="Comma-separated list of terminal names (software_name or program) "
             "to run; all others are skipped")
    parser.add_argument(
        "--pause-exit", action="store_true",
        help="Append 'read' to run scripts so the terminal stays open on error")
    parser.add_argument(
        "--use-system", action="store_true",
        help="Run directly on the host system instead of inside Docker")
    parser.add_argument(
        "--use-docker", action="store_true",
        help="Launch each terminal in its own Docker container (--cpus=2)")
    args = parser.parse_args()

    if args.use_docker and not _IS_DOCKER:
        if not _docker_image_exists():
            _docker_build()
        _docker_per_terminal_run(args)
        return

    if not args.use_system and not _IS_DOCKER:
        if not _docker_image_exists():
            _docker_build()
        argv = sys.argv[1:]
        argv = [a for a in argv if a != "--use-system"]
        _docker_self_run(argv)

    system_name = platform.system()
    if system_name.lower() not in ("linux",):
        print(f"Error: unsupported OS '{system_name}'. Only Linux is supported.",
              file=sys.stderr)
        sys.exit(1)

    if not shutil.which("xdotool"):
        print("Warning: xdotool not found; keyboard injection will not work",
              file=sys.stderr)

    # default parallelism: max(2, min(n_cpus // 2 - 1, 16))
    if args.parallel is None:
        n_cpus = os.cpu_count() or 2
        args.parallel = max(1, min(n_cpus // 3, 8))

    mixins = load_mixins()

    host_launch_cfg, _ = get_launch_config(args.host_terminal, mixins)
    if host_launch_cfg["subterminal"]:
        print(f"Error: --host-terminal '{args.host_terminal}' is a subterminal",
              file=sys.stderr)
        sys.exit(1)

    temp_dir = Path(tempfile.mkdtemp(prefix="ucs-run-series-"))
    if not args.keep_temp:
        atexit.register(shutil.rmtree, str(temp_dir), ignore_errors=True)
    else:
        print(f"Temp directory: {temp_dir}")

    all_terminals = list(discover_yamls(system_name))
    if not all_terminals:
        print(f"No terminal YAML files found for {system_name}", file=sys.stderr)
        sys.exit(0)

    run_only = set()
    if args.run_only:
        run_only = set(n.strip().lower() for n in args.run_only.split(",") if n.strip())

    jobs = []
    skipped = []
    for d in all_terminals:

        if d.error_msg:
            skipped.append((d.software_name, d.error_msg))
            continue

        launch_cfg, is_explicit = get_launch_config(d.software_name, mixins)

        if run_only:
            name_lower = d.software_name.lower()
            prog_lower = launch_cfg.get("program", "").lower()
            file_lower = d.path.stem.lower()
            if (name_lower not in run_only
                    and prog_lower not in run_only
                    and file_lower not in run_only):
                continue

        if _should_skip(launch_cfg):
            reason = launch_cfg.get("skip_reason") or "marked skip in mixins"
            skipped.append((d.software_name, reason))
            continue

        if launch_cfg["subterminal"]:
            if not is_explicit:
                skipped.append((d.software_name, "subterminal, no launch config"))
                continue
            if host_launch_cfg is None:
                skipped.append((d.software_name, "subterminal, no host terminal available"))
                continue

        jobs.append((d.path, d.software_name, launch_cfg, d.seconds_elapsed))

    jobs.sort(key=lambda j: j[3], reverse=True)

    if skipped:
        print(f"Skipping {len(skipped)} terminals:")
        for name, reason in skipped:
            print(f"  [{name}] {reason}")
        print()

    if not jobs:
        print("No launchable terminals found.", file=sys.stderr)
        sys.exit(0)

    if args.dry_run:
        mode = "Docker" if _IS_DOCKER else "system"
        print(f"Would run {len(jobs)} terminals with --parallel={args.parallel}"
              f" ({mode} mode):\n")
        for yaml_path, sw_name, launch_cfg, _seconds_elapsed in jobs:
            safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in sw_name)
            script_path = temp_dir / f"run-{safe_name}.sh"
            if not launch_cfg["subterminal"]:
                argv = build_launch_args(launch_cfg, script_path)
            else:
                argv = build_subterminal_launch_args(launch_cfg, host_launch_cfg,
                                                     script_path)
            print(f"  {sw_name}: {shlex.join(argv)}")
        return

    profiler_sessions = {}
    try:
        from ucs_detect.profiler import ProfileSession  # noqa: F811
    except ImportError:
        ProfileSession = None  # type: ignore[assignment]

    key_jobs = [j for j in jobs if j[2].get("post_launch_keys")]
    direct_jobs = [j for j in jobs if not j[2].get("post_launch_keys")]

    mode = "Docker" if _IS_DOCKER else "system"
    print(f"Running {len(key_jobs)} key-inject + {len(direct_jobs)} direct"
          f" terminals (parallel={args.parallel}, timeout={args.timeout}s, "
          f"host={args.host_terminal}, mode={mode})")
    print(f"Temp: {temp_dir}")
    print()

    results = {}
    failures = []
    t0 = time.monotonic()

    max_workers = max(args.parallel, 1)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {}

        if key_jobs:
            print("--- Key-injection terminals (sequential launch, parallel wait) ---")
        for yaml_path, sw_name, launch_cfg, _seconds_elapsed in key_jobs:
            print(f"[{sw_name}] launching ...", flush=True)

            proc, sentinel_path, stderr_path, launch_error = _launch_and_inject(
                yaml_path, sw_name, launch_cfg, host_launch_cfg,
                temp_dir,
                pause_exit=args.pause_exit)

            if launch_error:
                results[sw_name] = (-4, launch_error)
                print(f"[{sw_name}] FAILED: {launch_error}", flush=True)
                failures.append((sw_name, -4, launch_error))
                if not args.continue_after_failure:
                    break
                continue

            profile = None
            if ProfileSession is not None and proc is not None:
                profile = ProfileSession(sw_name, proc.pid,
                    program=launch_cfg["program"] if launch_cfg["subterminal"] else None,
                    extra_programs=launch_cfg.get("profile_processes") or None)
                profile.start()

            future = executor.submit(
                _poll_sentinel, sw_name, proc, sentinel_path, stderr_path,
                args.timeout)
            future_map[future] = (sw_name, proc, profile, sentinel_path, yaml_path,
                                  launch_cfg.get("program", sw_name))

        if direct_jobs and not (failures and not args.continue_after_failure):
            if key_jobs:
                print("\n--- Direct-launch terminals (parallel) ---")
            for yaml_path, sw_name, launch_cfg, _seconds_elapsed in direct_jobs:
                proc, sentinel_path, stderr_path, launch_error = _launch_and_inject(
                    yaml_path, sw_name, launch_cfg, host_launch_cfg,
                    temp_dir,
                    pause_exit=args.pause_exit)

                if launch_error:
                    results[sw_name] = (-4, launch_error)
                    print(f"[{sw_name}] FAILED: {launch_error}", flush=True)
                    failures.append((sw_name, -4, launch_error))
                    if not args.continue_after_failure:
                        break
                    continue

                profile = None
                if ProfileSession is not None and proc is not None:
                    profile = ProfileSession(sw_name, proc.pid,
                    program=launch_cfg["program"] if launch_cfg["subterminal"] else None,
                    extra_programs=launch_cfg.get("profile_processes") or None)
                    profile.start()

                future = executor.submit(
                    _poll_sentinel, sw_name, proc, sentinel_path, stderr_path,
                    args.timeout)
                future_map[future] = (sw_name, proc, profile, sentinel_path, yaml_path,
                                      launch_cfg.get("program", sw_name))

        for future in as_completed(future_map):
            sw_name, proc, profile, sentinel_path, yaml_path, program = future_map[future]
            try:
                name, exit_code, error = future.result()
            except Exception as exc:
                results[sw_name] = (-99, str(exc))
                print(f"[{sw_name}] EXCEPTION: {exc}", flush=True)
                failures.append((sw_name, -99, str(exc)))
                if not args.continue_after_failure:
                    for f in future_map:
                        f.cancel()
                    break
                if profile is not None:
                    profile.stop()
                continue

            if profile is not None:
                profile.stop()
                profiler_sessions[name] = profile
                _embed_profile_in_yaml(yaml_path, name, profile)

            results[name] = (exit_code, error)
            if error or exit_code != 0:
                status = error or f"exit code {exit_code}"
                print(f"[{name}] FAILED: {status}", flush=True)
                failures.append((name, exit_code, error))
                if not args.continue_after_failure:
                    for f in future_map:
                        f.cancel()
                    break
            else:
                print(f"[{name}] OK", flush=True)
                _fixup_yaml(yaml_path, name, mixins, program)

    # Profile graphs and resource scores are generated by
    # scripts/make_results_rst.py during docs generation.

    elapsed = time.monotonic() - t0
    n_ok = len(results) - len(failures)
    print(f"\n--- Done in {elapsed:.1f}s: {n_ok} OK, {len(failures)} failed ---")

    if failures:
        print("\nFailures:")
        for name, exit_code, error in failures:
            msg = error or f"exit code {exit_code}"
            print(f"  {name}: {msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
