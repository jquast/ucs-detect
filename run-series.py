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

import yaml

from ucs_detect.accessories import (
    DiscoveredYAML,
    _IS_DOCKER,
    _KEY_INJECT_LOCK,
    _KEY_INJECT_PRE_DELAY,
    _KEY_INJECT_POST_DELAY,
    _RE_PAUSE,
    build_launch_args,
    build_subterminal_launch_args,
    check_unmatched_run_only,
    discover_yamls,
    docker_build,
    docker_image_exists,
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
DOCKER_IMAGE = "ucs-detect:latest"
DOCKERFILE = PROJECT_DIR / "Dockerfile"

_RE_SECONDS_ELAPSED = re.compile(r'^seconds_elapsed:\s*([\d.]+)', re.MULTILINE)


def write_run_script(script_path, yaml_path, sentinel_path,
                     pause_exit=False):
    """Write a shell script that runs re-run.py and records the exit code."""
    yaml_rel = yaml_path.relative_to(PROJECT_DIR)
    py_bin = shlex.quote(os.path.dirname(sys.executable))
    parts = [
        "#!/bin/sh",
        f"export PATH={py_bin}:$PATH",
        f"cd {shlex.quote(str(PROJECT_DIR))} || exit 1",
        f"{shlex.quote(sys.executable)} re-run.py {shlex.quote(str(yaml_rel))}",
        f"echo $? > {shlex.quote(str(sentinel_path))}",
    ]
    if pause_exit:
        parts.append('read -p "Press enter to exit..." _')
    script_path.write_text("\n".join(parts) + "\n")
    script_path.chmod(0o755)


def _launch_and_inject(yaml_path, sw_name, launch_cfg, host_launch_cfg,
                       temp_dir, pause_exit=False):
    """Launch a terminal and inject keys. Does not wait for completion.

    Returns (proc, sentinel_path, stderr_path, error_msg).
    """
    safe = safe_name(sw_name)
    script_path = temp_dir / f"run-{safe}.sh"
    sentinel_path = temp_dir / f"exit-{safe}.rc"
    stderr_path = temp_dir / f"stderr-{safe}.log"
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

        if not _IS_DOCKER and platform.system().lower() == "linux":
            argv = ["systemd-run", "--user", "--scope",
                    "-p", "CPUQuota=200%", "--"] + argv

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
                # In Docker, the host terminal is our xterm, not the host's TERM_PROGRAM
                if _IS_DOCKER and launch_cfg["subterminal"]:
                    window_cfg = dict(window_cfg, wm_class="XTerm")
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


def _poll_sentinel(sw_name, proc, sentinel_path, stderr_path, timeout,
                   post_keys=None):
    """Wait for sentinel file.  Returns (sw_name, exit_code, error_msg).

    When *post_keys* is truthy, the deadline is not collapsed on process
    exit because key-inject terminals (Hyper, Extraterm, Warp) fork/detach
    and the launcher process exits immediately."""
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

        if not post_keys and not proc_dead and proc.poll() is not None:
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
    from ucs_detect.accessories import _atomic_yaml_dump
    data["resource_profile"]["hardware"] = hardware_info()
    try:
        _atomic_yaml_dump(data, yaml_path, default_flow_style=False,
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
    if not entry:
        stem_key = yaml_path.stem.lower()
        if stem_key != key:
            entry = mixins.get(stem_key, {})
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
        # resolve {aur_version} from pacman if aur_package is configured
        aur_version = ""
        aur_pkg = entry.get("aur_package")
        if aur_pkg:
            try:
                result = subprocess.run(
                    ["pacman", "-Q", aur_pkg],
                    capture_output=True, text=True, timeout=5,
                )
                if result.returncode == 0:
                    # "aur_pkg 1.2.3-4" -> "1.2.3-4"
                    parts = result.stdout.strip().split(None, 1)
                    if len(parts) > 1:
                        aur_version = parts[1]
            except (subprocess.TimeoutExpired, OSError):
                pass
        version_str = version_template.format(
            sw_name=raw_name,
            sw_version=raw_version,
            xt_name=xt_name,
            xt_version=xt_version,
            xtversion_raw=raw_xtversion,
            release=entry.get("version_release", ""),
            aur_version=aur_version,
        )
        data["software_version"] = version_str

    version_manual = entry.get("version_manual")
    if version_manual and not data.get("software_version"):
        data["software_version"] = version_manual

    try:
        from ucs_detect.accessories import _atomic_yaml_dump
        _atomic_yaml_dump(data, yaml_path, default_flow_style=False,
                          allow_unicode=True)
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
    run_only = parse_run_only(args.run_only)
    matched_run_only = set()

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
            for candidate in (name_lower, prog_lower):
                if candidate in run_only:
                    matched_run_only.add(candidate)
        if not run_only and should_skip(launch_cfg, is_docker=True):
            continue
        if launch_cfg.get("subterminal") and not launch_cfg.get("program"):
            continue
        jobs.append((d.software_name, d.seconds_elapsed, launch_cfg.get("timeout")))

    jobs.sort(key=lambda j: j[1], reverse=True)

    if run_only:
        check_unmatched_run_only(run_only, matched_run_only)

    n_cpus = os.cpu_count() or 2
    parallel = max(1, min((n_cpus - 2) // 2, 16))

    print(f"Per-terminal Docker: {len(jobs)} terminals, {parallel} parallel "
          f"(cpus={n_cpus}, timeout={args.timeout}s)")

    with ThreadPoolExecutor(max_workers=parallel) as executor:
        futures = {}
        for sw_name, _prev_time, term_timeout in jobs:
            cmd = [
                "docker", "run", "--rm", "--cpus=2",
                "-e", "DISPLAY=:99",
                "-v", f"{PROJECT_DIR}:/app",
                DOCKER_IMAGE,
                "python", "run-series.py", "--use-system",
                "--continue-after-failure",
                "--timeout", str(term_timeout or args.timeout),
                "--run-only", sw_name,
            ]
            future = executor.submit(subprocess.run, cmd, capture_output=True,
                                     text=True, timeout=(term_timeout or args.timeout) + 60)
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
        if not docker_image_exists():
            docker_build(DOCKERFILE, PROJECT_DIR)
        _docker_per_terminal_run(args)
        return

    if not args.use_system and not _IS_DOCKER:
        if not docker_image_exists():
            docker_build(DOCKERFILE, PROJECT_DIR)
        argv = sys.argv[1:]
        argv = [a for a in argv if a != "--use-system"]
        _docker_self_run(argv)

    system_name = platform.system()
    if system_name.lower() not in ("linux", "darwin"):
        print(f"Error: unsupported OS '{system_name}'. Only Linux and macOS are supported.",
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

    run_only = parse_run_only(args.run_only)
    matched_run_only = set()

    jobs = []
    skipped = []
    for d in all_terminals:

        if d.error_msg:
            skipped.append((d.software_name, d.error_msg))
            continue

        launch_cfg, is_explicit = get_launch_config(d.software_name, mixins)
        if not is_explicit:
            launch_cfg, is_explicit = get_launch_config(d.path.stem, mixins)

        if run_only:
            name_lower = d.software_name.lower()
            prog_lower = launch_cfg.get("program", "").lower()
            file_lower = d.path.stem.lower()
            if (name_lower not in run_only
                    and prog_lower not in run_only
                    and file_lower not in run_only):
                continue
            for candidate in (name_lower, prog_lower, file_lower):
                if candidate in run_only:
                    matched_run_only.add(candidate)

        if not run_only and should_skip(launch_cfg):
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

    if run_only:
        check_unmatched_run_only(run_only, matched_run_only)

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
            safe = safe_name(sw_name)
            script_path = temp_dir / f"run-{safe}.sh"
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
                    program=launch_cfg["program"],
                    extra_programs=launch_cfg.get("profile_processes") or None)
                profile.start()

            term_timeout = launch_cfg.get("timeout") or args.timeout
            post_keys = launch_cfg.get("post_launch_keys")
            future = executor.submit(
                _poll_sentinel, sw_name, proc, sentinel_path, stderr_path,
                term_timeout, post_keys=post_keys)
            future_map[future] = (
                sw_name, proc, profile, sentinel_path, yaml_path,
                launch_cfg.get("program", sw_name), launch_cfg)

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
                        program=launch_cfg["program"],
                        extra_programs=launch_cfg.get("profile_processes") or None)
                    profile.start()

                term_timeout = launch_cfg.get("timeout") or args.timeout
                post_keys = launch_cfg.get("post_launch_keys")
                future = executor.submit(
                    _poll_sentinel, sw_name, proc, sentinel_path, stderr_path,
                    term_timeout, post_keys=post_keys)
                future_map[future] = (
                    sw_name, proc, profile, sentinel_path, yaml_path,
                    launch_cfg.get("program", sw_name), launch_cfg)

        for future in as_completed(future_map):
            sw_name, proc, profile, sentinel_path, yaml_path, program, launch_cfg = future_map[future]
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
                run_kill_command(launch_cfg)
                if not args.continue_after_failure:
                    for f in future_map:
                        f.cancel()
                    break
            else:
                print(f"[{name}] OK", flush=True)
                _fixup_yaml(yaml_path, name, mixins, program)
                run_kill_command(launch_cfg)

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
