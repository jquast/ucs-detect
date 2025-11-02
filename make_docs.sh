#!/bin/sh
set -o xtrace

# Only clean build directory if '-f' flag is supplied
if [ "$1" = "-f" ]; then
    rm -rf docs/_build/html
fi

python make_results_rst.py \
    && sphinx-build -W -d docs/_build/doctrees -b html docs docs/_build/html

