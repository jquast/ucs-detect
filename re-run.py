#!/usr/bin/env python3
"""Re-run ucs-detect with arguments from a saved YAML file."""

import argparse
import subprocess
import sys
from pathlib import Path

import yaml


def build_command_from_yaml(yaml_file: Path) -> list[str]:
    """Build ucs-detect command from YAML file.

    Args:
        yaml_file: Path to YAML file containing session_arguments

    Returns:
        Command line arguments as list of strings
    """
    with open(yaml_file) as f:
        data = yaml.safe_load(f)

    session_args = data.get('session_arguments', {})

    cmd = ['ucs-detect']

    # Map YAML keys to CLI arguments
    arg_mapping = {
        'stream': '--stream',
        'limit_codepoints': '--limit-codepoints',
        'limit_words': '--limit-words',
        'limit_errors': '--limit-errors',
        'unicode_version': '--unicode-version',
        'timeout': '--timeout',
        'stop_at_error': '--stop-at-error',
    }

    # Boolean flags (only add if True)
    bool_flags = {
        'quick': '--quick',
        'shell': '--shell',
        'no_terminal_test': '--no-terminal-test',
        'no_languages_test': '--no-languages-test',
        'no_emit_osc1337': '--no-emit-osc1337',
    }

    # Add arguments with values
    for yaml_key, cli_arg in arg_mapping.items():
        if yaml_key in session_args:
            value = session_args[yaml_key]
            if value is not None:
                cmd.extend([cli_arg, str(value)])

    # Add boolean flags
    for yaml_key, cli_flag in bool_flags.items():
        if session_args.get(yaml_key):
            cmd.append(cli_flag)

    # Always add --save-yaml with the original file path
    cmd.extend(['--save-yaml', str(yaml_file)])

    return cmd


def main():
    """Parse arguments and re-run ucs-detect."""
    parser = argparse.ArgumentParser(
        description='Re-run ucs-detect with arguments from a saved YAML file.'
    )
    parser.add_argument(
        'yaml_file',
        type=Path,
        help='Path to YAML file (e.g., data/linux-6.14.0-33-fbdev.yaml)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print command without executing'
    )

    args = parser.parse_args()

    if not args.yaml_file.exists():
        print(f"Error: File not found: {args.yaml_file}", file=sys.stderr)
        sys.exit(1)

    cmd = build_command_from_yaml(args.yaml_file)

    print(f"Running: {' '.join(cmd)}")

    if args.dry_run:
        return 0

    try:
        result = subprocess.run(cmd, check=False)
        return result.returncode
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        return 130
    except Exception as e:
        print(f"Error running command: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
