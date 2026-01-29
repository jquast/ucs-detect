import wcwidth


def fetch_wide_data():
    """List all WIDE characters for the latest unicode version."""
    table = wcwidth.WIDE_EASTASIAN
    version = wcwidth.list_versions()[-1]
    codepoints = []
    for value_pair in table[version]:
        for value in range(value_pair[0], value_pair[1] + 1):
            codepoints.append(value)
    return [(version, codepoints)]


def main():
    import textwrap
    print("WIDE_CHARACTERS = (")
    for key, codepoints in fetch_wide_data():
        print(f"  ('{key}', (")
        line = ", ".join(str(cp) for cp in codepoints)
        for wrapped in textwrap.wrap(line, width=88, break_on_hyphens=False):
            print(f"    {wrapped}")
        print("  )),")
    print(")")


if __name__ == "__main__":
    # minimal wide table parser, for use:
    # $ python make_wide_table.py > ucs_detect/table_wide.py
    main()
