"""Generate narrow character table data for ucs_detect."""
import os
import urllib.request

import wcwidth

URL_DERIVED_AGE = "https://www.unicode.org/Public/{version}/ucd/DerivedAge.txt"
PATH_DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def _is_drawable(cp):
    """Return False for surrogates and noncharacters, which carry an age but are never drawn."""
    return not (0xD800 <= cp <= 0xDFFF
                or 0xFDD0 <= cp <= 0xFDEF
                or (cp & 0xFFFE) == 0xFFFE)


def fetch_assigned(version):
    """
    Return the set of assigned, drawable codepoints in *version*.

    :param str version: Unicode version, as reported by :func:`wcwidth.list_versions`.
    :returns: all codepoints with an age in DerivedAge.txt, except surrogates and noncharacters.
    :rtype: set
    """
    fname = os.path.join(PATH_DATA, f"DerivedAge-{version}.txt")
    if not os.path.exists(fname):
        os.makedirs(PATH_DATA, exist_ok=True)
        urllib.request.urlretrieve(URL_DERIVED_AGE.format(version=version), fname)
    assigned = set()
    with open(fname, encoding="utf-8") as fin:
        for line in fin:
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            codepoint_range, _age = (field.strip() for field in line.split(";"))
            start, _, end = codepoint_range.partition("..")
            assigned.update(cp for cp in range(int(start, 16), int(end or start, 16) + 1)
                            if _is_drawable(cp))
    return assigned


def fetch_narrow_data():
    """List all NARROW (width-1) characters for the latest unicode version."""
    version = wcwidth.list_versions()[-1]
    assigned = fetch_assigned(version)
    codepoints = []
    for cp in range(0x3FFFE):
        if cp not in assigned:
            continue
        if wcwidth.wcswidth(chr(cp)) == 1:
            codepoints.append(cp)
    return [(version, codepoints)]


def main():
    """Generate and write the NARROW unicode table module."""
    import textwrap
    print('NARROW_CHARACTERS = (')
    for key, codepoints in fetch_narrow_data():
        print(f"    ('{key}', (")
        line = ", ".join(str(cp) for cp in codepoints)
        for wrapped in textwrap.wrap(line, width=88, break_on_hyphens=False):
            print(f"        {wrapped}")
        print("    )),")
    print(')')


if __name__ == '__main__':
    main()
