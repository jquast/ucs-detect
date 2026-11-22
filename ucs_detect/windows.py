"""
Window capture of a native Windows terminal, for ucs-detect running under WSL.

The terminal under test is a Windows program, so the X11 tools cannot see it.  WSL can run
Windows programs, so one ``powershell.exe`` helper (``windows_capture.ps1``) is started and kept
running: it finds the window by the title ucs-detect sets, and captures its client area to a
PNG with ``PrintWindow``.  Window ids are Windows window handles, written in decimal.

Used when running under WSL with ``powershell.exe`` reachable; set ``UCS_DETECT_CAPTURE=x11`` to
use the X11 tools instead.  A WSL login appends the Windows PATH, an ssh login into WSL does not,
so ``powershell.exe`` is also looked for on the mounted Windows drives.
"""

# std imports
import os
import re
import sys
import time
import select
import shutil
import atexit
import threading
import subprocess

#: Seconds the helper is given to compile its native calls and say it is ready.
STARTUP_TIMEOUT = 60

#: Seconds one request is given before the helper is presumed stuck.
REQUEST_TIMEOUT = 20

_SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'windows_capture.ps1')


#: Where powershell.exe lives on the Windows system drive.
_POWERSHELL_RELATIVE = ('Windows', 'System32', 'WindowsPowerShell', 'v1.0', 'powershell.exe')


def _unescape_mount(field):
    """Undo the octal escapes /proc/mounts uses for space, tab, newline and backslash."""
    return re.sub(r'\\([0-7]{3})', lambda match: chr(int(match.group(1), 8)), field)


def find_powershell(mounts='/proc/mounts'):
    """Return the path of ``powershell.exe``: on PATH, else on a mounted Windows drive, else None."""
    found = shutil.which('powershell.exe')
    if found:
        return found
    try:
        with open(mounts, encoding='utf-8', errors='replace') as stream:
            lines = stream.read().splitlines()
    except OSError:
        return None
    for line in lines:
        fields = line.split()
        # WSL 2 mounts a Windows drive as 9p and WSL 1 as drvfs, from a source such as C:\.
        if len(fields) < 3 or fields[2] not in ('9p', 'drvfs'):
            continue
        if not re.match(r'[A-Za-z]:', _unescape_mount(fields[0])):
            continue
        candidate = os.path.join(_unescape_mount(fields[1]), *_POWERSHELL_RELATIVE)
        if os.access(candidate, os.X_OK):
            return candidate
    return None


def _detect():
    """Return the powershell.exe to run when ucs-detect runs under WSL, else None."""
    if not sys.platform.startswith('linux'):
        return None
    if os.environ.get('UCS_DETECT_CAPTURE', '').lower() == 'x11':
        return None
    try:
        with open('/proc/sys/kernel/osrelease', encoding='ascii') as stream:
            release = stream.read().lower()
    except OSError:
        return None
    return find_powershell() if 'microsoft' in release else None


#: The powershell.exe that runs the capture helper, or None.
POWERSHELL = _detect()

#: True when ucs-detect runs under WSL and captures through Windows.
IS_WSL = POWERSHELL is not None


class WindowsCaptureError(RuntimeError):
    """The capture helper failed or refused a request."""


_lock = threading.Lock()
_helper = None


def _windows_path(path):
    """Return the Windows form of a WSL *path*; the file itself need not exist yet."""
    directory, name = os.path.split(os.path.abspath(path))
    result = subprocess.run(['wslpath', '-w', directory],
                            capture_output=True, text=True, timeout=5, check=True)
    return result.stdout.strip().rstrip('\\') + '\\' + name


def _read_line(stream, timeout):
    ready, _, _ = select.select([stream], [], [], timeout)
    if not ready:
        raise WindowsCaptureError(f'no reply from the capture helper in {timeout} s')
    line = stream.readline()
    if not line:
        raise WindowsCaptureError('the capture helper exited')
    return line.strip()


def _stop():
    global _helper
    if _helper is not None:
        try:
            _helper.stdin.close()
            _helper.wait(timeout=5)
        except (OSError, subprocess.TimeoutExpired):
            _helper.kill()
        _helper = None


def _start():
    global _helper
    _helper = subprocess.Popen(
        [POWERSHELL, '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Bypass',
         '-File', _windows_path(_SCRIPT)],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        text=True, encoding='utf-8', errors='replace', bufsize=1)
    atexit.register(_stop)
    line = _read_line(_helper.stdout, STARTUP_TIMEOUT)
    if line != 'READY':
        _stop()
        raise WindowsCaptureError(f'capture helper did not start: {line}')


def _request(command, *arguments):
    """Send one request and return the helper's answer."""
    with _lock:
        if _helper is None or _helper.poll() is not None:
            _start()
        words = [command] + [str(argument).encode('utf-8').hex() for argument in arguments]
        try:
            _helper.stdin.write(' '.join(words) + '\n')
            _helper.stdin.flush()
            line = _read_line(_helper.stdout, REQUEST_TIMEOUT)
        except (OSError, WindowsCaptureError):
            _stop()
            raise
    if line.startswith('OK'):
        return line[3:]
    raise WindowsCaptureError(line[4:] if line.startswith('ERR ') else line)


def _pair(text):
    try:
        width, height = (int(part) for part in text.split())
    except ValueError:
        return None
    return (width, height) if width > 0 and height > 0 else None


def require_tools():
    """Return True when the capture helper starts."""
    try:
        _request('display')
    except (WindowsCaptureError, OSError, subprocess.SubprocessError) as error:
        print(f'Windows capture helper failed: {error}', file=sys.stderr)
        return False
    return True


def display_geometry():
    """Return the ``(width, height)`` of the whole Windows desktop in pixels, or None."""
    try:
        return _pair(_request('display'))
    except WindowsCaptureError:
        return None


def window_geometry(window_id):
    """Return the client area ``(width, height)`` of *window_id* in pixels, or None."""
    try:
        return _pair(_request('geometry', window_id))
    except WindowsCaptureError:
        return None


def find_own_window(title, timeout=5):
    """Return the window whose title contains *title*, or None."""
    deadline = time.monotonic() + timeout
    while True:
        try:
            found = _request('find', title)
        except WindowsCaptureError:
            found = ''
        if found:
            return found
        if time.monotonic() >= deadline:
            return None
        time.sleep(0.3)


def fit_window(window_id, max_size=None):
    """Leave the window at the size the user gave it; the capture takes it as it is."""
    return window_geometry(window_id) is not None


def focus(window_id):
    """Bring *window_id* to the front; Windows may refuse, and the capture does not need it."""
    try:
        _request('focus', window_id)
    except WindowsCaptureError:
        pass
    return True


def window_title(window_id):
    """Return the title of *window_id*, or an empty string."""
    try:
        return _request('title', window_id)
    except WindowsCaptureError:
        return ''


def window_class(window_id):
    """Return the window class name of *window_id*, or an empty string."""
    try:
        return _request('class', window_id)
    except WindowsCaptureError:
        return ''


def active_window():
    """Return the foreground window id, or an empty string."""
    try:
        return _request('active')
    except WindowsCaptureError:
        return ''


def capture_window_raw(window_id, output_path, park=True):
    """
    Capture the client area of *window_id* to the PNG *output_path*.

    The Windows pointer is never part of a capture, so *park* has nothing to do.
    """
    del park
    try:
        _request('capture', window_id, _windows_path(output_path))
    except WindowsCaptureError as error:
        raise RuntimeError(f'capture failed for window {window_id}: {error}') from error
