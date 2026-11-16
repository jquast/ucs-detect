"""Shared utility functions used across scripts and the ucs_detect package."""

from __future__ import annotations

# std imports
import os
import re
import sys
import time
import fcntl
import shlex
import tempfile
import threading
import contextlib
import subprocess
from pathlib import Path

from typing import NamedTuple

# 3rd party
import yaml

# local
from ucs_detect import macos

try:
    # The libyaml backed loader is several times faster on the multi-megabyte terminal data
    # files, and PyYAML only exposes it when it was built with it.
    # 3rd party
    from yaml import CSafeLoader as SafeLoader
except ImportError:  # pragma: no cover
    # 3rd party
    from yaml import SafeLoader

_RE_SYSTEM = re.compile(r'^system:\s*(\S+)', re.MULTILINE)
_RE_SOFTWARE_NAME = re.compile(r'^software_name:\s*(.+)$', re.MULTILINE)
_RE_SECONDS_ELAPSED = re.compile(r'^seconds_elapsed:\s*([-\d.eE+]+)', re.MULTILINE)
_RE_PAUSE = re.compile(r'^\\p(\d+)$')
_RE_KEY = re.compile(r'^\\k(\S+)$')


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


def load_document(path):
    """
    Return the YAML document at *path* as a dict, or an empty dict.

    Terminal data files reach 2.7 MB, where the pure Python loader costs four seconds per parse.
    """
    with open(path, encoding="utf-8") as stream:
        return yaml.load(stream, Loader=SafeLoader) or {}


FETCH_BLOCKSIZE = 3096


def do_retrieve(url, fname, force=False):
    """
    Retrieve *url* to *fname*, re-downloading a cached copy when *force* is set.

    Callers fetching a "latest" URL must set *force*: those files are re-issued with each Unicode
    release and a cached copy pins the tables to whichever version was current.
    """
    # 3rd party
    import requests
    folder = os.path.dirname(fname)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    if os.path.exists(fname) and not force:
        return
    resp = requests.get(url, stream=True, timeout=30)
    with open(fname, "wb") as fout:
        for chunk in resp.iter_content(FETCH_BLOCKSIZE):
            fout.write(chunk)


def safe_name(name):
    """Return a filesystem-safe version of *name*."""
    return "".join(c if c.isalnum() or c in "-_" else "_" for c in name)


def decode_wchars(escaped):
    r"""Decode a ``\u0915`` style escape sequence to text."""
    return bytes(escaped, "utf-8").decode("unicode-escape")


def load_mixins(project_dir=None):
    """Load terminals.yaml, keyed by software name, display name, and filename forms."""
    if project_dir is None:
        project_dir = Path(__file__).resolve().parent.parent
    mixins_path = project_dir / "terminals.yaml"
    if not mixins_path.exists():
        return {}
    data = load_document(mixins_path)
    terminals = data.get("terminals", {})

    def alias(name, value):
        result.setdefault(name.lower(), value)
        # Also index by filename-friendly form (no spaces/hyphens/underscores/dots)
        nospace = (name.lower().replace(" ", "").replace("-", "")
                   .replace("_", "").replace(".", ""))
        if nospace != name.lower():
            result.setdefault(nospace, value)

    result = {}
    for key, value in terminals.items():
        result[key.lower()] = value
        alias(key, value)
        display_name = value.get("display_name")
        if display_name:
            alias(display_name, value)
    return result


def _scalar(text):
    value = text.strip()
    if value[:1] in ("'", '"'):
        try:
            return yaml.load(f"value: {value}", Loader=SafeLoader)["value"]
        except yaml.YAMLError:
            return value.strip("'\"")
    return value


def discover_yamls(target_system, data_dir=None):
    """
    Yield DiscoveredYAML for each data YAML matching *target_system*.

    The corpus is 39 MB: reading the three top level keys costs a second where parsing
    every document costs eleven.
    """
    if data_dir is None:
        data_dir = Path(__file__).resolve().parent.parent / "data"
    target_lower = target_system.lower()
    for yaml_path in sorted(data_dir.glob("*.yaml")):
        if yaml_path.name.startswith("_"):
            continue
        try:
            text = yaml_path.read_text(encoding="utf-8")
        except OSError:
            continue

        system = _RE_SYSTEM.search(text)
        if not system or _scalar(system.group(1)).lower() != target_lower:
            continue

        name = _RE_SOFTWARE_NAME.search(text)
        sw_name = _scalar(name.group(1)) if name else yaml_path.stem
        elapsed = _RE_SECONDS_ELAPSED.search(text)
        try:
            seconds_elapsed = float(elapsed.group(1)) if elapsed else 0.0
        except ValueError:
            seconds_elapsed = 0.0
        yield DiscoveredYAML(yaml_path, sw_name, seconds_elapsed, None)


def get_launch_config(sw_name, mixins, is_docker=None):
    """Return (launch_config, is_explicit) for *sw_name*."""
    if is_docker is None:
        is_docker = os.path.exists("/.dockerenv")
    key = sw_name.lower()
    raw_entry = mixins.get(key, {})
    launch = raw_entry.get("launch") if raw_entry else None
    if launch is None:
        launch = {}

    if is_docker and raw_entry.get("launch_docker"):
        launch = raw_entry["launch_docker"]
    elif not is_docker and raw_entry.get("launch_system"):
        launch = raw_entry["launch_system"]

    is_explicit = bool(launch)

    skip_system = raw_entry.get("skip_system", False) or launch.get("skip_system", False)
    skip_docker = raw_entry.get("skip_docker", False) or launch.get("skip_docker", False)
    skip_any = raw_entry.get("skip", False) or launch.get("skip", False)
    skip_screenshots = (raw_entry.get("skip_screenshots", False)
                        or launch.get("skip_screenshots", False))
    skip_spillover = (raw_entry.get("skip_spillover", False)
                      or launch.get("skip_spillover", False))
    skip_colors = (raw_entry.get("skip_colors", skip_spillover)
                   or launch.get("skip_colors", False))
    skip_bidi = (raw_entry.get("skip_bidi", skip_spillover)
                 or launch.get("skip_bidi", False))

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
        "skip_screenshots": skip_screenshots,
        "skip_spillover": skip_spillover,
        "skip_colors": skip_colors,
        "skip_bidi": skip_bidi,
        "skip_reason": raw_entry.get("skip_reason", ""),
        "skip_screenshots_reason": raw_entry.get("skip_screenshots_reason", ""),
        "skip_spillover_reason": raw_entry.get("skip_spillover_reason", ""),
        "skip_colors_reason": raw_entry.get("skip_colors_reason", ""),
        "skip_bidi_reason": raw_entry.get("skip_bidi_reason",
                                          raw_entry.get("skip_spillover_reason", "")),
        "post_launch_delay_ms": launch.get("post_launch_delay_ms", 0),
        "post_launch_keys": launch.get("post_launch_keys", []),
        "env": launch.get("env", {}),
        "profile_processes": raw_entry.get("profile_processes", []),
        "timeout": raw_entry.get("timeout", None),
        "wm_class": launch.get("wm_class", None),
        "window_search_timeout_ms": launch.get("window_search_timeout_ms"),
        "click_before_keys": launch.get("click_before_keys", False),
        "kill_command": launch.get("kill_command"),
        "screenshot_delay_ms": raw_entry.get(
            "screenshot_delay_ms", launch.get("screenshot_delay_ms", 0)),
        "spillover_rtl": raw_entry.get(
            "spillover_rtl", launch.get("spillover_rtl", True)),
        "macos": launch.get("macos") or raw_entry.get("macos") or {},
        "cursor_center_rows": raw_entry.get(
            "cursor_center_rows", launch.get("cursor_center_rows", 0)),
    }
    return cfg, is_explicit


def build_launch_args(launch_cfg, script_path):
    """Build the full argv list for launching a terminal that executes *script_path*."""
    argv = list(launch_cfg["wrapper"])
    argv.append(launch_cfg["program"])
    script_str = str(script_path)
    has_placeholder = False
    for arg in launch_cfg["args"]:
        arg = str(arg)
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
    inner_parts = [launch_cfg["program"]] + [
        str(arg) for arg in launch_cfg["args"]]
    has_placeholder = any("{script}" in a for a in inner_parts)
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


def largest_window(window_ids):
    """Return the largest window from *window_ids*."""
    best = None
    best_area = -1
    for window_id in window_ids:
        try:
            result = subprocess.run(
                ["xdotool", "getwindowgeometry", "--shell", window_id],
                capture_output=True, text=True, timeout=3, check=False,
            )
        except (subprocess.TimeoutExpired, OSError):
            continue
        width = height = 0
        for line in result.stdout.splitlines():
            if line.startswith("WIDTH="):
                width = int(line.split("=", 1)[1] or 0)
            elif line.startswith("HEIGHT="):
                height = int(line.split("=", 1)[1] or 0)
        area = width * height
        if area > best_area:
            best_area = area
            best = window_id
    return best or list(window_ids)[-1]


def _matching_window_ids(argv):
    try:
        result = subprocess.run(
            argv, capture_output=True, text=True, timeout=3, check=False)
    except (subprocess.TimeoutExpired, OSError):
        return []
    if result.returncode != 0 or not result.stdout.strip():
        return []
    return result.stdout.split()


def _prefer_new_window(window_ids, pre_windows):
    if pre_windows:
        new = [window_id for window_id in window_ids
               if window_id not in pre_windows]
        if new:
            return largest_window(new)
    return largest_window(window_ids)


def _window_class_pattern(name):
    return f'^{re.escape(name)}(-.*)?$'


def window_snapshot():
    """Return the set of visible window ids, or None."""
    if macos.IS_MACOS:
        return {item['id'] for item in macos.windows()}
    try:
        result = subprocess.run(
            ['xdotool', 'search', '--onlyvisible', ''],
            capture_output=True, text=True, timeout=3, check=False)
    except (subprocess.TimeoutExpired, OSError):
        return None
    if result.returncode != 0:
        return None
    return set(result.stdout.strip().split('\n'))


def find_window_for_command(launch_cfg, pid, timeout=8, pre_windows=None,
                            title_pattern=None, stale_grace=0.0):
    """Find the window of a launched process, by title, PID, class, or new window."""
    if macos.IS_MACOS:
        owner = macos.app_owner(launch_cfg["macos"]) if launch_cfg.get(
            "macos") else os.path.basename(launch_cfg.get("program", ""))
        if not owner:
            owner = launch_cfg.get("wm_class") or ""
        return macos.find_window(
            owner, exclude=pre_windows or (), title_pattern=title_pattern,
            timeout=timeout, stale_grace=stale_grace)
    deadline = time.monotonic() + timeout
    started = time.monotonic()
    wm_class = launch_cfg.get("wm_class") or os.path.basename(
        launch_cfg.get("program", "")
    )
    class_names = list(dict.fromkeys(
        [_window_class_pattern(wm_class.lower()),
         _window_class_pattern(wm_class),
         _window_class_pattern(wm_class.capitalize())]))

    while time.monotonic() < deadline:
        if title_pattern:
            windows = _matching_window_ids(
                ["xdotool", "search", "--onlyvisible",
                 "--name", title_pattern])
            if windows:
                return _prefer_new_window(windows, pre_windows)

        if time.monotonic() - started < stale_grace:
            time.sleep(0.3)
            continue

        windows = _matching_window_ids(
            ["xdotool", "search", "--onlyvisible", "--pid", str(pid)])
        if windows:
            return _prefer_new_window(windows, pre_windows)

        for name in class_names:
            for flag in ("--class", "--classname"):
                windows = _matching_window_ids(
                    ["xdotool", "search", "--onlyvisible", flag, name])
                if windows:
                    return _prefer_new_window(windows, pre_windows)

        if pre_windows is not None:
            current = set(_matching_window_ids(
                ["xdotool", "search", "--onlyvisible", ""]))
            new = current - pre_windows
            if new:
                return largest_window(new)

        time.sleep(0.3)

    if os.path.exists("/.dockerenv"):
        windows = _matching_window_ids(
            ["xdotool", "search", "--onlyvisible", ""])
        if windows:
            return largest_window(windows)

    return None


def _xdotool(argv, timeout, text=False):
    try:
        return subprocess.run(
            argv, capture_output=True, text=text, timeout=timeout,
            check=False)
    except (subprocess.TimeoutExpired, OSError):
        return None


#: Nesting depth and file handle of :func:`display_lock`, and the thread lock behind it.
_DISPLAY_LOCK_DEPTH = 0
_DISPLAY_LOCK_HANDLE = None
_DISPLAY_LOCK = threading.RLock()


def display_lock_path():
    """Return the lock file every process driving this X display shares."""
    display = os.environ.get("DISPLAY", "")
    safe = re.sub(r"[^0-9A-Za-z_.-]", "_", display) or "local"
    return os.path.join(tempfile.gettempdir(), f"ucs-display-{safe}.lock")


@contextlib.contextmanager
def display_lock():
    """Hold this process's turn on the X display."""
    global _DISPLAY_LOCK_DEPTH, _DISPLAY_LOCK_HANDLE
    with _DISPLAY_LOCK:
        if _DISPLAY_LOCK_DEPTH == 0:
            _DISPLAY_LOCK_HANDLE = open(
                display_lock_path(), "a", encoding="utf-8")
            fcntl.flock(_DISPLAY_LOCK_HANDLE, fcntl.LOCK_EX)
        _DISPLAY_LOCK_DEPTH += 1
        try:
            yield
        finally:
            _DISPLAY_LOCK_DEPTH -= 1
            if _DISPLAY_LOCK_DEPTH == 0:
                fcntl.flock(_DISPLAY_LOCK_HANDLE, fcntl.LOCK_UN)
                _DISPLAY_LOCK_HANDLE.close()
                _DISPLAY_LOCK_HANDLE = None


def inject_keys(window_id, keys, key_delay_ms=30, click_before_keys=False):
    """Send keystrokes to a window via xdotool."""
    if macos.IS_MACOS:
        return macos.inject_keys(
            window_id, keys, key_delay_ms=key_delay_ms,
            click_before_keys=click_before_keys)
    with display_lock():
        activated = _xdotool(
            ["xdotool", "windowactivate", "--sync", str(window_id)], 5)
        if activated is None or activated.returncode != 0:
            _xdotool(
                ["xdotool", "windowfocus", "--sync", str(window_id)], 2)
        time.sleep(0.2)

        if click_before_keys:
            width, height = 0, 0
            geometry = _xdotool(
                ["xdotool", "getwindowgeometry", "--shell", str(window_id)],
                3, text=True)
            if geometry is not None:
                try:
                    values = dict(
                        line.split("=", 1)
                        for line in geometry.stdout.splitlines() if "=" in line
                    )
                    width = int(values.get("WIDTH", 0))
                    height = int(values.get("HEIGHT", 0))
                except ValueError:
                    pass
            _xdotool(
                ["xdotool", "mousemove", "--window", str(window_id),
                 str(width // 2 if width else 40),
                 str(height // 2 if height else 40), "click", "1"], 5)
            time.sleep(0.2)

        _xdotool(
            ["xdotool", "windowfocus", "--sync", str(window_id)], 2)
        time.sleep(0.3)
        delay_str = str(key_delay_ms)
        merged = []
        for key in keys:
            if (key in ("\n", "\\n") or _RE_PAUSE.match(key)
                    or _RE_KEY.match(key)):
                if merged:
                    combined = "".join(merged)
                    _xdotool(
                        ["xdotool", "type", "--delay", delay_str, combined],
                        120)
                    merged = []
                if key in ("\n", "\\n"):
                    _xdotool(["xdotool", "key", "Return"], 5)
                elif _RE_PAUSE.match(key):
                    ms = int(_RE_PAUSE.match(key).group(1))
                    time.sleep(ms / 1000.0)
                else:
                    combo = _RE_KEY.match(key).group(1)
                    _xdotool(["xdotool", "key", combo], 5)
            else:
                merged.append(key)
        if merged:
            combined = "".join(merged)
            _xdotool(["xdotool", "type", "--delay", delay_str, combined], 120)


def _atomic_yaml_dump(data, path, **dump_kwargs):
    tmp_path = str(path) + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, **dump_kwargs)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)


def fixup_yaml(yaml_path, sw_name, mixins, program):
    """Fix up software_name in YAML from raw XTVERSION values to display names."""
    key = sw_name.lower()
    entry = mixins.get(key, {})
    if not entry:
        stem_key = yaml_path.stem.lower()
        if stem_key != key:
            entry = mixins.get(stem_key, {})
    display_name = entry.get("display_name")
    version_template = entry.get("version_template")

    data = load_document(yaml_path)
    if not data:
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
                    check=False,
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

    _atomic_yaml_dump(data, yaml_path, default_flow_style=False,
                      allow_unicode=True)


_IS_DOCKER = os.path.exists("/.dockerenv")

_KEY_INJECT_LOCK = threading.RLock()
_KEY_INJECT_PRE_DELAY = 0.5
_KEY_INJECT_POST_DELAY = 1.5


def should_skip(launch_cfg, is_docker=None):
    """Return True if the config should be skipped in the current environment."""
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
