# pylint: disable=duplicate-code
"""Generate Emoji ZWJ sequence table data for ucs_detect."""
# This is a minified version of bin/update-tables.py from https://github.com/jquast/wcwidth/
import os
import re

import wcwidth

from ucs_detect.accessories import do_retrieve, get_data_dir

URL_EMOJI_ZWJ_SEQUENCES = "https://unicode.org/Public/emoji/{version}/emoji-zwj-sequences.txt"
PATH_DATA = str(get_data_dir())


def fetch_zwj_data():
    """Fetch all Emoji ZWJ sequences from the latest Unicode emoji spec."""
    fname = os.path.join(PATH_DATA, URL_EMOJI_ZWJ_SEQUENCES.rsplit("/", 1)[-1])
    filename, ext = os.path.splitext(fname)
    fname = filename + "-latest" + ext
    do_retrieve(url=URL_EMOJI_ZWJ_SEQUENCES.format(version="latest"), fname=fname)
    pattern = re.compile(r".*# E([0-9.]+)")
    all_sequences = []
    latest_version = "0"
    with open(fname, encoding="utf-8") as f:
        for line in f:
            if match := re.match(pattern, line):
                version = match.group(1)
                if wcwidth._wcversion_value(version) > wcwidth._wcversion_value(latest_version):
                    latest_version = version
                data, _, _ = line.partition("#")
                data_fields = (field.strip() for field in data.split(";"))
                code_points_str, *_ = data_fields
                if code_points_str:
                    all_sequences.append(
                        tuple(int(code_point, 16) for code_point in code_points_str.split())
                    )
    return latest_version, all_sequences


def main():
    """Generate and write the ZWJ unicode table module."""
    version, sequences = fetch_zwj_data()
    print("EMOJI_ZWJ_SEQUENCES = (")
    print(f"  ('{version}', (")
    # pack multiple sequences per line
    line = ""
    for seq in sequences:
        entry = repr(seq) + ", "
        if len(line) + len(entry) > 88:
            print(f"    {line}")
            line = entry
        else:
            line += entry
    if line:
        print(f"    {line}")
    print("  )),")
    print(")")


if __name__ == "__main__":
    # minimal emoji zwj parser, for use:
    # $ python scripts/make_table_zwj.py > ucs_detect/table_zwj.py
    main()
