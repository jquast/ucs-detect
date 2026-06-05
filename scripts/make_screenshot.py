#!/usr/bin/env python3
"""Display unicode characters with width measurements and capture screenshots.

Runs inside a terminal emulator.  Reads a JSON batch file of failure records.
For each record, displays a simplified ``--stop-at-error``-style box with
``measured by terminal`` / ``measured by wcwidth``, captures its own X11 window,
and saves a trimmed PNG.
"""
import argparse
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
    """Return (row1_str, row2_str) — a 2×2 checkerboard of magenta and yellow."""
    mc = term.on_color_rgb(255, 0, 255)
    yc = term.on_color_rgb(255, 255, 0)
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


def _crop_to_markers(src_path, dst_path):
    """Crop *src_path* to the rectangle bounded by bright-magenta markers."""
    from PIL import Image
    img = Image.open(src_path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    w, h = img.size

    def _is_marker(px):
        r, g, b = px[0], px[1], px[2]
        return (r > 220 and g < 30 and b > 220) or (r > 220 and g > 220 and b < 30)

    # Scan top-down for first marker row
    y1 = None
    for y in range(h):
        for x in range(w):
            if _is_marker(img.getpixel((x, y))):
                y1 = y
                break
        if y1 is not None:
            break

    if y1 is None:
        _imagemagick_trim(src_path, dst_path)
        return

    # Scan bottom-up for last marker row
    y2 = None
    for y in range(h - 1, -1, -1):
        for x in range(w):
            if _is_marker(img.getpixel((x, y))):
                y2 = y
                break
        if y2 is not None:
            break

    y2 = min(h, y2 + 4)
    img.crop((0, y1, w, y2)).save(dst_path)
    subprocess.run(
        ["convert", dst_path, "-strip", dst_path],
        capture_output=True, check=True, timeout=10,
    )


def display_and_capture(term, wchars, expected_width, measured_width,
                        output_path, window_id, has_text_sizing=False,
                        software_name=None):
    """Display a single failure and capture a screenshot."""
    hbar, vbar, cross = "━", "┃", "╋"
    LEFT_PAD, TOP_PAD = 2, 1
    PAD = 4

    sys.stdout.write("\x1b[?25l")  # hide cursor

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
            print(prefix)
            print(prefix + term.normal + heading)
        print(prefix + term.cyan(top))
        print(prefix + term.cyan(vbar) + inner + term.cyan(vbar))
        print(prefix + term.cyan(bottom))

        return interior, len(heading) if heading else 0

    # Clear screen, position cursor
    sys.stdout.write("\x1b[H\x1b[2J")

    # Top-left crop marker: 2×2 magenta block (padded by TOP_PAD, LEFT_PAD)
    top_marker_row = TOP_PAD + 1
    marker_row1, marker_row2 = _marker_cells(term)
    sys.stdout.write(
        f"\x1b[{top_marker_row};{LEFT_PAD + 1}H{marker_row1}")
    sys.stdout.write(
        f"\x1b[{top_marker_row + 1};{LEFT_PAD + 1}H{marker_row2}")
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
        f"\x1b[{marker_row};{marker_col}H{marker_row1}")
    sys.stdout.write(
        f"\x1b[{marker_row + 1};{marker_col}H{marker_row2}")
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
