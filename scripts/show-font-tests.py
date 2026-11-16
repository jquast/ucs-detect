#!/usr/bin/env python3
"""Print the ASCII font test cells recorded in terminal data YAML files."""

# std imports
import os
import sys
import glob
import argparse

# 3rd party
import yaml


def load_section(path):
    """Return the ``font_test_results`` section of *path*, or None."""
    with open(path, encoding='utf-8') as stream:
        data = yaml.safe_load(stream) or {}
    return data.get('font_test_results')


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', default='data',
                        help='Directory holding terminal data YAML files')
    parser.add_argument('terminals', nargs='*',
                        help='Limit output to these software names')
    args = parser.parse_args()
    wanted = {name.lower() for name in args.terminals}
    found = 0
    for path in sorted(glob.glob(os.path.join(args.data_dir, '*.yaml'))):
        if os.path.basename(path).startswith('_'):
            continue
        section = load_section(path)
        if not section:
            continue
        name = os.path.splitext(os.path.basename(path))[0]
        if wanted and name.lower() not in wanted:
            continue
        found += 1
        grapheme = section.get('grapheme', {})
        print(f"== {name}: {grapheme.get('codepoint', '?')} "
              f"{grapheme.get('name', '')} "
              f"(Emoji {grapheme.get('emoji_version', '?')}, "
              f"Unifont {section.get('font_version', '?')})")
        print(f"   ink {section.get('ink_fraction', 0):.3f}, "
              f"color {section.get('ink_color')}, "
              f"monochrome {section.get('monochrome')}")
        for line in section.get('ascii', ()):
            print(f'   {line}')
        control = section.get('control')
        if control:
            control_grapheme = control.get('grapheme', {})
            print(f"   control {control_grapheme.get('codepoint', '?')} "
                  f"{control_grapheme.get('name', '')}: "
                  f"ink {control.get('ink_fraction', 0):.3f}, "
                  f"monochrome {control.get('monochrome')}")
            for line in control.get('ascii', ()):
                print(f'   {line}')
    if not found:
        print('No font test results found', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
