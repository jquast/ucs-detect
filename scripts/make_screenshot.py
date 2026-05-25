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

from ucs_detect.accessories import decode_wchars
from ucs_detect.measure import _wcswidth_vs15


def set_window_title(title):
    """Set the X11 window title via OSC escape sequence."""
    sys.stdout.write(f"\x1b]0;{title}\x07")
    sys.stdout.flush()


def find_own_window(title, timeout=5):
    """Find our containing terminal window by searching for *title*."""
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

    # Fallback: try getactivewindow
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
    """Capture *window_id* to *output_path* as a trimmed PNG."""
    tmp_xwd = None
    try:
        tmp_xwd = tempfile.mktemp(suffix=".xwd")
        # xwd may fail with BadMatch on window resize races; retry once.
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
        subprocess.run(
            ["convert", tmp_xwd, "-trim", "+repage", output_path],
            capture_output=True, check=True, timeout=10,
        )
    finally:
        if tmp_xwd and os.path.exists(tmp_xwd):
            os.unlink(tmp_xwd)


def display_and_capture(term, wchars, expected_width, measured_width,
                        output_path, window_id, has_text_sizing=False):
    """Display a single failure and capture a screenshot."""
    hbar = "━"
    vbar = "┃"
    cross = "╋"

    text = decode_wchars(wchars)
    display_width = _wcswidth_vs15(text)

    padding = 4
    interior = display_width + padding * 2 + 4  # +4 for "•+" and "+•"
    dots = "•" * padding
    inner = (term.magenta(dots + f"•{vbar}") + term.normal + text
             + term.magenta(f"{vbar}•" + dots))

    # Top border with expected-width marker aligned to text width
    wstr = str(expected_width)
    marker_pad = max(0, expected_width - len(wstr))
    width_str = "╂" + "┰" * marker_pad + wstr + "╂"
    left_fill = (interior - len(width_str)) // 2
    right_fill = interior - len(width_str) - left_fill
    top = cross + hbar * left_fill + width_str + hbar * right_fill + cross

    # Bottom border, simple fill
    bottom = cross + term.center("", interior, fillchar=hbar) + cross

    # Clear screen, position cursor
    sys.stdout.write("\x1b[H\x1b[2J")
    sys.stdout.write("\x1b[2;1H")
    sys.stdout.flush()

    print(term.cyan(top))
    print(term.cyan(vbar) + inner + term.cyan(vbar))
    print(term.cyan(bottom))

    if has_text_sizing:
        sized_raw = term.text_sized(text, width=expected_width)
        sized_dots = "•" * padding
        sized_inner = (term.magenta(sized_dots + f"•{vbar}") + term.normal + sized_raw
                       + term.magenta(f"{vbar}•" + sized_dots))

        print()
        print(term.normal + "This terminal supports kitty text sizing protocol:")
        print(term.cyan(top))
        print(term.cyan(vbar) + sized_inner + term.cyan(vbar))
        print(term.cyan(bottom))
    sys.stdout.flush()

    # Drain stale input (e.g. from does_text_sizing probe) so the CPR
    # response we read is genuinely our own.
    try:
        term.flushinp(timeout=0.05)
    except Exception:
        pass

    # Sync: wait for terminal to finish processing escape sequences
    try:
        term.get_location(timeout=2)
    except Exception:
        pass

    # Settle: nudge a repaint and wait for the framebuffer to catch up.
    # CPR confirms the terminal parsed our bytes, but pixel rendering is async.
    # FocusIn via xdotool triggers repaint (pattern from modem.xyz renderer).
    subprocess.run(
        ["xdotool", "windowfocus", "--sync", str(window_id)],
        capture_output=True, timeout=2,
    )
    time.sleep(0.05)

    capture_window(window_id, output_path)

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
    args = parser.parse_args()

    if not shutil.which("xdotool") or not shutil.which("xwd"):
        print("Error: xdotool and xwd are required for screenshot capture",
              file=sys.stderr)
        sys.exit(1)

    with open(args.batch) as f:
        records = json.load(f)

    # Find window once using the first record's title
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

    failed = 0
    for record in records:
        wchars = record["wchars"]
        expected_width = record["expected_width"]
        measured_width = record["measured_width"]
        output_path = record["output"]

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        if not display_and_capture(term, wchars, expected_width, measured_width,
                                   output_path, window_id, has_text_sizing):
            failed += 1

    if failed:
        print(f"{failed} screenshot(s) failed", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
