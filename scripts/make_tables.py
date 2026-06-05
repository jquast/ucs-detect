"""Regenerate all ucs_detect table modules from upstream Unicode data."""
import os
import subprocess
import sys


_HERE = os.path.dirname(os.path.abspath(__file__))
_PROJECT = os.path.dirname(_HERE)
_TABLE_DIR = os.path.join(_PROJECT, "ucs_detect")


def _atomic_write(target_path, content):
    tmp_path = target_path + ".tmp"
    with open(tmp_path, "wb") as f:
        f.write(content)
    os.replace(tmp_path, target_path)


def _run_script(script_name, output_filename=None):
    """Run *script_name* via subprocess, optionally capturing stdout to file."""
    script_path = os.path.join(_HERE, script_name)
    print(f"==> {script_name}")
    if output_filename is not None:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            check=True,
            cwd=_PROJECT,
        )
        _atomic_write(os.path.join(_TABLE_DIR, output_filename), result.stdout)
    else:
        subprocess.run(
            [sys.executable, script_path],
            check=True,
            cwd=_PROJECT,
        )


def main():
    """Run all table generation scripts with atomic output writes."""
    for script_name, output_filename in [
        ("make_wide_table.py", "table_wide.py"),
        ("make_ri_table.py", "table_ri.py"),
        ("make_sfz_table.py", "table_sfz.py"),
        ("make_sri_table.py", "table_sri.py"),
        ("make_table_zwj.py", "table_zwj.py"),
        ("make_vs15_table.py", "table_vs15.py"),
        ("make_vs16_table.py", "table_vs16.py"),
        ("make_lang_table.py", "table_lang.py"),
    ]:
        _run_script(script_name, output_filename)

    _run_script("make_contested_tables.py")
    print("Done.")


if __name__ == "__main__":
    main()
