#!/usr/bin/env python3
"""Probe a terminal for right to left text layout.

Usage::

    python scripts/bidi_scan.py --yaml data/xterm.yaml
"""

# std imports
import os
import sys
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
from ucs_detect import bidi, imaging, spillover
from ucs_detect.accessories import safe_name
from ucs_detect.terminal import make_terminal


def main():
    """Entry point."""
    parser = build_parser('Detect a right to left layout')
    args = parser.parse_args()

    prepared = prepare(args, 'ucs-bidi', 'bidi scan')
    if prepared is None:
        return 1
    imaging.try_fullscreen(prepared.window_id)

    term = make_terminal()
    temp_dir = tempfile.mkdtemp(
        prefix=f'ucs-bidi-{safe_name(prepared.software_name)}-')
    try:
        with term.location(), term.cbreak(), term.fullscreen(), \
                term.hidden_cursor():
            section = bidi.scan_terminal(
                term, prepared.window_id, temp_dir,
                window_title=prepared.title)
        bidi.write_results(args.yaml, section)
    except spillover.SpilloverError as error:
        print(f'BiDi scan failed: {error}', file=sys.stderr)
        print(f'Captures kept in {temp_dir}', file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print('Interrupted', file=sys.stderr)
        print(f'Captures kept in {temp_dir}', file=sys.stderr)
        return 130

    shutil.rmtree(temp_dir, ignore_errors=True)
    print(f"BiDi {section['supported']}: "
          f"control left {section['control_left']}, "
          f"requested right {section['requested_right']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
