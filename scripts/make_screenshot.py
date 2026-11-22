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
_SCRIPTS_DIR = os.path.join(_PROJECT_DIR, "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

import capture_cli
from ucs_detect import imaging, wcwidth
from ucs_detect.accessories import display_lock, decode_wchars
from ucs_detect.tasks import TaskPool

#: Seconds to wait before each retry when the crop markers are missing.  A GPU terminal renders
#: asynchronously, so the first pages of a cold window need longer than a warm one.
CAPTURE_RETRY_DELAYS = (0.15, 0.25, 0.4, 0.55, 0.75, 1.0, 1.25, 1.65)


def _marker_cells(term):
    # The 256 color layer is the fallback for GNU Screen with truecolor off,
    # which drops the 48;2 sequence.
    mc = "\x1b[45m\x1b[105m\x1b[48;5;201m\x1b[48;2;255;0;255m"
    yc = "\x1b[43m\x1b[103m\x1b[48;5;226m\x1b[48;2;255;255;0m"
    row1 = mc + " " + yc + " " + term.normal
    row2 = yc + " " + mc + " " + term.normal
    return row1, row2


def marker_column(term_width, desired):
    """Return the column of the bottom-right crop marker."""
    return max(1, min(desired, term_width - 2))


def capture_marked_page(window_id, output_path, pool):
    """Capture *window_id* and hand the marker crop to *pool*.

    The page is not written when the markers never appear: a frame captured before the terminal
    rendered would crop to the shell prompt and silently replace the real screenshot.
    """
    raw_path = tempfile.mktemp(suffix=".png")
    attempts = len(CAPTURE_RETRY_DELAYS) + 1
    for attempt in range(attempts):
        try:
            imaging.capture_window_raw(window_id, raw_path)
        except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
            if os.path.exists(raw_path):
                os.unlink(raw_path)
            return f"capture failed: {error}"
        if imaging.has_capture_markers(raw_path):
            pool.submit(imaging.finish_capture, raw_path, output_path,
                        label=output_path)
            return None
        if attempt < attempts - 1:
            imaging.focus_window(window_id)
            time.sleep(CAPTURE_RETRY_DELAYS[attempt])
    if os.path.exists(raw_path):
        os.unlink(raw_path)
    return f"markers missing from {attempts} captures"


def _clear_screen(term):
    parts = [term.move_yx(row, 0) + term.clear_eol
             for row in range(term.height)]
    parts.append(term.move_yx(0, 0))
    sys.stdout.write("".join(parts))
    sys.stdout.flush()


def display_and_capture(term, wchars, expected_width, measured_width,
                        output_path, window_id, has_text_sizing=False,
                        software_name=None, pool=None):
    """Display a single failure and capture a screenshot."""
    pool = pool or TaskPool()
    hbar, vbar = "━", "┃"
    cross_left, cross_right = "┣", "┫"
    LEFT_PAD, TOP_PAD = 2, 1
    PAD = 4

    sys.stdout.write("\x1b[?25l")  # hide cursor

    printc = functools.partial(print, end=term.clear_eol + "\n")

    text = decode_wchars(wchars)
    display_width = wcwidth.wcswidth(text)

    def _chrome(characters):
        return term.on_magenta(term.cyan(characters))

    def _box(box_width, content, *, heading=None):
        interior = box_width + PAD * 2 + 4
        dots = "•" * PAD
        inner = (_chrome(dots + f"•{vbar}") + term.normal
                 + term.center(content, box_width)
                 + _chrome(f"{vbar}•" + dots))

        ws = str(box_width)
        mpad = max(0, box_width - len(ws))
        wm = "╂" + "┰" * mpad + ws + "╂"
        lf = (interior - len(wm)) // 2
        rf = interior - len(wm) - lf
        top = cross_left + hbar * lf + wm + hbar * rf + cross_right
        bottom = (cross_left + term.center("", interior, fillchar=hbar)
                  + cross_right)

        if heading is not None:
            printc(prefix)
            printc(prefix + term.normal + heading)
        printc(prefix + term.cyan(top))
        printc(prefix + _chrome(vbar) + inner + _chrome(vbar) + term.normal)
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
    marker_col = marker_column(term.width, max(
        interior + max(0, measured_width - expected_width) + 5 + LEFT_PAD,
        max_interior + 5 + LEFT_PAD,
        max_heading + 3 + LEFT_PAD,
    ))
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
    # The focus stays inside the display lock: a terminal staged beside this one
    # that took the focus could receive the next stage's keystrokes.
    with display_lock():
        imaging.focus_window(window_id)
        time.sleep(0.15 + imaging.capture_delay())

        # Second sync for slow compositors (weston, Xwayland)
        term.get_location(timeout=1)
        time.sleep(0.1)

        error = capture_marked_page(window_id, output_path, pool)

    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()

    # Post-capture settle: let the framebuffer finish swapping before the
    # next iteration writes new content.  Without this, the next CPR sync
    # may return before the current render lands on screen, causing shot N
    # to capture pixels from shot N-1.
    time.sleep(0.05)

    return error


def write_status(path, errors):
    """Record the recoverable image errors for the driver, when it asked for them."""
    if not path:
        return
    try:
        with open(path, "w", encoding="utf-8") as stream:
            json.dump({"errors": errors}, stream)
    except OSError as error:
        print(f"Error: cannot write {path}: {error}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Display unicode characters and capture screenshots")
    parser.add_argument("--batch", required=True,
                        help="JSON file with array of failure records")
    parser.add_argument("--window-id",
                        help="X11 window ID to capture (skips find_own_window)")
    parser.add_argument("--window-id-file",
                        help="File where the driver writes the X11 window ID")
    parser.add_argument("--status-file",
                        help="JSON file where image errors are reported")
    parser.add_argument("--workers", type=int, default=1,
                        help="Processes cropping captures (default: 1, inline)")
    parser.add_argument("--capture-delay-ms", type=int, default=0,
                        help="Extra milliseconds to wait after rendering "
                             "before the window is captured")
    args = parser.parse_args()

    imaging.set_capture_delay(args.capture_delay_ms)

    if not imaging.require_capture_tools():
        print("Error: the capture tools for this platform are required "
              "for screenshot capture", file=sys.stderr)
        sys.exit(1)

    with open(args.batch) as f:
        records = json.load(f)

    first_title = (records[0].get("title", "ucs-detect-screenshot")
                   if records else "ucs-detect-screenshot")
    imaging.set_window_title(first_title)
    window_id = args.window_id or capture_cli.wait_for_window_id(
        args.window_id_file)
    if window_id is None:
        time.sleep(0.5)
        window_id = imaging.find_own_window(first_title)
    if window_id is None:
        print("Error: could not find terminal window", file=sys.stderr)
        sys.exit(1)

    imaging.try_fullscreen(
        window_id, max_size=imaging.SCREENSHOT_MAX_SIZE)

    # Create terminal and probe text sizing support once
    from blessed import Terminal
    term = Terminal()
    has_text_sizing = bool(term.does_text_sizing(timeout=1))

    software_name = records[0].get("software_name") if records else None

    errors = []
    with TaskPool(args.workers) as pool:
        for record in records:
            wchars = record["wchars"]
            expected_width = record["expected_width"]
            measured_width = record["measured_width"]
            output_path = record["output"]

            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            error = display_and_capture(
                term, wchars, expected_width, measured_width,
                output_path, window_id, has_text_sizing,
                software_name, pool=pool)
            if error:
                print(f"Error: {output_path}: {error}", file=sys.stderr)
                errors.append({"output": output_path, "error": error})
        pool.collect()

    errors.extend({"output": failure.label, "error": failure.message}
                  for failure in pool.errors)
    write_status(args.status_file, errors)
    if errors:
        print(f"{len(errors)} recoverable image error(s)", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
