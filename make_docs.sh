#!/bin/sh
set -o xtrace
rm -rf docs/_build/html
python make_results_rst.py \
    && sphinx-build -W -d docs/_build/doctrees -b html docs docs/_build/html

