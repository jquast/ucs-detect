"""Generate Standalone Regional Indicator table data for ucs_detect."""
import wcwidth


def fetch_sri_data():
    """List standalone Regional Indicator codepoints (U+1F1E6-U+1F1FF)."""
    version = wcwidth.list_versions()[-1]
    codepoints = list(range(0x1F1E6, 0x1F1FF + 1))
    return [(version, codepoints)]


def main():
    """Generate and write the SRI unicode table module."""
    import textwrap
    print("STANDALONE_REGIONAL_INDICATORS = (")
    for key, codepoints in fetch_sri_data():
        print(f"    ('{key}', (")
        line = ", ".join(str(cp) for cp in codepoints)
        for wrapped in textwrap.wrap(line, width=88, break_on_hyphens=False):
            print(f"        {wrapped}")
        print("    )),")
    print(")")


if __name__ == "__main__":
    # $ python scripts/make_sri_table.py > ucs_detect/table_sri.py
    main()
