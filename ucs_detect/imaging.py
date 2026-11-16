"""X11 window capture and image analysis helpers shared by screenshot tools."""

# std imports
import os
import time
import shutil
import tempfile
import subprocess

try:
    # 3rd party
    import numpy
except ImportError:  # pragma: no cover
    numpy = None

# local
from ucs_detect import macos
from ucs_detect.accessories import display_lock, largest_window

#: Fraction of the display a window must cover to count as fullscreen.
FULLSCREEN_FRACTION = 0.9

#: Largest window used by the failure screenshot stage, whose output is marker-cropped.
SCREENSHOT_MAX_SIZE = (1280, 800)

#: Smallest horizontal run of marker pixels that counts as part of a capture marker.
MIN_MARKER_RUN = 6

#: Smallest vertical extent of a capture marker.
MIN_MARKER_HEIGHT = 12

#: Extra seconds a slow renderer is given before its window is captured.
_CAPTURE_DELAY = 0.0


def set_capture_delay(milliseconds):
    """Set the extra pause made before each capture, for a slow terminal renderer."""
    global _CAPTURE_DELAY
    _CAPTURE_DELAY = max(0.0, (milliseconds or 0) / 1000.0)


def capture_delay():
    """Return the extra seconds to pause before a capture."""
    return _CAPTURE_DELAY


def _require_numpy():
    if numpy is None:
        raise RuntimeError('numpy is required to measure captures')
    return numpy


def _run_quiet(argv, timeout=3):
    try:
        result = subprocess.run(
            argv, capture_output=True, text=True, timeout=timeout, check=False)
    except (subprocess.TimeoutExpired, OSError):
        return False
    return result.returncode == 0


def display_geometry():
    """Return the X11 display ``(width, height)`` in pixels, or None."""
    if macos.IS_MACOS:
        return macos.display_geometry()
    try:
        result = subprocess.run(
            ["xdotool", "getdisplaygeometry"],
            capture_output=True, text=True, timeout=3, check=False)
    except (subprocess.TimeoutExpired, OSError):
        return None
    parts = result.stdout.split()
    if result.returncode != 0 or len(parts) != 2:
        return None
    try:
        return int(parts[0]), int(parts[1])
    except ValueError:
        return None


def window_geometry(window_id):
    """Return the ``(width, height)`` of *window_id* in pixels, or None."""
    if macos.IS_MACOS:
        return macos.window_geometry(window_id)
    try:
        result = subprocess.run(
            ["xdotool", "getwindowgeometry", "--shell", str(window_id)],
            capture_output=True, text=True, timeout=3, check=False)
    except (subprocess.TimeoutExpired, OSError):
        return None
    width = height = 0
    for line in result.stdout.splitlines():
        if line.startswith("WIDTH="):
            width = int(line.split("=", 1)[1] or 0)
        elif line.startswith("HEIGHT="):
            height = int(line.split("=", 1)[1] or 0)
    if result.returncode != 0 or width <= 0 or height <= 0:
        return None
    return width, height


def _covers(window_id, width, height, fraction=FULLSCREEN_FRACTION):
    geometry = window_geometry(window_id)
    if geometry is None:
        return False
    return (geometry[0] >= width * fraction
            and geometry[1] >= height * fraction)


def _within(geometry, width, height):
    return geometry[0] <= width * 1.2 and geometry[1] <= height * 1.2


def _fills_screen(window_id, screen_width, screen_height,
                  fraction=FULLSCREEN_FRACTION):
    return _covers(window_id, screen_width, screen_height, fraction)


def _leave_fullscreen(window_id, screen_width, screen_height):
    if shutil.which("wmctrl") and _run_quiet(
            ["wmctrl", "-i", "-r", window_id, "-b",
             "remove,fullscreen,maximized_vert,maximized_horz"]):
        time.sleep(0.4)
        return
    if _fills_screen(window_id, screen_width, screen_height):
        with display_lock():
            if _run_quiet(["xdotool", "windowfocus", "--sync", window_id]):
                _run_quiet(["xdotool", "key", "--clearmodifiers", "F11"])
        time.sleep(0.4)


def try_fullscreen(window_id, screen_size=None, max_size=None):
    """Best-effort fill of *window_id* to the X11 display."""
    if macos.IS_MACOS:
        return macos.fit_window(window_id, max_size=max_size)
    window_id = str(window_id)
    screen_size = screen_size or display_geometry()
    if not screen_size:
        return False
    screen_width, screen_height = screen_size
    if max_size is not None:
        target_width = min(screen_width, max_size[0])
        target_height = min(screen_height, max_size[1])
        geometry = window_geometry(window_id)
        if geometry is not None and _within(
                geometry, target_width, target_height):
            return True
        for _attempt in range(2):
            if _covers(window_id, target_width, target_height):
                _leave_fullscreen(window_id, screen_width, screen_height)
            _run_quiet(["xdotool", "windowmove", "--sync", window_id, "0", "0"])
            _run_quiet(["xdotool", "windowsize", "--sync", window_id,
                        str(target_width), str(target_height)])
            time.sleep(0.2)
            previous, geometry = geometry, window_geometry(window_id)
            if geometry is None:
                return False
            if _within(geometry, target_width, target_height):
                return True
            if previous is not None and any(
                    geometry[axis] > target and geometry[axis] == previous[axis]
                    for axis, target in
                    enumerate((target_width, target_height))):
                break
        return False

    if _fills_screen(window_id, screen_width, screen_height):
        return True

    requested = False
    if shutil.which("wmctrl"):
        requested = _run_quiet(
            ["wmctrl", "-i", "-r", window_id, "-b", "add,fullscreen"])
    if requested:
        time.sleep(0.5)
        if _fills_screen(window_id, screen_width, screen_height):
            return True
    else:
        with display_lock():
            focused = _run_quiet(
                ["xdotool", "windowfocus", "--sync", window_id])
            if focused:
                _run_quiet(["xdotool", "key", "--clearmodifiers", "F11"])
        if focused:
            time.sleep(0.4)
            if _fills_screen(window_id, screen_width, screen_height):
                return True

    _run_quiet(["xdotool", "windowmove", "--sync", window_id, "0", "0"])
    _run_quiet(["xdotool", "windowsize", "--sync", window_id,
                str(screen_width), str(screen_height)])
    time.sleep(0.2)
    return _fills_screen(window_id, screen_width, screen_height)


def set_window_title(title):
    """Set the X11 window title via OSC escape sequence."""
    # std imports
    import sys
    sys.stdout.write(f"\x1b]0;{title}\x07")
    sys.stdout.flush()


def find_own_window(title, timeout=5):
    """Find the terminal window that contains this process."""
    if macos.IS_MACOS:
        return macos.find_own_window(title, timeout=timeout)
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            result = subprocess.run(
                ["xdotool", "search", "--name", title],
                capture_output=True, text=True, timeout=3, check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                return largest_window(result.stdout.strip().split("\n"))
        except (subprocess.TimeoutExpired, OSError):
            pass
        time.sleep(0.3)

    ppid = os.getppid()
    parent_names = []
    for _ in range(4):
        try:
            with open(f"/proc/{ppid}/stat") as f:
                stat = f.read().split()
            parent_names.append(stat[1].strip("()"))
            result = subprocess.run(
                ["xdotool", "search", "--onlyvisible", "--pid", str(ppid)],
                capture_output=True, text=True, timeout=3, check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                return largest_window(result.stdout.strip().split("\n"))
            ppid = int(stat[3])
        except (OSError, ValueError, IndexError, subprocess.TimeoutExpired):
            break

    for name in parent_names:
        for flag in ("--class", "--classname"):
            try:
                result = subprocess.run(
                    ["xdotool", "search", "--onlyvisible", flag, name],
                    capture_output=True, text=True, timeout=3, check=False,
                )
                if result.returncode == 0 and result.stdout.strip():
                    return largest_window(result.stdout.strip().split("\n"))
            except (subprocess.TimeoutExpired, OSError):
                pass

    if os.path.exists("/.dockerenv"):
        try:
            result = subprocess.run(
                ["xdotool", "getactivewindow"],
                capture_output=True, text=True, timeout=3, check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except (subprocess.TimeoutExpired, OSError):
            pass

    return None


def park_pointer(window_id):
    """
    Move the X pointer to the top right corner of *window_id*.

    Xvfb paints the pointer into the framebuffer, so a pointer resting over the terminal shows up in
    the capture.
    """
    if macos.IS_MACOS:
        return True
    geometry = window_geometry(window_id)
    if geometry is not None:
        return _run_quiet(
            ["xdotool", "mousemove", "--window", str(window_id),
             str(geometry[0] - 2), "2"])
    screen = display_geometry()
    if screen is None:
        return False
    return _run_quiet(
        ["xdotool", "mousemove", str(screen[0] - 2), "2"])


def capture_window_raw(window_id, output_path, park=True):
    """Capture *window_id* to *output_path* without cropping."""
    if macos.IS_MACOS:
        return macos.capture_window_raw(window_id, output_path, park=park)
    with display_lock():
        if park:
            park_pointer(window_id)
        _capture_window_xwd(window_id, output_path)


def _capture_window_xwd(window_id, output_path):
    tmp_xwd = tempfile.mktemp(suffix=".xwd")
    try:
        last_error = None
        for attempt in range(4):
            if os.path.exists(tmp_xwd):
                os.unlink(tmp_xwd)
            try:
                subprocess.run(
                    ["xwd", "-id", str(window_id), "-silent", "-out", tmp_xwd],
                    capture_output=True, check=True, timeout=10,
                )
                last_error = None
                break
            except subprocess.CalledProcessError as error:
                last_error = error
                if attempt < 3:
                    time.sleep(0.4 * (attempt + 1))
        if last_error is not None:
            message = last_error.stderr or last_error.output or ""
            if isinstance(message, bytes):
                message = message.decode("utf-8", "replace")
            raise RuntimeError(
                f"xwd failed for window {window_id}: {message.strip()}")
        subprocess.run(
            ["convert", tmp_xwd, "-strip", output_path],
            capture_output=True, check=True, timeout=10,
        )
    finally:
        if os.path.exists(tmp_xwd):
            os.unlink(tmp_xwd)


def capture_window(window_id, output_path):
    """Capture *window_id* to *output_path* as a marker-cropped PNG."""
    tmp_png = tempfile.mktemp(suffix=".png")
    try:
        capture_window_raw(window_id, tmp_png)
        crop_to_markers(tmp_png, output_path)
    finally:
        if os.path.exists(tmp_png):
            os.unlink(tmp_png)


def is_blank(path):
    """Return True if *path* is mostly blank."""
    # 3rd party
    from PIL import Image
    with Image.open(path) as opened:
        img = opened.convert("RGB") if opened.mode != "RGB" else opened
        flattened = getattr(img, "get_flattened_data", None)
        pixels = list(flattened() if flattened else img.getdata())
    white = sum(1 for p in pixels if p[0] > 240 and p[1] > 240 and p[2] > 240)
    if white / len(pixels) > 0.95:
        return True
    if os.path.exists("/.dockerenv"):
        black = sum(1 for p in pixels if p[0] < 15 and p[1] < 15 and p[2] < 15)
        if black / len(pixels) > 0.95:
            return True
    return False


def imagemagick_trim(src_path, dst_path):
    """Crop *src_path* using ImageMagick trim as a fallback."""
    if shutil.which("convert"):
        subprocess.run(
            ["convert", src_path, "-trim", "+repage", "-strip", dst_path],
            capture_output=True, check=True, timeout=10,
        )
        return
    # 3rd party
    from PIL import Image, ImageChops
    with Image.open(src_path) as opened:
        image = opened.convert("RGB")
        background = Image.new("RGB", image.size, image.getpixel((0, 0)))
        box = ImageChops.difference(image, background).getbbox()
        image.crop(box).save(dst_path)


def _load_rgb(path):
    # 3rd party
    from PIL import Image
    with Image.open(path) as image:
        return image.convert("RGB")


def marker_mask(array):
    """Return a boolean mask of marker pixels in an ``(h, w, 3)`` RGB array."""
    np = _require_numpy()
    r = array[:, :, 0].astype("int16")
    g = array[:, :, 1].astype("int16")
    b = array[:, :, 2].astype("int16")
    magenta = (r > 150) & (b > 150) & (g < 100) & (np.abs(r - b) < 80)
    yellow = (r > 150) & (g > 140) & (b < 100) & (np.abs(r - g) < 110)
    warm = (r > 110) & ((r - g) > 70) & ((r - b) > 70) & (b < 80)
    return magenta | yellow | warm


def marker_edge_mask(array):
    """Return a boolean mask of pixels blended between a marker color and background."""
    r = array[:, :, 0].astype("int16")
    g = array[:, :, 1].astype("int16")
    b = array[:, :, 2].astype("int16")
    return (((r - g) > 80) & ((b - g) > 80)) | (((r - b) > 80) & ((g - b) > 80))


def marker_runs(row_mask):
    """Return the inclusive ``(start, end)`` runs of marker pixels in one row mask."""
    np = _require_numpy()
    indexes = np.flatnonzero(row_mask)
    if not indexes.size:
        return []
    breaks = np.flatnonzero(np.diff(indexes) != 1)
    starts = np.concatenate(([indexes[0]], indexes[breaks + 1]))
    ends = np.concatenate((indexes[breaks], [indexes[-1]]))
    return [(int(start), int(end)) for start, end in zip(starts, ends)
            if end - start + 1 >= MIN_MARKER_RUN]


def marker_blocks(mask):
    """Return ``[x1, y1, x2, y2]`` for each vertical block of marker runs."""
    np = _require_numpy()
    blocks = []
    current = []
    previous = None
    for row in np.flatnonzero(mask.any(axis=1)):
        runs = marker_runs(mask[row])
        if not runs:
            continue
        y = int(row)
        run_x1 = min(run[0] for run in runs)
        run_x2 = max(run[1] for run in runs)
        if not current or (previous is not None and y - previous - 1 >= 2):
            if current:
                blocks.append(current)
            current = [run_x1, y, run_x2, y]
        else:
            current[0] = min(current[0], run_x1)
            current[2] = max(current[2], run_x2)
            current[3] = y
        previous = y
    if current:
        blocks.append(current)
    return blocks


def marker_block_has_checkerboard(mask, array, block):
    """Return True when *block* contains both cells of the checkerboard."""
    x1, y1, x2, y2 = block
    window = mask[y1:y2 + 1, x1:x2 + 1]
    green = array[y1:y2 + 1, x1:x2 + 1, 1]
    return bool((window & (green < 100)).any()
                and (window & (green >= 100)).any())


def _marker_scan(image):
    np = _require_numpy()
    array = np.asarray(image, dtype="uint8")
    if array.ndim != 3 or array.shape[2] < 3:
        return None, None, []
    mask = marker_mask(array)
    blocks = [block for block in marker_blocks(mask)
              if block[3] - block[1] + 1 >= MIN_MARKER_HEIGHT
              and marker_block_has_checkerboard(mask, array, block)]
    if not blocks:
        return array, mask, []
    tallest = max(block[3] - block[1] + 1 for block in blocks)
    return array, mask, [block for block in blocks
                         if block[3] - block[1] + 1 >= tallest / 2]


def capture_marker_blocks(image):
    """Return the ``[x1, y1, x2, y2]`` capture marker blocks found in *image*."""
    return _marker_scan(image)[2]


def _marker_frame(image):
    array, mask, blocks = _marker_scan(image)
    if not blocks:
        return None
    top = min(blocks, key=lambda block: block[1])
    bottom = max(blocks, key=lambda block: block[3])
    if top[1] >= bottom[1]:
        return None
    return mask, array, top, bottom


def has_capture_markers(path):
    """Return True when the capture at *path* shows both checkerboard markers."""
    return _marker_frame(_load_rgb(path)) is not None


def crop_to_markers(src_path, dst_path):
    """Crop *src_path* to the rectangle bounded by two checkerboards."""
    image = _load_rgb(src_path)
    frame = _marker_frame(image)
    if frame is None:
        imagemagick_trim(src_path, dst_path)
        return False
    _mask, array, top, bottom = frame
    height, width = array.shape[:2]
    edges = marker_edge_mask(array)

    x1, y1, top_x2, top_y2 = top
    bottom_x1, bottom_y1, x2, y2 = bottom
    if x1 > 0 and edges[y1:top_y2 + 1, x1 - 1].any():
        x1 -= 1
    if x2 + 1 < width and edges[bottom_y1:y2 + 1, x2 + 1].any():
        x2 += 1
    if y1 > 0 and edges[y1 - 1, x1:top_x2 + 1].any():
        y1 -= 1
    if y2 + 1 < height and edges[y2 + 1, bottom_x1:x2 + 1].any():
        y2 += 1

    if x2 < x1 or y2 < y1:
        imagemagick_trim(src_path, dst_path)
        return False
    image.crop((x1, y1, x2 + 1, y2 + 1)).save(dst_path)
    _strip_png(dst_path)
    return True


def _strip_png(path):
    if shutil.which("convert"):
        subprocess.run(
            ["convert", path, "-strip", path],
            capture_output=True, check=True, timeout=10,
        )
        return
    # 3rd party
    from PIL import Image
    with Image.open(path) as opened:
        image = opened.copy()
    image.save(path)


def finish_capture(raw_path, output_path):
    """Crop the raw capture *raw_path* into *output_path* and remove the raw file."""
    try:
        return crop_to_markers(raw_path, output_path)
    finally:
        if os.path.exists(raw_path):
            os.unlink(raw_path)


def require_capture_tools():
    """Return True when the platform capture tools are available."""
    if macos.IS_MACOS:
        return macos.require_tools()
    return bool(shutil.which("xdotool") and shutil.which("xwd"))


def focus_window(window_id):
    """Raise and focus *window_id*, returning True on success."""
    if macos.IS_MACOS:
        return macos.focus(window_id)
    with display_lock():
        for argv in (
                ["xdotool", "windowraise", str(window_id)],
                ["xdotool", "windowactivate", "--sync", str(window_id)],
                ["xdotool", "windowfocus", "--sync", str(window_id)]):
            _run_quiet(argv)
    return True


def window_title(window_id):
    """Return the title of *window_id*, or an empty string."""
    if macos.IS_MACOS:
        return macos.window_title(window_id)
    try:
        result = subprocess.run(
            ["xdotool", "getwindowname", str(window_id)],
            capture_output=True, text=True, timeout=2, check=False)
    except (subprocess.TimeoutExpired, OSError):
        return ''
    return result.stdout.strip() if result.returncode == 0 else ''


def window_class(window_id):
    """Return the X11 class name of *window_id*, or an empty string."""
    if macos.IS_MACOS:
        return macos.window_owner(window_id)
    try:
        result = subprocess.run(
            ["xdotool", "getwindowclassname", str(window_id)],
            capture_output=True, text=True, timeout=2, check=False)
    except (subprocess.TimeoutExpired, OSError):
        return ''
    return result.stdout.strip() if result.returncode == 0 else ''


def active_window():
    """Return the frontmost window id, or an empty string."""
    if macos.IS_MACOS:
        return macos.active_window()
    try:
        result = subprocess.run(
            ["xdotool", "getactivewindow"],
            capture_output=True, text=True, timeout=2, check=False)
    except (subprocess.TimeoutExpired, OSError):
        return ''
    return result.stdout.strip() if result.returncode == 0 else ''
