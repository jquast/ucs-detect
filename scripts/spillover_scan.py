#!/usr/bin/env python3
"""Scan contested graphemes for spillover inside a terminal.

Runs inside the terminal under test.  It paints truecolor cell blocks, draws
contested graphemes one per row, captures each page with xwd, compares the page
with and without graphemes, and records the graphemes whose ink crosses the
cursor advance boundary in the terminal data YAML.

Usage::

    python scripts/spillover_scan.py --yaml data/xterm.yaml
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
from ucs_detect import spillover, imaging
from ucs_detect.accessories import safe_name
from ucs_detect.tasks import TaskPool
from ucs_detect.terminal import make_terminal


def main():
    """Entry point."""
    parser = build_parser('Scan contested graphemes for spillover')
    parser.add_argument('--limit', type=int, default=0,
                        help='Test only the first N candidates')
    parser.add_argument('--evidence-dir', default=None,
                        help='Directory for full page spillover images')
    parser.add_argument('--workers', type=int, default=1,
                        help='Processes analysing pages (default: 1, inline)')
    args = parser.parse_args()

    prepared = prepare(args, 'ucs-spillover', 'spillover scan')
    if prepared is None:
        return 1
    imaging.try_fullscreen(prepared.window_id)

    candidates = spillover.contested_graphemes()
    candidates = spillover.apply_measured_advances(candidates, prepared.data)
    if args.limit:
        candidates = candidates[:args.limit]
    if not candidates:
        print('No contested candidates found', file=sys.stderr)
        return 1

    term = make_terminal()
    temp_dir = tempfile.mkdtemp(
        prefix=f'ucs-spillover-{safe_name(prepared.software_name)}-')
    evidence_dir = args.evidence_dir
    if evidence_dir:
        os.makedirs(evidence_dir, exist_ok=True)

    started = time.time()
    keep_temp = False
    with TaskPool(args.workers) as pool:
        try:
            with term.location(), term.cbreak(), \
                    term.fullscreen(), term.hidden_cursor():
                calibration, results, errors, images, shifted, painted_rows = \
                    spillover.scan_terminal(
                        term, prepared.window_id, candidates, temp_dir,
                        evidence_dir=evidence_dir,
                        window_title=prepared.title,
                        name_prefix=safe_name(prepared.software_name),
                        pool=pool,
                        cursor_rows=args.cursor_center_rows)
            section = spillover.build_results(
                calibration, results, errors, len(candidates), images,
                shifted, painted_rows, args.cursor_center_rows)
            spillover.write_results(args.yaml, section)
        except spillover.SpilloverError as error:
            keep_temp = True
            print(f'Spillover scan failed: {error}', file=sys.stderr)
            print(f'Captures kept in {temp_dir}', file=sys.stderr)
            return 1
        except KeyboardInterrupt:
            keep_temp = True
            print('Interrupted', file=sys.stderr)
            print(f'Captures kept in {temp_dir}', file=sys.stderr)
            return 130
        finally:
            pool.collect()
            if not keep_temp:
                shutil.rmtree(temp_dir, ignore_errors=True)

    elapsed = time.time() - started
    print(f'{section["n_tested"]} graphemes in {elapsed:.1f}s, '
          f'{section["n_spillover"]} with spillover, '
          f'{section["n_no_ink"]} with no ink, '
          f'{section["n_shifted"]} on displaced rows')
    if pool.errors:
        print(f'{len(pool.errors)} page analysis error(s)', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
