"""Generate narrow character table data for ucs_detect."""
import wcwidth


def fetch_narrow_data():
    """List all NARROW (width-1) characters for the latest unicode version."""
    version = wcwidth.list_versions()[-1]
    codepoints = []
    for cp in range(0x3FFFE):
        ch = chr(cp)
        if wcwidth.wcswidth(ch) == 1:
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
