#!/usr/bin/env python
"""
ucs-detect: Detects the Unicode Version of an interactive terminal for export

https://github.com/jquast/ucs-detect
"""
from __future__ import print_function

# std imports
import sys
import functools

# 3rd party
import blessed


def main():
    term = blessed.Terminal(stream=sys.__stderr__)
    assert term.is_a_tty
    previous_version = '4.1.0'
    wide_by_version = [
        ('5.0.0', '龼'),
        ('5.1.0', '🈯'),
        ('5.2.0', '🉐'),
        ('8.0.0', '🐹'),
        ('9.0.0', '🦖'),
        ('10.0.0', '🧪'),
        ('11.0.0', '🧬'),
        ('12.0.0', '㋿'),
        ('12.1.0', 'ㆻ'),
    ]
    echo = functools.partial(print, end='', flush=True, file=sys.stderr)
    echo(term.black)
    for version, wchar in wide_by_version:
        _, start_x = term.get_location(timeout=5.0)
        echo(wchar)
        _, end_x = term.get_location(timeout=5.0)
        echo(term.move_x(0) + term.clear_eol)
        if -1 in (start_x, end_x):
            echo(term.normal)
            print('ucs-detect: Unicode Version could not be determined!')
            return 1
        if end_x - start_x != 2:
            break
        previous_version = version
    echo(term.normal)
    print('UNICODE_VERSION={0}; export UNICODE_VERSION'
          .format(previous_version))
    return 0


if __name__ == '__main__':
    sys.exit(main())
