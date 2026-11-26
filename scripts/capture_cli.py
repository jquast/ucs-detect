#!/usr/bin/env python3
"""Command line flags and window lookup shared by the terminal side capture drivers."""

# std imports
import os
import sys
import time
import argparse
import collections

# pylint: disable=wrong-import-position

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_DIR not in sys.path:
    sys.path.insert(0, _PROJECT_DIR)

# local
from ucs_detect import spillover, imaging
from ucs_detect.accessories import load_document

#: Seconds a driver waits for the launcher to write the window id file.
WINDOW_ID_TIMEOUT = 30

#: Terminal data, its software name and window title, and the X11 window id found for it.
Prepared = collections.namedtuple(
    'Prepared', ('data', 'software_name', 'title', 'window_id'))


def build_parser(description):
    """Return an argument parser with the terminal data and window flags."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--yaml', required=True,
                        help='Terminal data YAML to update')
    parser.add_argument('--window-id', default=None,
                        help='X11 window id to capture')
    parser.add_argument('--window-id-file', default=None,
                        help='File where the launcher writes the window id')
    parser.add_argument('--title', default=None,
                        help='Window title used to find the terminal')
    parser.add_argument('--cursor-center-rows', type=int, default=0,
                        help='Terminal rows hidden behind the terminal own '
                             'mouse pointer at the centre of the window')
    parser.add_argument('--capture-delay-ms', type=int, default=0,
                        help='Extra milliseconds to wait after rendering '
                             'before the window is captured')
    parser.add_argument('--draw-delay', type=float,
                        default=spillover.DRAW_DELAY,
                        help='Seconds between painting page bars and drawing '
                             f'glyphs (default: {spillover.DRAW_DELAY})')
    return parser


def wait_for_window_id(path, timeout=WINDOW_ID_TIMEOUT):
    """Return the window id written to *path*, or None after *timeout* seconds."""
    if not path:
        return None
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with open(path, encoding='utf-8') as stream:
                window_id = stream.read().strip()
        except OSError:
            window_id = ''
        if window_id:
            return window_id
        time.sleep(0.1)
    return None


def find_window(args, title):
    """Return the X11 window id of this terminal, or None."""
    imaging.set_window_title(title)
    time.sleep(0.2)
    if args.window_id:
        return args.window_id
    window_id = wait_for_window_id(args.window_id_file)
    if window_id:
        return window_id
    time.sleep(0.5)
    return imaging.find_own_window(title)


def prepare(args, title_prefix, noun):
    """Return a :class:`Prepared` for the terminal data at ``args.yaml``, or None."""
    if not imaging.require_capture_tools():
        print(f'Error: the capture tools for this platform are required '
              f'for the {noun}', file=sys.stderr)
        return None
    imaging.set_capture_delay(args.capture_delay_ms)
    spillover.set_draw_delay(args.draw_delay)
    data = load_document(args.yaml)
    software_name = data.get('software_name', os.path.basename(args.yaml))
    title = args.title or f'{title_prefix}-{software_name}'
    window_id = find_window(args, title)
    if window_id is None:
        print('Error: could not find terminal window', file=sys.stderr)
        return None
    return Prepared(data, software_name, title, window_id)
