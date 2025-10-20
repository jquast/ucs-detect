#!/usr/bin/env python3
"""
Fix encoding errors in UDHR text files.

Some files contain malformed UTF-8 from incorrect Windows-1252 conversion.
Bytes were treated as Unicode codepoints instead of Windows-1252 characters.

  Windows-1252 0x91 -> [wrong] U+0091 -> UTF-8 0xC2 0x91
  Windows-1252 0x91 -> [right] U+2018 -> UTF-8 0xE2 0x80 0x98

  Windows-1252 0x92 -> [wrong] U+0092 -> UTF-8 0xC2 0x92
  Windows-1252 0x92 -> [right] U+2019 -> UTF-8 0xE2 0x80 0x99
"""
import os
import sys

# Add more files here as needed
in_folder = lambda fname: os.path.join(os.path.dirname(__file__), 'ucs_detect', 'udhr', fname)

FIXES = {
    in_folder('udhr_kng_AO.txt'): (b'\xc2\x92', b'\xe2\x80\x99'),
    in_folder('udhr_sco.txt'): (b'\xc2\x91', b'\xe2\x80\x98'),
}


def fix_file(filename: str, find_bytes: bytes, replace_bytes: bytes):
    """Fix encoding in a single file (idempotent with .orig backup)."""
    backup_path = filename + '.orig'
    assert os.path.isfile(filename), filename
    if not os.path.exists(backup_path):
        print(f"creating backup: {backup_path}")
        open(backup_path, 'wb').write(open(filename, 'rb').read())

    # Read and fix
    data = open(filename, 'rb').read()
    count = data.count(find_bytes)

    if count > 0:
        fixed_data = data.replace(find_bytes, replace_bytes)
        open(filename, 'wb').write(fixed_data)
        print(f"{filename}: fixup applied")


def main():
    for filename, (find_bytes, replace_bytes) in FIXES.items():
        fix_file(filename, find_bytes, replace_bytes)


if __name__ == '__main__':
    sys.exit(main())
