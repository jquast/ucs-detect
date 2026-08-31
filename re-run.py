#!/usr/bin/env python3
"""Re-run ucs-detect with arguments from a saved YAML file."""
import os
import shlex
import argparse
import textwrap
import subprocess
import sys

EPILOG = textwrap.dedent("""\
    Arguments after yaml_file must be separated with '--' as arguments to 'ucs-detect' CLI

        re-run.py data/securecrt.yaml -- --all
        re-run.py data/securecrt.yaml -- --limit-category-time 60
    """)


def main():
    parser = argparse.ArgumentParser(
        usage='%(prog)s yaml_file [-- ucs-detect-arg ...]',
        description='Re-run ucs-detect with arguments from a saved YAML file.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EPILOG)
    parser.add_argument('yaml_file',
                        help='saved report to restore session_arguments from, and save back to')
    parser.add_argument('extra_args', nargs='*', metavar='ucs-detect-arg',
                        help="arguments passed through to ucs-detect, after a '--' separator")
    args = parser.parse_args()

    if not os.path.exists(args.yaml_file):
        print(f"Error: File not found: {args.yaml_file}", file=sys.stderr)
        sys.exit(1)

    # ucs-detect --rerun restores 'session_arguments' from the file itself; anything
    # given here is passed through and takes precedence over the restored value.
    cmd = ['ucs-detect', '--rerun', str(args.yaml_file)]

    if args.extra_args:
        extra = args.extra_args
        if extra and extra[0] == "--":
            extra = extra[1:]
        if extra:
            cmd.extend(extra)

    print(f"Running: {shlex.join(cmd)}")

    subprocess.check_call(cmd)


if __name__ == '__main__':
    sys.exit(main())
