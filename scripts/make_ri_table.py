# pylint: disable=duplicate-code
"""Generate Regional Indicator flag sequence table data for ucs_detect."""
import os
import re

import wcwidth

from ucs_detect.accessories import do_retrieve, get_data_dir

URL_EMOJI_TEST = "https://unicode.org/Public/emoji/{version}/emoji-test.txt"
PATH_DATA = str(get_data_dir())


def fetch_ri_flag_data():
    """Fetch all Regional Indicator flag sequences from the latest emoji spec."""
    fname = os.path.join(PATH_DATA, "emoji-test-latest.txt")
    do_retrieve(url=URL_EMOJI_TEST.format(version="latest"), fname=fname)

    version = "0"
    flag_sequences = []

    in_flags = False
    with open(fname, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# Version:"):
                version = line.split(":")[1].strip()
                continue
            if "# subgroup: country-flag" in line:
                in_flags = True
                continue
            if "# subgroup: subdivision-flag" in line:
                in_flags = True
                continue
            if in_flags and line.startswith("# subgroup:") and "flag" not in line.lower():
                in_flags = False
                continue
            if in_flags and line.strip() and not line.startswith("#"):
                data, _, _ = line.partition("#")
                if "fully-qualified" not in data:
                    continue
                cp_str = data.split(";")[0].strip()
                cps = tuple(int(x, 16) for x in cp_str.split())
                flag_sequences.append(cps)

    return version, flag_sequences


def main():
    """Generate and write the RI unicode table module."""
    version, sequences = fetch_ri_flag_data()
    print("REGIONAL_INDICATOR_FLAGS = (")
    print(f"    ('{version}', (")
    line = ""
    for seq in sequences:
        entry = repr(seq) + ", "
        if len(line) + len(entry) > 88:
            print(f"        {line}")
            line = entry
        else:
            line += entry
    if line:
        print(f"        {line}")
    print("    )),")
    print(")")


if __name__ == "__main__":
    # $ python scripts/make_ri_table.py > ucs_detect/table_ri.py
    main()
