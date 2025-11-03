#!/usr/bin/env python3
"""Re-run ucs-detect with arguments from a saved YAML file."""
import os
import shlex
import argparse
import subprocess
import sys

import yaml


def build_command_from_yaml(yaml_file):
    with open(yaml_file) as f:
        data = yaml.safe_load(f)

    session_args = data.get('session_arguments', {})

    cmd = ['ucs-detect', '--save-yaml', str(yaml_file)]

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

    return cmd


def main():
    parser = argparse.ArgumentParser(
        description='Re-run ucs-detect with arguments from a saved YAML file.')
    parser.add_argument('yaml_file')
    args = parser.parse_args()

    if not os.path.exists(args.yaml_file):
        print(f"Error: File not found: {args.yaml_file}", file=sys.stderr)
        sys.exit(1)

    cmd = build_command_from_yaml(args.yaml_file)

    print(f"Running: {shlex.join(cmd)}")

    subprocess.check_call(cmd)

if __name__ == '__main__':
    sys.exit(main())
