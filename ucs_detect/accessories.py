"""Shared utility functions used across scripts and the ucs_detect package."""

# std imports
import os
import re
import sys
import time
import shlex
import threading
import subprocess
from pathlib import Path

from typing import NamedTuple

# 3rd party
import yaml

_RE_SYSTEM = re.compile(r'^system:\s*(\S+)', re.MULTILINE)
_RE_SOFTWARE_NAME = re.compile(r'^software_name:\s*(.+)', re.MULTILINE)
_RE_PAUSE = re.compile(r'^\\p(\d+)$')


class DiscoveredYAML(NamedTuple):
    """A YAML data file discovered by discover_yamls."""

    path: Path
    software_name: str
    seconds_elapsed: float = 0.0
    error_msg: str | None = None


def find_best_failure(records):
    """Find the midpoint failure from a list of failure records."""
    if not records:
        return None
    sorted_records = sorted(records, key=lambda r: r.get("measured_by_wcwidth", 0))
    return sorted_records[len(sorted_records) // 2]


def get_project_dir():
    """Return the project root directory (parent of the ucs_detect package)."""
    return Path(__file__).resolve().parent.parent


def get_data_dir():
    """Return the data directory under the project root."""
    return get_project_dir() / "data"


FETCH_BLOCKSIZE = 3096


def do_retrieve(url, fname):
    """Retrieve given url to target filepath fname."""
    # 3rd party
    import requests
    folder = os.path.dirname(fname)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    if os.path.exists(fname):
        return
    resp = requests.get(url, stream=True, timeout=30)
    with open(fname, "wb") as fout:
        for chunk in resp.iter_content(FETCH_BLOCKSIZE):
            fout.write(chunk)


def safe_name(name):
    """Return a filesystem-safe version of *name*."""
    return "".join(c if c.isalnum() or c in "-_" else "_" for c in name)


def decode_wchars(escaped):
    r"""Decode a unicode-escape-encoded string like ``\\u0915`` to the actual unicode text."""
    return bytes(escaped, "utf-8").decode("unicode-escape")


def load_mixins(project_dir=None):
    """Load terminals.yaml, returning a dict keyed by lowercased software_name."""
    if project_dir is None:
        project_dir = Path(__file__).resolve().parent.parent
    mixins_path = project_dir / "terminals.yaml"
    if not mixins_path.exists():
        return {}
    with open(mixins_path) as f:
        data = yaml.safe_load(f) or {}
    terminals = data.get("terminals", {})
    result = {}
    for key, value in terminals.items():
        result[key.lower()] = value
        # Also index by filename-friendly form (no spaces/hyphens/underscores/dots)
        nospace = key.lower().replace(" ", "").replace("-", "").replace("_", "").replace(".", "")
        if nospace != key.lower():
            result.setdefault(nospace, value)
    return result


def discover_yamls(target_system, data_dir=None):
    """Yield DiscoveredYAML for each data YAML matching *target_system*."""
    if data_dir is None:
        data_dir = Path(__file__).resolve().parent.parent / "data"
    target_lower = target_system.lower()
    for yaml_path in sorted(data_dir.glob("*.yaml")):
        if yaml_path.name == "terminals.yaml":
            continue
        try:
            with open(yaml_path) as f:
                data = yaml.safe_load(f) or {}
        except (OSError, yaml.YAMLError):
            continue

        system = data.get("system", "")
        if system.lower() != target_lower:
            continue

        sw_name = data.get("software_name", yaml_path.stem)
        seconds_elapsed = data.get("seconds_elapsed", 0.0)
        yield DiscoveredYAML(yaml_path, sw_name, seconds_elapsed, None)


def get_launch_config(sw_name, mixins, is_docker=None):
    """Return (launch_config, is_explicit) for *sw_name*."""
    if is_docker is None:
        is_docker = os.path.exists("/.dockerenv")
    key = sw_name.lower()
    raw_entry = mixins.get(key, {})
    launch = raw_entry.get("launch", {}) if raw_entry else {}

    if is_docker and raw_entry.get("launch_docker"):
        launch = raw_entry["launch_docker"]
    elif not is_docker and raw_entry.get("launch_system"):
        launch = raw_entry["launch_system"]

    is_explicit = bool(launch)

    skip_system = raw_entry.get("skip_system", False) or launch.get("skip_system", False)
    skip_docker = raw_entry.get("skip_docker", False) or launch.get("skip_docker", False)
    skip_any = launch.get("skip", False)

    wrapper = list(launch.get("wrapper", []))
    if is_docker and skip_system and wrapper:
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
        "timeout": raw_entry.get("timeout", None),
        "wm_class": launch.get("wm_class", None),
    }
    return cfg, is_explicit


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
    """
    Find X11 window ID for a launched process, by PID then by class name.

    If *pre_windows* is a set of window IDs that existed before the process was launched, any new
    window (not in the set) is returned as a last-resort fallback.
    """
    deadline = time.monotonic() + timeout

    # Strategy 1: search by PID
    pid_deadline = time.monotonic() + min(timeout / 2, 5)
    while time.monotonic() < pid_deadline:
        try:
            result = subprocess.run(
                ["xdotool", "search", "--onlyvisible", "--pid", str(pid)],
                capture_output=True, text=True, timeout=3, check=False,
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
                    capture_output=True, text=True, timeout=3, check=False,
                )
                if result.returncode == 0 and result.stdout.strip():
                    return result.stdout.strip().split("\n")[-1]
            except (subprocess.TimeoutExpired, OSError):
                pass
        time.sleep(0.3)

    # Strategy 3: find any new window that appeared since pre_windows snapshot
    if pre_windows is not None:
        while time.monotonic() < deadline:
            try:
                result = subprocess.run(
                    ["xdotool", "search", "--onlyvisible", ""],
                    capture_output=True, text=True, timeout=3, check=False,
                )
                if result.returncode == 0:
                    current = set(result.stdout.strip().split("\n"))
                    new = current - pre_windows
                    if new:
                        return max(new, key=int)
            except (subprocess.TimeoutExpired, OSError):
                pass
            time.sleep(0.3)

    # Strategy 4: any visible window (Docker only)
    if os.path.exists("/.dockerenv"):
        try:
            result = subprocess.run(
                ["xdotool", "search", "--onlyvisible", ""],
                capture_output=True, text=True, timeout=3, check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                windows = result.stdout.strip().split("\n")
                return windows[-1]
        except (subprocess.TimeoutExpired, OSError):
            pass

    return None


def inject_keys(window_id, keys):
    r"""
    Send keystrokes to a window via xdotool.

    Special tokens:
      ``\\n``       press Return
      ``\\pNNN``    pause for NNN milliseconds
    """
    subprocess.run(
        ["xdotool", "windowfocus", "--sync", str(window_id)],
        capture_output=True, timeout=2, check=False,
    )
    time.sleep(0.3)
    merged = []
    for key in keys:
        if key in ("\n", "\\n") or _RE_PAUSE.match(key):
            if merged:
                combined = "".join(merged)
                subprocess.run(
                    ["xdotool", "type", "--delay", "30", combined],
                    capture_output=True, timeout=120, check=False,
                )
                merged = []
            if key in ("\n", "\\n"):
                subprocess.run(
                    ["xdotool", "key", "Return"],
                    capture_output=True, timeout=5, check=False,
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
            capture_output=True, timeout=120, check=False,
        )


def _atomic_yaml_dump(data, path, **dump_kwargs):
    """Write *data* as YAML to *path* atomically."""
    tmp_path = str(path) + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, **dump_kwargs)
            f.flush()
            os.fsync(f.fileno())
        os.rename(tmp_path, path)
    except Exception:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def fixup_yaml(yaml_path, sw_name, mixins, program):
    """Fix up software_name in YAML from raw XTVERSION values to display names.

    When ucs-detect runs without operator override, the auto-detected
    ``software_name`` is the raw XTVERSION response (e.g. ``VTE`` for
    VTE-based terminals).  This function reads the YAML and corrects
    ``software_name`` to the display name from ``terminals.yaml``.  If a
    ``version_template`` is present, the ``software_version`` is also composed.

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
        aur_version = ""
        aur_pkg = entry.get("aur_package")
        if aur_pkg:
            try:
                result = subprocess.run(
                    ["pacman", "-Q", aur_pkg],
                    capture_output=True, text=True, timeout=5,
                )
                if result.returncode == 0:
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
        if version_str:
            data["software_version"] = version_str

    version_manual = entry.get("version_manual")
    if version_manual and not data.get("software_version"):
        data["software_version"] = version_manual

    try:
        _atomic_yaml_dump(data, yaml_path, default_flow_style=False,
                          allow_unicode=True)
    except OSError:
        pass


_IS_DOCKER = os.path.exists("/.dockerenv")

_KEY_INJECT_LOCK = threading.RLock()
_KEY_INJECT_PRE_DELAY = 0.5
_KEY_INJECT_POST_DELAY = 1.5


def should_skip(launch_cfg, is_docker=None):
    """
    Return True if the config should be skipped in the current environment.

    If *is_docker* is None, uses the process environment (_IS_DOCKER).
    Docker runs terminals with skip_docker: false; system runs the rest
    (skip_docker: true).  Both respect skip and skip_system.
    """
    if is_docker is None:
        is_docker = _IS_DOCKER
    if launch_cfg["skip"]:
        return True
    if is_docker and launch_cfg["skip_docker"]:
        return True
    if not is_docker and not launch_cfg["skip_docker"]:
        return True
    if not is_docker and launch_cfg["skip_system"]:
        return True
    return False


def run_kill_command(launch_cfg):
    """Execute kill_command from launch config to clean up a terminal process."""
    kill_cmd = launch_cfg.get("kill_command")
    if not kill_cmd:
        return
    try:
        subprocess.run(kill_cmd, timeout=5, capture_output=True, check=False)
    except (subprocess.TimeoutExpired, OSError):
        pass


def docker_image_exists(image="ucs-detect:latest"):
    """Check if the Docker image is already built."""
    try:
        result = subprocess.run(
            ["docker", "images", "-q", image],
            capture_output=True, text=True, timeout=10, check=False,
        )
        return bool(result.stdout.strip())
    except (subprocess.TimeoutExpired, OSError):
        return False


def docker_build(dockerfile, project_dir, image="ucs-detect:latest"):
    """Build the Docker image."""
    print(f"Building Docker image {image} ...", flush=True)
    env = os.environ.copy()
    env.setdefault("DOCKER_BUILDKIT", "1")
    subprocess.check_call(
        ["docker", "build", "-f", str(dockerfile), "-t", image, str(project_dir)],
        env=env,
    )


def parse_run_only(raw):
    """Parse --run-only comma-separated string into a set of lowercased names."""
    return set(n.strip().lower() for n in raw.split(",") if n.strip()) if raw else set()


def check_unmatched_run_only(run_only, matched):
    """Exit with error if any *run_only* names were not matched."""
    unmatched = run_only - matched
    if unmatched:
        print(f"Error: --run-only names not found: {', '.join(sorted(unmatched))}",
              file=sys.stderr)
        raise SystemExit(2)
