#!/usr/bin/env python3
"""Render one recent emoji in a terminal and record its cell as ASCII art.

Runs inside the terminal under test, after the width screenshots and before the
spillover scan.  The result is stored in the terminal data YAML under
``font_test_results`` and is used to check that the configured font rendered the
newest codepoint rather than a tofu box.

Usage::

    python scripts/font_test.py --yaml data/xterm.yaml
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
from ucs_detect import fonttest
from ucs_detect.terminal import make_terminal


def main():
    """Entry point."""
    parser = build_parser('Render one emoji and record its cell as ASCII art')
    parser.add_argument('--capture', default=None,
                        help='Keep the captured page at this path')
    args = parser.parse_args()

    prepared = prepare(args, 'ucs-font', 'font test')
    if prepared is None:
        return 1

    term = make_terminal()
    temp_dir = tempfile.mkdtemp(prefix='ucs-font-test-')
    started = time.time()
    try:
        with term.location(), term.cbreak(), \
                term.fullscreen(), term.hidden_cursor():
            calibration, measurements = fonttest.scan(
                term, prepared.window_id, temp_dir,
                capture_path=args.capture)
        section = fonttest.build_section(calibration, measurements)
        fonttest.write_results(args.yaml, section)
    except Exception as error:  # pylint: disable=broad-except
        print(f'Font test failed: {error}', file=sys.stderr)
        return 1
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    elapsed = time.time() - started
    print(f'{section["grapheme"]["codepoint"]} in {elapsed:.1f}s, '
          f'{section["ink_fraction"]:.3f} ink, '
          f'control {section["control"]["ink_fraction"]:.3f}')
    for line in section['ascii']:
        print(line)
    return 0


if __name__ == '__main__':
    sys.exit(main())
