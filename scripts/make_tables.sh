#!/bin/sh
# Regenerate all ucs_detect table modules from upstream Unicode data.
# Requires the ucs-detect package and dependencies installed.
# Usage: ./make_tables.sh
set -eu

cd "$(dirname "$0")/.."
PYTHON="${PYTHON:-python}"

echo "==> make_wide_table.py"
$PYTHON scripts/make_wide_table.py > ucs_detect/table_wide.tmp
mv ucs_detect/table_wide.tmp ucs_detect/table_wide.py

echo "==> make_ri_table.py"
$PYTHON scripts/make_ri_table.py > ucs_detect/table_ri.tmp
mv ucs_detect/table_ri.tmp ucs_detect/table_ri.py

echo "==> make_sfz_table.py"
$PYTHON scripts/make_sfz_table.py > ucs_detect/table_sfz.tmp
mv ucs_detect/table_sfz.tmp ucs_detect/table_sfz.py

echo "==> make_sri_table.py"
$PYTHON scripts/make_sri_table.py > ucs_detect/table_sri.tmp
mv ucs_detect/table_sri.tmp ucs_detect/table_sri.py

echo "==> make_table_zwj.py"
$PYTHON scripts/make_table_zwj.py > ucs_detect/table_zwj.tmp
mv ucs_detect/table_zwj.tmp ucs_detect/table_zwj.py

echo "==> make_vs15_table.py"
$PYTHON scripts/make_vs15_table.py > ucs_detect/table_vs15.tmp
mv ucs_detect/table_vs15.tmp ucs_detect/table_vs15.py

echo "==> make_vs16_table.py"
$PYTHON scripts/make_vs16_table.py > ucs_detect/table_vs16.tmp
mv ucs_detect/table_vs16.tmp ucs_detect/table_vs16.py

echo "==> make_lang_table.py"
$PYTHON scripts/make_lang_table.py > ucs_detect/table_lang.tmp
mv ucs_detect/table_lang.tmp ucs_detect/table_lang.py

echo "==> make_contested_tables.py"
$PYTHON scripts/make_contested_tables.py

echo "Done."
