"""
Shared terminal launch machinery for the screenshot and spillover stages.

Both stages discover terminal data YAML files, resolve their launch config, start the terminal, find
its X11 window, optionally inject keys, and wait for a sentinel file written by a script running
inside the terminal.  This module holds that machinery so the stages differ only in the script they
run and the outputs they verify.
"""

# std imports
import os
import time
import uuid
import shlex
import platform
import subprocess
from pathlib import Path
from contextlib import contextmanager
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor, as_completed

# local
from ucs_detect import imaging, macos
from ucs_detect.accessories import (_KEY_INJECT_LOCK,
                                    safe_name,
                                    inject_keys,
                                    load_mixins,
                                    should_skip,
                                    docker_build,
                                    discover_yamls,
                                    window_snapshot,
                                    parse_run_only,
                                    get_project_dir,
                                    run_kill_command,
                                    build_launch_args,
                                    get_launch_config,
                                    docker_image_exists,
                                    find_window_for_command,
                                    check_unmatched_run_only,
                                    build_subterminal_launch_args)

PROJECT_DIR = get_project_dir()
DOCKER_IMAGE = 'ucs-detect:latest'

#: Titles the stage scripts set, used to pick the right window of a single-instance terminal.
STAGE_TITLE_PATTERN = r'^ucs-(shot|font|spillover)-'

#: Seconds a direct launch gets to title its own window before a pre-existing one is accepted.
STALE_WINDOW_GRACE = 4.0

#: A terminal data file paired with the launch configuration that starts it.
TerminalJob = namedtuple(
    'TerminalJob', ('yaml_path', 'software_name', 'display_name', 'launch_cfg'))


class StageError(RuntimeError):
    """Raised when a stage cannot complete."""


def mixin_key(discovered, mixins):
    """Return the terminals.yaml key matching *discovered*, or None."""
    for name in (discovered.software_name, discovered.path.stem):
        key = name.lower()
        if key in mixins:
            return key
        nospace = (key.replace(' ', '').replace('-', '')
                   .replace('_', '').replace('.', ''))
        if nospace in mixins:
            return nospace
    return None


def launch_and_entry(discovered, mixins):
    """Return the launch config and terminals.yaml entry for *discovered*."""
    key = mixin_key(discovered, mixins)
    if key is None:
        config, _explicit = get_launch_config(
            discovered.software_name, mixins)
        return config, {}
    config, _explicit = get_launch_config(key, mixins)
    return config, mixins.get(key, {})


def display_name(discovered, entry):
    """Return the display name for a terminal."""
    return entry.get('display_name', discovered.software_name)


def terminal_jobs(system_name, run_only, is_docker):
    """Return ``(jobs, skipped)`` for terminals that should be staged."""
    mixins = load_mixins()
    jobs = []
    skipped = []
    matched = set()

    for discovered in discover_yamls(system_name):
        if discovered.error_msg:
            continue
        launch_cfg, entry = launch_and_entry(discovered, mixins)
        if run_only:
            name = discovered.software_name.lower()
            program = launch_cfg.get('program', '').lower()
            if name not in run_only and program not in run_only:
                continue
            matched.update(value for value in (name, program)
                           if value in run_only)
        reason = None
        if launch_cfg['skip']:
            reason = launch_cfg.get('skip_reason') or 'marked skip'
        elif should_skip(launch_cfg, is_docker=is_docker):
            reason = launch_cfg.get('skip_reason') or 'excluded'
        elif launch_cfg['subterminal'] and not entry:
            reason = 'subterminal without launch config'
        elif (not entry
              and launch_cfg['program'] == discovered.software_name.lower()):
            reason = 'no terminals.yaml entry'
        if reason:
            skipped.append((discovered.software_name, reason))
            continue
        jobs.append(TerminalJob(
            discovered.path, discovered.software_name,
            display_name(discovered, entry), launch_cfg))

    if run_only:
        check_unmatched_run_only(run_only, matched)
    return jobs, skipped


def write_commands(path, commands, sentinel_path, stop_on_error=True,
                   log_path=None):
    """Write a POSIX shell wrapper that runs *commands* and records the exit code."""
    parts = [
        '#!/bin/sh',
        'export LANG=en_US.UTF-8',
        f'cd {shlex.quote(str(PROJECT_DIR))} || exit 1',
        'run() {',
        '    "$@"',
        '    RC=$?',
        '}',
        'RC=0',
    ]

    def command_line(command):
        line = 'run ' + ' '.join(shlex.quote(str(item)) for item in command)
        if log_path is not None:
            line += f' 2>> {shlex.quote(str(log_path))}'
        return line

    if stop_on_error:
        indent = ''
        for index, command in enumerate(commands):
            parts.append(f'{indent}{command_line(command)}')
            if index < len(commands) - 1:
                parts.append(f'{indent}if [ $RC -eq 0 ]; then')
                indent += '    '
        for _ in range(max(0, len(commands) - 1)):
            indent = indent[:-4]
            parts.append(f'{indent}fi')
    else:
        parts.append('FIRST_RC=0')
        for command in commands:
            parts.append(command_line(command))
            parts.append(
                'if [ $RC -ne 0 ] && [ $FIRST_RC -eq 0 ]; '
                'then FIRST_RC=$RC; fi')
        parts.append('if [ $RC -eq 0 ]; then RC=$FIRST_RC; fi')

    parts.extend([
        f'echo $RC > {shlex.quote(str(sentinel_path))}',
        'if [ $RC -ne 0 ]; then',
        '    read -p "Press enter to exit... " _',
        'fi',
    ])
    path.write_text('\n'.join(parts) + '\n')
    path.chmod(0o755)


def write_script(path, arguments, sentinel_path, log_path=None):
    """Write a POSIX shell wrapper that runs *arguments* and records its code."""
    write_commands(path, [arguments], sentinel_path, log_path=log_path)


def find_window(launch_cfg, host_cfg, pid, post_keys, post_delay,
                snapshot=None):
    """
    Return the X11 window id for a launched terminal, or None.

    Window lookup holds :data:`_KEY_INJECT_LOCK`, so a stage running beside another one never
    answers with the window the other one just opened.
    """
    window_cfg = host_cfg if launch_cfg['subterminal'] else launch_cfg
    timeout = (window_cfg.get('window_search_timeout_ms') or 8000) / 1000.0
    if snapshot is None:
        snapshot = window_snapshot()
    reuse_expected = bool(post_keys) or launch_cfg['subterminal']
    grace = 0.0 if reuse_expected else STALE_WINDOW_GRACE
    try:
        with _KEY_INJECT_LOCK:
            if post_keys:
                time.sleep(0.5)
                time.sleep(post_delay / 1000.0)
            return find_window_for_command(
                window_cfg, pid, timeout=timeout, pre_windows=snapshot,
                title_pattern=STAGE_TITLE_PATTERN, stale_grace=grace)
    except (subprocess.TimeoutExpired, OSError):
        return None


def launch_argv(launch_cfg, host_cfg, script_path):
    """Return the command line that starts a terminal running *script_path*."""
    if not launch_cfg['subterminal']:
        return build_launch_args(launch_cfg, script_path)
    return build_subterminal_launch_args(launch_cfg, host_cfg, script_path)


def terminal_environment(launch_cfg):
    """Return the environment for a launched terminal."""
    environment = os.environ.copy()
    for key in ('TERM', 'TERM_PROGRAM', 'TERM_PROGRAM_VERSION'):
        environment.pop(key, None)
    for key, value in launch_cfg.get('env', {}).items():
        if value == '':
            environment.pop(key, None)
        else:
            environment[key] = value
    return environment


@contextmanager
def terminal_session(process, launch_cfg):
    """Close the terminal and run its kill command on every exit path."""
    try:
        yield
    finally:
        run_kill_command(launch_cfg)
        closer = getattr(process, 'close', None)
        if closer is not None:
            try:
                closer()
            except (OSError, macos.MacOSError):
                pass
        elif process.poll() is None:
            try:
                process.kill()
            except OSError:
                pass


def wait_for_sentinel(process, sentinel_path, timeout, post_keys,
                      window_id=None):
    """
    Wait for *sentinel_path* and return its exit code, or None on timeout.

    Terminals that fork and detach outlive the launcher, so the deadline only collapses for direct
    launches, or for a key injected window that has disappeared.
    """
    deadline = time.monotonic() + timeout
    process_dead = False
    while time.monotonic() < deadline:
        if sentinel_path.exists():
            try:
                return int(sentinel_path.read_text().strip())
            except (ValueError, OSError):
                return -2
        if not process_dead and process.poll() is not None:
            process_dead = True
            window_gone = (window_id is not None
                           and imaging.window_geometry(window_id) is None)
            if not post_keys or window_gone:
                deadline = min(deadline, time.monotonic() + 30)
        time.sleep(0.3)
    return None


def read_stderr(stderr_path):
    """Return the stripped contents of *stderr_path*, or an empty string."""
    try:
        return stderr_path.read_text().strip()
    except OSError:
        return ''


def run_stage(launch_cfg, host_cfg, script_path, sentinel_path,
              stderr_path, window_id_path, timeout, max_window_size=None):
    """
    Run one terminal stage and return ``(exit_code, message)``.

    The terminal is killed and its configured kill command runs on timeout and on exception alike.
    """
    post_keys = launch_cfg.get('post_launch_keys', [])
    post_delay = launch_cfg.get('post_launch_delay_ms', 0)
    mac_config = launch_cfg.get('macos') or {}
    argv = launch_argv(launch_cfg, host_cfg, script_path)
    snapshot = window_snapshot()
    process: subprocess.Popen | macos.MacLaunch
    if mac_config:
        try:
            process = macos.launch(
                mac_config, script_path,
                launch_cfg.get('window_search_timeout_ms'))
        except macos.MacOSError as error:
            return -4, f'unable to launch: {error}'
    else:
        try:
            stderr_file = open(stderr_path, 'w')  # pylint: disable=consider-using-with
            with stderr_file:
                process = subprocess.Popen(  # pylint: disable=consider-using-with
                    argv, env=terminal_environment(launch_cfg),
                    stdout=subprocess.DEVNULL, stderr=stderr_file,
                    stdin=subprocess.DEVNULL)
        except OSError as error:
            return -4, f'unable to launch: {error}'

    with terminal_session(process, launch_cfg):
        window_id = getattr(process, 'window_id', None)
        if window_id is None:
            window_id = find_window(
                launch_cfg, host_cfg, process.pid, post_keys, post_delay,
                snapshot=snapshot)
        if window_id is not None:
            imaging.try_fullscreen(window_id, max_size=max_window_size)
            try:
                window_id_path.write_text(str(window_id))
            except OSError:
                pass

        if post_keys:
            if window_id is None:
                return -4, 'key injection failed: no window found'
            resolved = [key.replace('${SCRIPT}', str(script_path))
                        for key in post_keys]
            inject_keys(
                window_id, resolved,
                key_delay_ms=launch_cfg.get('key_delay_ms', 30),
                click_before_keys=launch_cfg.get('click_before_keys', False))
            time.sleep(1.5)

        exit_code = wait_for_sentinel(
            process, sentinel_path, timeout, post_keys, window_id)

    if exit_code is None:
        launcher_exited = process.poll() is not None
        message = ('terminal exited before sentinel' if launcher_exited
                   else 'timeout')
        text = read_stderr(stderr_path)
        if text:
            message += f' ({text})'
        return (-5 if launcher_exited else -1), message
    if exit_code != 0:
        message = f'exit code {exit_code}'
        text = read_stderr(stderr_path)
        if text:
            message += f' ({text})'
        return exit_code, message
    return 0, ''


def scaled_timeout(timeout, n_records):
    """Return the wait budget for a stage producing *n_records* outputs."""
    return timeout * max(1, n_records / 10)


def unique_title(prefix, software_name):
    """Return a unique window title for one terminal run."""
    return f'{prefix}-{safe_name(software_name)}-{uuid.uuid4().hex[:8]}'


def evidence_relative(path_value):
    """Return *path_value* relative to the project, or None when outside it."""
    path = Path(path_value)
    if not path.is_absolute():
        return str(path)
    try:
        return str(path.relative_to(PROJECT_DIR))
    except ValueError:
        print(f'Warning: {path_value} is outside the project and will not be '
              f'mounted into Docker, output is disabled inside the container')
        return None


def run_containers(software_names, script_args, parallel, container_prefix,
                   timeout, docker_args=(), image=DOCKER_IMAGE):
    """Run ``make-screenshots.py --use-system`` once per terminal in Docker."""
    failures = []

    def run_container(command, container):
        try:
            return subprocess.run(
                command, capture_output=True, text=True,
                timeout=timeout, check=False)
        except subprocess.TimeoutExpired:
            subprocess.run(['docker', 'rm', '-f', container],
                           capture_output=True, check=False)
            raise

    with ThreadPoolExecutor(max_workers=parallel) as executor:
        futures = {}
        for software_name in software_names:
            container = (f'{container_prefix}-'
                         f'{safe_name(software_name)}-{os.getpid()}')
            command = [
                'docker', 'run', '--rm', '--cpus=2',
                '--name', container,
                '-e', 'DISPLAY=:99',
                *docker_args,
                '-v', f'{PROJECT_DIR}:/app',
                image,
                'python', 'make-screenshots.py', '--use-system',
                '--run-only', software_name,
                *script_args,
            ]
            print(f'[{software_name}] docker run ...', flush=True)
            futures[executor.submit(
                run_container, command, container)] = software_name

        for future in as_completed(futures):
            software_name = futures[future]
            try:
                result = future.result()
            except Exception as error:  # pylint: disable=broad-except
                print(f'[{software_name}] EXCEPTION: {error}', flush=True)
                failures.append((software_name, -1))
                continue
            status = 'OK' if result.returncode == 0 else (
                f'exit={result.returncode}')
            print(f'[{software_name}] {status}', flush=True)
            if result.returncode != 0:
                for stream in (result.stderr, result.stdout):
                    if stream:
                        print(f'[{software_name}] {stream.strip()[:2000]}',
                              flush=True)
                failures.append((software_name, result.returncode))
    return failures


def in_docker():
    """Return True when running inside the Docker test image."""
    return os.path.exists('/.dockerenv')


def prepare_docker(image=DOCKER_IMAGE):
    """Build the Docker image when it is missing."""
    if not docker_image_exists(image):
        docker_build(PROJECT_DIR / 'Dockerfile', PROJECT_DIR, image)


#: Containers to stage at once.  Each one starts its own Xvfb, so a container never sees another
#: container's windows or focus.
DOCKER_PARALLEL = 4


def default_parallel(requested=0):
    """Return how many containers to stage at once."""
    return requested or DOCKER_PARALLEL


def selected_terminals(args, is_docker):
    """Return ``(jobs, skipped)`` for *args* using the parsed ``--run-only``."""
    return terminal_jobs(
        platform.system(), parse_run_only(args.run_only), is_docker)
