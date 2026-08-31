#!/usr/bin/env python
"""Display the tofus recorded in a ucs-detect yaml data file."""
# std imports
import sys
import unicodedata

# 3rd party
import yaml


def main(filepath):
    """Print the tofus of the ucs-detect yaml data file at *filepath*."""
    with open(filepath, encoding='utf-8') as fin:
        doc = yaml.safe_load(fin)

    for ver, result in doc['test_results']['tofu_results'].items():
        print(f'Unicode {ver}: {result["n_errors"]:,} tofus '
              f'of {result["n_total"]:,} codepoints tested')
        for block_name, block in result['blocks'].items():
            print(f'\n{block_name}: {block["n_errors"]:,}')
            for start, end in block['codepoint_ranges']:
                for codepoint in range(start, end + 1):
                    char = chr(codepoint)
                    print(f'    U+{codepoint:04X} {char} '
                          f'{unicodedata.name(char, "")}')


if __name__ == '__main__':
    main(sys.argv[1])
