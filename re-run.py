#!/usr/bin/env python3
"""Re-run ucs-detect with arguments from a saved YAML file."""
import os
import shlex
import argparse
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(
        description='Re-run ucs-detect with arguments from a saved YAML file.',
        epilog='Any additional arguments after yaml_file are passed to ucs-detect')
    parser.add_argument('yaml_file')
    parser.add_argument('extra_args', nargs='*', help='Additional arguments to pass to ucs-detect')
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
