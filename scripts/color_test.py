#!/usr/bin/env python3
"""Measure the default 16 colors a terminal renders.

Runs inside the terminal under test.  It paints the 16 configurable palette colors, captures the
page, and records the measured RGB values in the terminal data YAML under ``color_results``.

Usage::

    python scripts/color_test.py --yaml data/xterm.yaml
"""

# std imports
import os
import sys
import time
import shutil
import tempfile

# pylint: disable=wrong-import-position

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_DIR not in sys.path:
    sys.path.insert(0, _PROJECT_DIR)
_SCRIPTS_DIR = os.path.join(_PROJECT_DIR, 'scripts')
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

# local
from capture_cli import build_parser, prepare
from ucs_detect import colors
from ucs_detect.terminal import make_terminal


def main():
    """Entry point."""
    parser = build_parser('Measure the default 16 colors a terminal renders')
    parser.add_argument('--capture-dir', default=None,
                        help='Keep the cropped page capture in this directory')
    args = parser.parse_args()

    prepared = prepare(args, 'ucs-color', 'color test')
    if prepared is None:
        return 1

    term = make_terminal()
    temp_dir = tempfile.mkdtemp(prefix='ucs-color-test-')
    started = time.time()
    try:
        with term.location(), term.cbreak(), \
                term.fullscreen(), term.hidden_cursor():
            calibration, section, _pages = colors.scan(
                term, prepared.window_id, temp_dir,
                capture_dir=args.capture_dir,
                cursor_rows=args.cursor_center_rows)
        colors.write_results(args.yaml, section)
    except Exception as error:  # pylint: disable=broad-except
        print(f'Color test failed: {error}', file=sys.stderr)
        return 1
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    elapsed = time.time() - started
    print(f'{len(section["sixteen"]["colors"])} colors measured in '
          f'{elapsed:.1f}s')
    print(f'cell {calibration.cell_width:.2f}x{calibration.cell_height:.2f}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
