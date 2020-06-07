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
    """Program entry point."""
    term = blessed.Terminal(stream=sys.__stderr__)
    assert term.is_a_tty
    # This table was generated with the aide of bin/new-wide-by-version.py in
    # the wcwidth repository, note that 4.1.0 and 5.0.0 have identical wide
    # characters.
    previous_version = '4.1.0'
    wide_by_version = [
        ('5.1.0', '龼'),
        ('5.2.0', '🈯'),
        ('6.0.0', '🈁'),
        ('8.0.0', '🉐'),
        ('9.0.0', '🐹'),
        ('10.0.0', '🦖'),
        ('11.0.0', '🧪'),
        ('12.0.0', '🪐'),
        ('12.1.0', '㋿'),
        ('13.0.0', '🫕'),
    ]

    echo = functools.partial(print, end='', flush=True, file=sys.stderr)

    def get_xpos():
        ypos, xpos = term.get_location(timeout=3.0)
        if -1 in (ypos, xpos):
            echo(term.normal + term.move_x(0) + term.clear_eol)
            echo('ucs-detect: Unicode Version could not be determined!\n')
            sys.exit(1)
        return xpos

    with term.hidden_cursor():
        echo(term.black)
        for version, wchar in wide_by_version:
            start_x = get_xpos()
            echo(wchar)
            end_x = get_xpos()
            echo(term.move_x(0) + term.clear_eol)
            if end_x - start_x != 2:
                break
            previous_version = version
        echo(term.normal)
        print('UNICODE_VERSION={0}; export UNICODE_VERSION'
              .format(previous_version))
    return 0


if __name__ == '__main__':
    sys.exit(main())
