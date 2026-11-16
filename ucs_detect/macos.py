"""macOS window, capture, and keystroke primitives for the system stages.

Linux stages drive X11 through xdotool and xwd.  macOS has no X server, so the same operations run
through CoreGraphics window listings, ``screencapture -l`` and System Events keystrokes.  Every
function returns what its X11 counterpart returns, so the stages never branch on the platform.
"""

# std imports
import os
import re
import sys
import json
import time
import shlex
import plistlib
import subprocess
from pathlib import Path

IS_MACOS = sys.platform == 'darwin'

#: Command line tools every macOS stage requires.
OSASCRIPT = '/usr/bin/osascript'
SCREENCAPTURE = '/usr/sbin/screencapture'

#: Space the menu bar reserves, so a fitted window keeps its title bar reachable.
MENU_BAR_HEIGHT = 25

#: Second between two window list queries while looking for a window.
WINDOW_POLL_INTERVAL = 0.4

#: Seconds between window liveness checks made by :meth:`MacLaunch.poll`.
LIVENESS_INTERVAL = 5.0

#: CoreGraphics window listing, as JSON: every window with its frame and owning process.
WINDOW_LIST = """
ObjC.import("CoreGraphics");
var list = ObjC.castRefToObject($.CGWindowListCopyWindowInfo(0, 0));
var found = [];
for (var index = 0; index < list.count; index++) {
    var item = list.objectAtIndex(index);
    var box = item.objectForKey("kCGWindowBounds");
    found.push({
        id: ObjC.unwrap(item.objectForKey("kCGWindowNumber")),
        owner: ObjC.unwrap(item.objectForKey("kCGWindowOwnerName")),
        pid: ObjC.unwrap(item.objectForKey("kCGWindowOwnerPID")),
        name: ObjC.unwrap(item.objectForKey("kCGWindowName")) || "",
        layer: ObjC.unwrap(item.objectForKey("kCGWindowLayer")),
        x: box ? ObjC.unwrap(box.objectForKey("X")) : 0,
        y: box ? ObjC.unwrap(box.objectForKey("Y")) : 0,
        width: box ? ObjC.unwrap(box.objectForKey("Width")) : 0,
        height: box ? ObjC.unwrap(box.objectForKey("Height")) : 0
    });
}
JSON.stringify(found);
"""

#: Main display size in points, as JSON.
DISPLAY_SIZE = """
ObjC.import("CoreGraphics");
var main = $.CGMainDisplayID();
JSON.stringify([Number($.CGDisplayPixelsWide(main)), Number($.CGDisplayPixelsHigh(main))]);
"""

#: Virtual key codes for the keys post_launch_keys names other than plain text.
KEY_CODES = {
    'return': 36,
    'enter': 36,
    'tab': 48,
    'space': 49,
    'escape': 53,
    'esc': 53,
    'backspace': 51,
    'delete': 51,
    'left': 123,
    'right': 124,
    'down': 125,
    'up': 126,
    'home': 115,
    'end': 119,
    'pageup': 116,
    'pagedown': 121,
    'f11': 103,
    'f12': 111,
}

#: Modifier names accepted in a ``\\kctrl+shift+t`` key combination.
MODIFIERS = {
    'ctrl': 'control down',
    'control': 'control down',
    'shift': 'shift down',
    'alt': 'option down',
    'option': 'option down',
    'opt': 'option down',
    'cmd': 'command down',
    'command': 'command down',
    'meta': 'command down',
}


class MacOSError(RuntimeError):
    """Raised when a macOS tool is missing, refuses, or fails."""


class MacLaunch:
    """Stand-in for ``subprocess.Popen`` when the application runs the script itself."""

    def __init__(self, owner, window_id, timeout=8.0):
        self.owner = owner
        self.window_id = window_id
        self.timeout = timeout
        self.pid = 0
        self._dead = window_id is None
        self._next_check = None

    def poll(self):
        """Return None while the terminal window lives, else a non-zero exit code."""
        now = time.monotonic()
        if self._next_check is None or now >= self._next_check:
            self._dead = window_geometry(self.window_id) is None
            self._next_check = now + LIVENESS_INTERVAL
        return 1 if self._dead else None

    def kill(self):
        """Close the terminal window."""
        close_window(self.window_id)

    def close(self):
        """Close the terminal window."""
        close_window(self.window_id)


def require_tools(timeout=None):  # pylint: disable=unused-argument
    """Return True when osascript and screencapture are installed."""
    return (os.access(OSASCRIPT, os.X_OK)
            and os.access(SCREENCAPTURE, os.X_OK))


def run_tool(argv, timeout=30):
    """Run *argv* and return its stripped standard output, raising :class:`MacOSError`."""
    try:
        result = subprocess.run(
            argv, capture_output=True, text=True, timeout=timeout, check=False)
    except (subprocess.TimeoutExpired, OSError) as error:
        raise MacOSError(f'{argv[0]} failed: {error}') from error
    if result.returncode != 0:
        message = (result.stderr or result.stdout).strip()
        raise MacOSError(f'{argv[0]} exited {result.returncode}: {message}')
    return result.stdout.strip()


def osascript(lines, timeout=30):
    """Run the AppleScript *lines* and return the result as text."""
    argv = [OSASCRIPT]
    for line in lines:
        argv.extend(['-e', line])
    return run_tool(argv, timeout=timeout)


def jxa(script, timeout=30):
    """Run the JavaScript for Automation *script* and return the result as text."""
    return run_tool([OSASCRIPT, '-l', 'JavaScript', '-e', script],
                    timeout=timeout)


def applescript_string(value):
    """Return *value* quoted as an AppleScript string literal."""
    escaped = str(value).replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'


def _number(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def windows():
    """Return the on-screen windows, each a dict of id, owner, pid, name, layer and frame."""
    try:
        items = json.loads(jxa(WINDOW_LIST, timeout=20))
    except (MacOSError, ValueError):
        return []
    found = []
    for item in items:
        if not item.get('id'):
            continue
        found.append({
            'id': str(_number(item.get('id'))),
            'owner': item.get('owner') or '',
            'pid': _number(item.get('pid')),
            'name': item.get('name') or '',
            'layer': _number(item.get('layer'), -1),
            'x': _number(item.get('x')),
            'y': _number(item.get('y')),
            'width': _number(item.get('width')),
            'height': _number(item.get('height')),
        })
    return found


def window(window_id):
    """Return the window dict for *window_id*, or None."""
    wanted = str(window_id)
    for item in windows():
        if item['id'] == wanted:
            return item
    return None


def window_owner(window_id):
    """Return the owning application name of *window_id*, or an empty string."""
    item = window(window_id)
    return item['owner'] if item else ''


def window_title(window_id):
    """Return the title of *window_id*, or an empty string."""
    item = window(window_id)
    return item['name'] if item else ''


def window_geometry(window_id):
    """Return the ``(width, height)`` of *window_id* in points, or None."""
    item = window(window_id)
    if item is None or item['width'] <= 0 or item['height'] <= 0:
        return None
    return item['width'], item['height']


def active_window():
    """Return the frontmost application window id, or an empty string."""
    for item in windows():
        if item['layer'] == 0 and item['name']:
            return item['id']
    return ''


def display_geometry():
    """Return the main display ``(width, height)`` in points, or None."""
    try:
        width, height = json.loads(jxa(DISPLAY_SIZE, timeout=20))
    except (MacOSError, ValueError, TypeError):
        return None
    width, height = _number(width), _number(height)
    if width <= 0 or height <= 0:
        return None
    return width, height


def find_window(owner, exclude=(), title_pattern=None, timeout=8.0,
                stale_grace=0.0):
    """Return the id of a new window owned by *owner*, or None."""
    deadline = time.monotonic() + timeout
    started = time.monotonic()
    while True:
        candidates = [item for item in windows()
                      if item['owner'] == owner and item['layer'] == 0]
        if title_pattern:
            matches = [item for item in candidates
                       if re.search(title_pattern, item['name'])]
            if matches:
                return largest_window_id(matches)
        if time.monotonic() - started >= stale_grace:
            fresh = [item for item in candidates
                     if item['id'] not in set(exclude)]
            if fresh:
                titled = [item for item in fresh if item['name']]
                return frontmost_window_id(titled or fresh)
        if time.monotonic() >= deadline:
            return None
        time.sleep(WINDOW_POLL_INTERVAL)


def largest_window_id(items):
    """Return the id of the largest window in *items*."""
    ordered = sorted(
        items, key=lambda item: item['width'] * item['height'])
    return ordered[-1]['id'] if ordered else None


def frontmost_window_id(items):
    """Return the id of the frontmost window in *items*, which CoreGraphics lists in order."""
    for item in items:
        if item['name']:
            return item['id']
    return items[0]['id'] if items else None


def find_own_window(title, timeout=5):
    """Return a window whose title contains *title*, or None."""
    deadline = time.monotonic() + timeout
    while True:
        matches = [item for item in windows()
                   if item['layer'] == 0 and title in item['name']]
        if matches:
            return largest_window_id(matches)
        if time.monotonic() >= deadline:
            return None
        time.sleep(WINDOW_POLL_INTERVAL)


def wait_for_owner(owner, timeout=20):
    """Return True when a process named *owner* owns at least one window."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if any(item['owner'] == owner for item in windows()):
            return True
        time.sleep(WINDOW_POLL_INTERVAL)
    return False


def ax_windows(owner):
    """Return the Accessibility ``(x, y, width, height)`` frames of *owner*'s windows."""
    script = [
        'set found to ""',
        f'tell application "System Events" to tell process '
        f'{applescript_string(owner)}',
        'repeat with index from 1 to count of windows',
        'set spot to position of window index',
        'set area to size of window index',
        'set found to found & (item 1 of spot) & "," & (item 2 of spot) '
        '& "," & (item 1 of area) & "," & (item 2 of area) & ";"',
        'end repeat',
        'end tell',
        'return found',
    ]
    try:
        text = osascript(script, timeout=15)
    except MacOSError:
        return []
    frames = []
    for chunk in text.split(';'):
        values = [part.strip() for part in chunk.split(',')]
        if len(values) != 4:
            continue
        try:
            frames.append(tuple(int(value) for value in values))
        except ValueError:
            continue
    return frames


def ax_window_index(window_id):
    """Return the 1-based Accessibility window index of *window_id*, or None."""
    item = window(window_id)
    if item is None:
        return None
    sought = (item['x'], item['y'], item['width'], item['height'])
    frames = ax_windows(item['owner'])
    for index, frame in enumerate(frames, start=1):
        if all(abs(frame[axis] - sought[axis]) <= 4 for axis in range(4)):
            return index
    for index, frame in enumerate(frames, start=1):
        if abs(frame[2] - sought[2]) <= 4 and abs(frame[3] - sought[3]) <= 4:
            return index
    return None


def focus(window_id):
    """Raise and focus *window_id*, returning True on success."""
    item = window(window_id)
    if item is None:
        return False
    owner = applescript_string(item['owner'])
    try:
        osascript([
            f'tell application "System Events" to set frontmost of process '
            f'{owner} to true',
        ], timeout=15)
    except MacOSError:
        return False
    index = ax_window_index(window_id)
    if index is not None:
        try:
            osascript([
                f'tell application "System Events" to tell process {owner}',
                f'perform action "AXRaise" of window {index}',
                'end tell',
            ], timeout=15)
        except MacOSError:
            pass
    time.sleep(0.15)
    return True


def _app_set_bounds(program, current, target):
    """Resize a window through the application's own ``bounds`` property."""
    left, top = 0, MENU_BAR_HEIGHT
    right, bottom = target[0], MENU_BAR_HEIGHT + target[1]
    script = [
        f'tell application {applescript_string(program)}',
        'set found to 0',
        'repeat with index from 1 to count of windows',
        'set box to bounds of window index',
        f'if ((item 3 of box) - (item 1 of box) is {current[0]}) then '
        'set found to index',
        'end repeat',
        f'if found is not 0 then set bounds of window found to '
        f'{{{left}, {top}, {right}, {bottom}}}',
        'return found',
        'end tell',
    ]
    try:
        return osascript(script, timeout=20).strip() not in ('', '0')
    except MacOSError:
        return False


def _ax_set_size(window_id, target):
    """Resize a window through the Accessibility API."""
    item = window(window_id)
    index = ax_window_index(window_id)
    if item is None or index is None:
        return False
    try:
        osascript([
            f'tell application "System Events" to tell process '
            f'{applescript_string(item["owner"])}',
            f'set position of window {index} to {{0, {MENU_BAR_HEIGHT}}}',
            f'set size of window {index} to {{{target[0]}, {target[1]}}}',
            'end tell',
        ], timeout=20)
    except MacOSError:
        return False
    return True


def fit_window(window_id, max_size=None):
    """Resize *window_id* to the smaller of the display and *max_size*."""
    screen = display_geometry()
    geometry = window_geometry(window_id)
    item = window(window_id)
    if screen is None or geometry is None or item is None:
        return False
    target = (min(screen[0], max_size[0]) if max_size else screen[0],
              min(screen[1], max_size[1]) if max_size else
              screen[1] - MENU_BAR_HEIGHT)
    if max_size:
        if geometry[0] <= target[0] * 1.2 and geometry[1] <= target[1] * 1.2:
            return True
    elif (geometry[0] >= target[0] * 0.9
          and geometry[1] >= target[1] * 0.9):
        return True

    program = (_LAUNCHED_APPS.get(str(window_id))
               or app_paths().get(item['owner'], ''))
    if program and not _app_set_bounds(program, geometry, target):
        _ax_set_size(window_id, target)
    elif not program:
        _ax_set_size(window_id, target)
    time.sleep(0.5)
    geometry = window_geometry(window_id)
    if geometry is None:
        return False
    return (geometry[0] >= target[0] * 0.9
            and geometry[1] >= target[1] * 0.9)


def capture_window_raw(window_id, output_path, park=True):
    """Capture *window_id* to *output_path* without cropping."""
    del park  # the pointer is never painted into a window capture
    try:
        run_tool([SCREENCAPTURE, '-x', '-o', f'-l{window_id}',
                  str(output_path)], timeout=30)
    except MacOSError as error:
        raise RuntimeError(
            f'screencapture failed for window {window_id}: {error}') from error
    if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
        raise RuntimeError(
            f'screencapture produced no image for window {window_id}')


def _key_statement(combination):
    """Return the AppleScript statement for one ``+`` separated key combination."""
    parts = [part.strip().lower() for part in combination.split('+') if part.strip()]
    if not parts:
        return ''
    modifiers = [MODIFIERS[name] for name in parts[:-1] if name in MODIFIERS]
    key = parts[-1]
    using = f' using {{{", ".join(modifiers)}}}' if modifiers else ''
    if key in KEY_CODES:
        return f'key code {KEY_CODES[key]}{using}'
    return f'keystroke {applescript_string(key)}{using}'


def keystroke_lines(keys, key_delay_ms=30):
    """Return AppleScript statements that type *keys* into the frontmost window."""
    del key_delay_ms  # System Events types a whole string at once
    lines = []
    pending = []
    for key in keys:
        if key in ('\n', '\\n'):
            if pending:
                lines.append(f'keystroke {applescript_string("".join(pending))}')
                pending = []
            lines.append('key code 36')
        elif key.startswith('\\p') and key[2:].isdigit():
            if pending:
                lines.append(f'keystroke {applescript_string("".join(pending))}')
                pending = []
            lines.append(f'delay {int(key[2:]) / 1000.0}')
        elif key.startswith('\\k'):
            if pending:
                lines.append(f'keystroke {applescript_string("".join(pending))}')
                pending = []
            statement = _key_statement(key[2:])
            if statement:
                lines.append(statement)
        else:
            pending.append(key)
    if pending:
        lines.append(f'keystroke {applescript_string("".join(pending))}')
    return lines


def inject_keys(window_id, keys, key_delay_ms=30, click_before_keys=False):
    """Type *keys* into *window_id* through System Events."""
    del click_before_keys  # raising the window is the equivalent of the X11 click
    if not focus(window_id):
        return False
    lines = keystroke_lines(keys, key_delay_ms=key_delay_ms)
    if not lines:
        return True
    script = (['tell application "System Events"'] + lines + ['end tell'])
    try:
        osascript(script, timeout=60)
    except MacOSError:
        return False
    return True


def close_window(window_id):
    """Close *window_id* with its own close command, returning True on success."""
    if window_id is None or window(window_id) is None:
        return False
    if not focus(window_id):
        return False
    try:
        osascript(['tell application "System Events" to key code 13 '
                   'using command down'], timeout=15)
    except MacOSError:
        return False
    time.sleep(0.5)
    return window(window_id) is None


#: Application bundles searched for the owner name of a window.
APP_DIRECTORIES = ('/Applications',
                   '/Applications/Utilities',
                   '/System/Applications',
                   '/System/Applications/Utilities')

#: Owner name to bundle path, and window id to bundle path of the terminal that was launched.
_APP_PATH_CACHE = {}
_LAUNCHED_APPS = {}


def app_paths():
    """Return a mapping of application name to bundle path."""
    if _APP_PATH_CACHE:
        return _APP_PATH_CACHE
    for directory in APP_DIRECTORIES:
        for bundle in sorted(Path(directory).glob('*.app')):
            info = bundle / 'Contents' / 'Info.plist'
            try:
                with open(info, 'rb') as stream:
                    name = plistlib.load(stream).get('CFBundleName')
            except (OSError, ValueError):
                continue
            if name:
                _APP_PATH_CACHE.setdefault(name, str(bundle))
    return _APP_PATH_CACHE


def register_window(window_id, program):
    """Remember which application bundle owns *window_id*."""
    if window_id:
        _LAUNCHED_APPS[str(window_id)] = program


def app_path(config):
    """Return the application bundle path named by a macOS launch config."""
    return config.get('app') or config.get('program') or ''


def app_owner(config):
    """Return the window owner name of the application in *config*."""
    if config.get('owner'):
        return config['owner']
    bundle = Path(app_path(config))
    for candidate in (bundle, Path('/Applications') / bundle.name):
        info = candidate / 'Contents' / 'Info.plist'
        try:
            with open(info, 'rb') as stream:
                name = plistlib.load(stream).get('CFBundleName')
        except (OSError, ValueError):
            name = None
        if name:
            return name
    return bundle.stem


def launch(config, script_path, window_search_timeout_ms=None):
    """Start the terminal in *config* running *script_path*, returning a :class:`MacLaunch`."""
    owner = app_owner(config)
    adapter = (config.get('adapter') or 'terminal').lower()
    program = app_path(config)
    before = {item['id'] for item in windows()}
    timeout = (window_search_timeout_ms
               or config.get('window_search_timeout_ms')
               or 8000) / 1000.0
    title_pattern = None
    if adapter == 'iterm2':
        command = f'sh {shlex.quote(str(script_path))}'
        osascript([
            f'tell application {applescript_string(program)}',
            'activate',
            f'create window with default profile command '
            f'{applescript_string(command)}',
            'end tell',
        ], timeout=60)
    elif adapter == 'tecolot':
        # Tecolot takes no command line argument, and it restores the windows of its last
        # session, so the window is opened in the stage's own directory and found by that name.
        workdir = os.path.dirname(str(script_path)) or '/tmp'
        osascript([
            f'tell application {applescript_string(program)}',
            f'open terminal {applescript_string(workdir)}',
            'end tell',
        ], timeout=60)
        title_pattern = re.escape(os.path.basename(workdir))
    else:
        run_tool(['open', '-a', program, str(script_path)], timeout=60)
    window_id = find_window(owner, exclude=before, title_pattern=title_pattern,
                            timeout=timeout)
    register_window(window_id, program)
    return MacLaunch(owner, window_id, timeout=timeout)
