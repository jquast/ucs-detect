# This is a minified version of bin/update-tables.py from https://github.com/jquast/wcwidth/
import os
import re
import collections

# third party
import requests
import wcwidth

URL_EMOJI_ZWJ_SEQUENCES = 'https://unicode.org/Public/emoji/{version}/emoji-zwj-sequences.txt'
FETCH_BLOCKSIZE = 3096
PATH_UP = os.path.relpath(os.path.join(os.path.dirname(__file__), os.path.pardir))
PATH_DATA = os.path.join(PATH_UP, 'data')

def do_retrieve(url: str, fname: str) -> None:
    """Retrieve given url to target filepath fname."""
    folder = os.path.dirname(fname)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    if os.path.exists(fname):
        return
    resp = requests.get(url, stream=True)
    with open(fname, 'wb') as fout:
        for chunk in resp.iter_content(FETCH_BLOCKSIZE):
            fout.write(chunk)

def fetch_zwj_data():
    """Determine Unicode Versions with Emoji Zero Width Join character support."""
    # From Unicode® Technical Standard #51
    #
    # > Starting with Version 11.0 of this specification, the repertoire of
    # > emoji characters is synchronized with the Unicode Standard, and has the
    # > same version numbering system. For details, see Section 1.5.2, Versioning.
    #
    # http://www.unicode.org/reports/tr51/#Versioning
    # http://www.unicode.org/reports/tr51/#EmojiVersions
    fname = os.path.join(PATH_DATA, URL_EMOJI_ZWJ_SEQUENCES.rsplit('/', 1)[-1])
    filename, ext = os.path.splitext(fname)
    fname = filename + '-latest' + ext
    do_retrieve(url=URL_EMOJI_ZWJ_SEQUENCES.format(version='latest'), fname=fname)
    pattern = re.compile(r'.*# E([0-9.]+)')
    versions = set()
    result = collections.defaultdict(list)
    with open(fname, encoding='utf-8') as f:
        for line in f:
            if match := re.match(pattern, line):
                version = match.group(1)
                versions.add(version)
                data, _, _ = line.partition('#')
                data_fields = (field.strip() for field in data.split(';'))
                code_points_str, *_ = data_fields
                if code_points_str:
                    result[version].append(
                        tuple(int(code_point, 16)
                              for code_point in code_points_str.split()))

    sorted_versions = [int_str_version_pair[1] for int_str_version_pair in sorted(
        [(wcwidth._wcversion_value(_v_str), _v_str) for _v_str in versions],
        reverse=True)]
    return {vv_str: result[vv_str] for vv_str in sorted_versions}

def parse_zwj(fname: str, version: str):
    sequences = []
    with open(fname, encoding='utf-8') as fin:
        for line in fin:
            data, _, comment = line.partition('#')
            data_fields = (field.strip() for field in data.split(';'))
            code_points_str, *type_description = data_fields
            if code_points_str:
                sequences.append(tuple(int(code_point, 16)
                                for code_point in code_points_str.split()))
    return sequences


def main():
    # create basic python code, skipping all that jinja stuff
    print("EMOJI_ZWJ_SEQUENCES = (")
    for key, sequences in fetch_zwj_data().items():
        print(f"  ('{key}', (")
        for seq in sequences:
            print(f"    {seq},")
        print("    ),")
        print("  ),")
    print(")")


if __name__ == '__main__':
    # minimal emoji zwj parser, for use:
    # $ python make_zwj_table.py > ucs_detect/table_zwj.py
    main()