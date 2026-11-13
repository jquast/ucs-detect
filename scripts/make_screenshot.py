#!/usr/bin/env python3
"""Display unicode characters with width measurements and capture screenshots.

Runs inside a terminal emulator.  Reads a JSON batch file of failure records.
For each record, displays a simplified ``--stop-at-error``-style box with
``measured by terminal`` / ``measured by wcwidth``, captures its own X11 window,
and saves a trimmed PNG.
"""
import argparse
import functools
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

# Ensure the project root is on sys.path for ucs_detect imports
_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_DIR not in sys.path:
    sys.path.insert(0, _PROJECT_DIR)

import wcwidth

from ucs_detect.accessories import decode_wchars


def _marker_cells(term):
    """Return (row1_str, row2_str), a 2x2 checkerboard of magenta and yellow.

    The sequences are layered so the most precise color a terminal supports
    wins: ANSI bright background first, then the exact xterm 256-color cube
    entry (201 is magenta, 226 is yellow), then truecolor.  Writing the
    truecolor SGR directly avoids blessed's downconversion.  The 256-color
    layer keeps the markers exact through multiplexers such as GNU Screen,
    which drops ``48;2`` unless its own truecolor setting is on.
    """
    mc = "\x1b[45m\x1b[105m\x1b[48;5;201m\x1b[48;2;255;0;255m"
    yc = "\x1b[43m\x1b[103m\x1b[48;5;226m\x1b[48;2;255;255;0m"
    row1 = mc + " " + yc + " " + term.normal
    row2 = yc + " " + mc + " " + term.normal
    return row1, row2


def set_window_title(title):
    """Set the X11 window title via OSC escape sequence."""
    sys.stdout.write(f"\x1b]0;{title}\x07")
    sys.stdout.flush()


def find_own_window(title, timeout=5):
    """Find our containing terminal window."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            result = subprocess.run(
                ["xdotool", "search", "--name", title],
                capture_output=True, text=True, timeout=3,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().split("\n")[-1]
        except (subprocess.TimeoutExpired, OSError):
            pass
        time.sleep(0.3)

    # Fallback: walk parent PIDs, collecting process names for class search
    ppid = os.getppid()
    parent_names = []
    for _ in range(4):
        try:
            with open(f"/proc/{ppid}/stat") as f:
                stat = f.read().split()
                parent_names.append(stat[1].strip("()"))
            result = subprocess.run(
                ["xdotool", "search", "--onlyvisible", "--pid", str(ppid)],
                capture_output=True, text=True, timeout=3,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().split("\n")[-1]
            ppid = int(stat[3])
        except (OSError, ValueError, IndexError, subprocess.TimeoutExpired):
            break

    # Fallback: search by class name derived from parent process names
    for name in parent_names:
        for flag in ("--class", "--classname"):
            try:
                result = subprocess.run(
                    ["xdotool", "search", "--onlyvisible", flag, name],
                    capture_output=True, text=True, timeout=3,
                )
                if result.returncode == 0 and result.stdout.strip():
                    return result.stdout.strip().split("\n")[-1]
            except (subprocess.TimeoutExpired, OSError):
                pass

    # Docker-only fallback: with a single X11 window, getactivewindow is safe
    if os.path.exists("/.dockerenv"):
        try:
            result = subprocess.run(
                ["xdotool", "getactivewindow"],
                capture_output=True, text=True, timeout=3,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except (subprocess.TimeoutExpired, OSError):
            pass

    return None


def capture_window(window_id, output_path):
    """Capture *window_id* to *output_path* as a marker-cropped PNG."""
    tmp_xwd = None
    tmp_png = None
    try:
        tmp_xwd = tempfile.mktemp(suffix=".xwd")
        for attempt in range(2):
            try:
                subprocess.run(
                    ["xwd", "-id", str(window_id), "-silent", "-out", tmp_xwd],
                    capture_output=True, check=True, timeout=10,
                )
                break
            except subprocess.CalledProcessError:
                if attempt == 0:
                    time.sleep(0.5)
                    continue
                raise
        # Convert to PNG first (no -trim), then crop via marker detection
        tmp_png = tempfile.mktemp(suffix=".png")
        subprocess.run(
            ["convert", tmp_xwd, "-strip", tmp_png],
            capture_output=True, check=True, timeout=10,
        )
        _crop_to_markers(tmp_png, output_path)
    finally:
        if tmp_xwd and os.path.exists(tmp_xwd):
            os.unlink(tmp_xwd)
        if tmp_png and os.path.exists(tmp_png):
            os.unlink(tmp_png)


def _is_blank(path):
    """Return True if *path* is mostly blank/white."""
    from PIL import Image
    img = Image.open(path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    pixels = list(img.get_flattened_data())
    white = sum(1 for p in pixels if p[0] > 240 and p[1] > 240 and p[2] > 240)
    if white / len(pixels) > 0.95:
        return True
    # All-black is only blank in Docker (Xvfb may produce black frames)
    if os.path.exists("/.dockerenv"):
        black = sum(1 for p in pixels if p[0] < 15 and p[1] < 15 and p[2] < 15)
        if black / len(pixels) > 0.95:
            return True
    return False


def _imagemagick_trim(src_path, dst_path):
    """Crop *src_path* using ImageMagick's -trim as a fallback."""
    subprocess.run(
        ["convert", src_path, "-trim", "+repage", "-strip", dst_path],
        capture_output=True, check=True, timeout=10,
    )


def _is_marker_pixel(pixel):
    """Return True for a marker's magenta or yellow, allowing palette drift."""
    r, g, b = pixel[0], pixel[1], pixel[2]
    magenta = r > 150 and b > 150 and g < 100 and abs(r - b) < 80
    yellow = r > 150 and g > 140 and b < 100 and abs(r - g) < 110
    warm = r > 110 and r - g > 70 and r - b > 70 and b < 80
    return magenta or yellow or warm


def _is_marker_edge(pixel):
    """Return True for a pixel blended between a marker color and the background."""
    r, g, b = pixel[0], pixel[1], pixel[2]
    return (r - g > 80 and b - g > 80) or (r - b > 80 and g - b > 80)


_MIN_MARKER_RUN = 6
_MIN_MARKER_HEIGHT = 12


def _marker_runs(px, y, width):
    """Return the horizontal runs of marker pixels in row *y*."""
    runs = []
    start = None
    for x in range(width):
        if _is_marker_pixel(px[x, y]):
            if start is None:
                start = x
        elif start is not None:
            if x - start >= _MIN_MARKER_RUN:
                runs.append((start, x - 1))
            start = None
    if start is not None and width - start >= _MIN_MARKER_RUN:
        runs.append((start, width - 1))
    return runs


def _marker_blocks(px, width, height):
    """Return ``(x1, y1, x2, y2)`` for each block of marker pixels.

    A checkerboard's two cell rows can be separated by one blended row that
    fails the color test, so a single empty row is tolerated inside a block.
    """
    blocks = []
    current = []
    gap = 0
    for y in range(height):
        runs = _marker_runs(px, y, width)
        if runs:
            run_x1 = min(run[0] for run in runs)
            run_x2 = max(run[1] for run in runs)
            if not current or gap >= 2:
                if current:
                    blocks.append(current)
                current = [run_x1, y, run_x2, y]
            else:
                current[0] = min(current[0], run_x1)
                current[2] = max(current[2], run_x2)
                current[3] = y
            gap = 0
        else:
            gap += 1
    if current:
        blocks.append(current)
    return blocks


def _crop_to_markers(src_path, dst_path):
    """Crop *src_path* to the rectangle bounded by the two checkerboards.

    The top-left marker supplies the left and top edges, the bottom-right
    marker the right and bottom edges.  One extra pixel is included on a side
    where the marker's anti-aliased edge is still visible.
    """
    from PIL import Image
    img = Image.open(src_path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    w, h = img.size
    px = img.load()

    blocks = [block for block in _marker_blocks(px, w, h)
              if block[3] - block[1] + 1 >= _MIN_MARKER_HEIGHT]
    if not blocks:
        _imagemagick_trim(src_path, dst_path)
        return

    # The two markers are the tallest blocks; window chrome can contain
    # smaller patches of the same colors.
    tallest = max(block[3] - block[1] + 1 for block in blocks)
    blocks = [block for block in blocks
              if block[3] - block[1] + 1 >= tallest / 2]
    top = min(blocks, key=lambda block: block[1])
    bottom = max(blocks, key=lambda block: block[3])
    if top[1] >= bottom[1]:
        _imagemagick_trim(src_path, dst_path)
        return

    x1, y1, top_x2, top_y2 = top
    bottom_x1, bottom_y1, x2, y2 = bottom

    if x1 > 0 and any(_is_marker_edge(px[x1 - 1, y])
                      for y in range(y1, top_y2 + 1)):
        x1 -= 1
    if x2 + 1 < w and any(_is_marker_edge(px[x2 + 1, y])
                          for y in range(bottom_y1, y2 + 1)):
        x2 += 1
    if y1 > 0 and any(_is_marker_edge(px[x, y1 - 1])
                      for x in range(x1, top_x2 + 1)):
        y1 -= 1
    if y2 + 1 < h and any(_is_marker_edge(px[x, y2 + 1])
                          for x in range(bottom_x1, x2 + 1)):
        y2 += 1

    img.crop((x1, y1, x2 + 1, y2 + 1)).save(dst_path)
    subprocess.run(
        ["convert", dst_path, "-strip", dst_path],
        capture_output=True, check=True, timeout=10,
    )


def _clear_screen(term):
    """Blank the visible screen one line at a time with EL.

    Erasing the display (``CSI 2J``) is not a plain clear on every terminal:
    OTTY scrolls the erased lines into history, and its viewport then keeps
    showing them, so successive screens stack down the window.
    """
    parts = [term.move_yx(row, 0) + term.clear_eol
             for row in range(term.height)]
    parts.append(term.move_yx(0, 0))
    sys.stdout.write("".join(parts))
    sys.stdout.flush()


def display_and_capture(term, wchars, expected_width, measured_width,
                        output_path, window_id, has_text_sizing=False,
                        software_name=None):
    """Display a single failure and capture a screenshot."""
    hbar, vbar, cross = "━", "┃", "╋"
    LEFT_PAD, TOP_PAD = 2, 1
    PAD = 4

    sys.stdout.write("\x1b[?25l")  # hide cursor

    printc = functools.partial(print, end=term.clear_eol + "\n")

    text = decode_wchars(wchars)
    display_width = wcwidth.wcswidth(text)

    def _box(box_width, content, *, heading=None):
        """Render a measurement box.  Returns (interior_width, heading_width)."""
        interior = box_width + PAD * 2 + 4
        dots = "•" * PAD
        inner = (term.magenta(dots + f"•{vbar}") + term.normal + content
                 + term.magenta(f"{vbar}•" + dots))

        ws = str(box_width)
        mpad = max(0, box_width - len(ws))
        wm = "╂" + "┰" * mpad + ws + "╂"
        lf = (interior - len(wm)) // 2
        rf = interior - len(wm) - lf
        top = cross + hbar * lf + wm + hbar * rf + cross
        bottom = cross + term.center("", interior, fillchar=hbar) + cross

        if heading is not None:
            printc(prefix)
            printc(prefix + term.normal + heading)
        printc(prefix + term.cyan(top))
        printc(prefix + term.cyan(vbar) + inner + term.cyan(vbar))
        printc(prefix + term.cyan(bottom))

        return interior, len(heading) if heading else 0

    _clear_screen(term)

    # Top-left crop marker: 2×2 magenta block (padded by TOP_PAD, LEFT_PAD)
    top_marker_row = TOP_PAD + 1
    marker_row1, marker_row2 = _marker_cells(term)
    sys.stdout.write(
        f"\x1b[{top_marker_row};{LEFT_PAD + 1}H{marker_row1}{term.clear_eol}")
    sys.stdout.write(
        f"\x1b[{top_marker_row + 1};{LEFT_PAD + 1}H{marker_row2}{term.clear_eol}")
    sys.stdout.flush()

    content_row = top_marker_row + 3
    sys.stdout.write(f"\x1b[{content_row};1H")
    sys.stdout.flush()

    prefix = " " * LEFT_PAD

    # Table 1: measured by wcwidth (no terminal overrides)
    interior, _ = _box(expected_width, text)
    max_interior = interior
    max_heading = 0
    extra_tables = 0

    # Table 2: kitty text sizing protocol
    if has_text_sizing:
        si, hw = _box(expected_width, term.text_sized(text, width=expected_width),
                      heading="This terminal supports kitty text sizing protocol:")
        max_interior = max(max_interior, si)
        max_heading = max(max_heading, hw)
        extra_tables += 1

    # Table 3: wcwidth with term_program overrides
    if (software_name
            and (cw := wcwidth.wcstwidth(text, term_program=software_name)) != display_width):
        ci, hw = _box(cw, text,
                      heading=(f"This may be corrected using wcstwidth("
                               f"'…', term_program='{software_name}'):"))
        max_interior = max(max_interior, ci)
        max_heading = max(max_heading, hw)
        extra_tables += 1

    # Bottom-right crop marker: max of content widths + margin
    # Shifted right by LEFT_PAD, down by TOP_PAD + 2 (2-row top marker + gap)
    marker_col = max(
        interior + max(0, measured_width - expected_width) + 5 + LEFT_PAD,
        max_interior + 5 + LEFT_PAD,
        max_heading + 3 + LEFT_PAD,
    )
    marker_row = 6 + extra_tables * 4 + TOP_PAD + 2
    sys.stdout.write(
        f"\x1b[{marker_row};{marker_col}H{marker_row1}{term.clear_eol}")
    sys.stdout.write(
        f"\x1b[{marker_row + 1};{marker_col}H{marker_row2}{term.clear_eol}")
    sys.stdout.flush()

    # Drain stale input (e.g. from does_text_sizing probe) so the CPR
    # response we read is genuinely our own.
    term.flushinp(timeout=0.05)

    # Sync: wait for terminal to finish processing escape sequences
    term.get_location(timeout=2)

    # Settle: nudge a repaint and wait for the framebuffer to catch up.
    # CPR confirms the terminal parsed our bytes, but pixel rendering is async.
    # FocusIn via xdotool triggers repaint (pattern from modem.xyz renderer).
    subprocess.run(
        ["xdotool", "windowfocus", "--sync", str(window_id)],
        capture_output=True, timeout=2,
    )
    time.sleep(0.15)

    # Second sync for slow compositors (weston, Xwayland)
    term.get_location(timeout=1)
    time.sleep(0.1)

    for _ in range(5):
        capture_window(window_id, output_path)
        if not _is_blank(output_path):
            break
        time.sleep(0.5)

    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()

    # Post-capture settle: let the framebuffer finish swapping before the
    # next iteration writes new content.  Without this, the next CPR sync
    # may return before the current render lands on screen, causing shot N
    # to capture pixels from shot N-1.
    time.sleep(0.05)

    if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
        print(f"Error: screenshot not written to {output_path}", file=sys.stderr)
        return False

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Display unicode characters and capture screenshots")
    parser.add_argument("--batch", required=True,
                        help="JSON file with array of failure records")
    parser.add_argument("--window-id",
                        help="X11 window ID to capture (skips find_own_window)")
    args = parser.parse_args()

    if not shutil.which("xdotool") or not shutil.which("xwd"):
        print("Error: xdotool and xwd are required for screenshot capture",
              file=sys.stderr)
        sys.exit(1)

    with open(args.batch) as f:
        records = json.load(f)

    # Find window once using the first record's title
    if args.window_id:
        window_id = args.window_id
    else:
        first_title = records[0].get("title", "ucs-detect-screenshot") if records else "ucs-detect-screenshot"
        set_window_title(first_title)
        time.sleep(0.5)
        window_id = find_own_window(first_title)
    if window_id is None:
        print("Error: could not find terminal window", file=sys.stderr)
        sys.exit(1)

    # Create terminal and probe text sizing support once
    from blessed import Terminal
    term = Terminal()
    has_text_sizing = bool(term.does_text_sizing(timeout=1))

    software_name = records[0].get("software_name") if records else None

    failed = 0
    for record in records:
        wchars = record["wchars"]
        expected_width = record["expected_width"]
        measured_width = record["measured_width"]
        output_path = record["output"]

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        if not display_and_capture(term, wchars, expected_width, measured_width,
                                   output_path, window_id, has_text_sizing,
                                   software_name):
            failed += 1

    if failed:
        print(f"{failed} screenshot(s) failed", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
