ucs-detect
==========

This package provides two command-line tools for testing and inspecting Unicode
support in terminal emulators.

Installation
------------

To install or upgrade::

   $ pip install -U ucs-detect

Problem
-------

Unicode contains East Asian languages which use Wide (W) or Fullwidth (F) characters that occupy 2
cells. Many languages use zero-width or "combining" characters that modify adjacent characters with
complex advancing rules.  Emoji sequences also use Zero Width Joiners to join multiple emojis, or
with adjusting Fitzpatrick variations, and emoji flags are represented by regional indicators of a
country code.  They may be also displayed without combined emoji and have a "standalone"
representation.

Terminal applications must determine the displayed width of these characters, but the Unicode
Standards are non-specific about terminals leaving much for interpretation.  Even well-meaning
terminals who report to support "Grapheme Support" by DEC Private Mode 2027 have varying
interpretations of the Unicode Standards.

Many terminal emulators have stood behind without any grapheme or emoji support at all, conforming
to pre-emoji era POSIX standard definitions of the wcwidth(3) system libraries.

Solution
--------

``ucs-detect`` measures terminal compliance with the Specification_ of the python wcwidth_ library,
for the latest Unicode versions across WIDE, ZERO, ZWJ, VS-16, and VS-15 unicode sequences and
grapheme width of over 500 languages.

``ucs-browser`` allows interactive browsing of each kind of category with an interactive terminal
browsing program. This may also output to a non-tty, and is used to publish the example test files
at https://github.com/jquast/ucs-detect/tree/master/docs/ucs_example_files

How it works
------------

``ucs-detect`` uses the `Query Cursor Position`_ terminal sequence to ask
*"where is the cursor?"* after printing test characters. By comparing the
reported cursor position against the wcwidth_ expected width, compliance is
measured.

This technique is inspired by `resize(1)`_, which determines terminal
dimensions over transports like serial lines by moving to (999, 999) and
querying cursor position.

ucs-detect
----------

.. figure:: https://dxtz6bzwq9sxx.cloudfront.net/ucs-detect2.gif
   :alt: video demonstration of running ucs-detect

``ucs-detect`` is the primary testing tool. It tests a terminal emulator's
Unicode support for Wide characters, Emoji Zero Width Joiner (ZWJ) sequences,
Regional Indicators and flags, Variation Selector-16 (VS-16) and VS-15 sequences,
and zero-width combining characters across hundreds of languages.

Terminal features that may be automatically detected are also reported:
`Bracketed Paste`_, `Synchronized Output`_, `Mouse SGR`_, `Grapheme
Clustering`_, `Kitty Keyboard protocol`_, `Sixel`_, `ReGIS`_, `Kitty`_ or
`iTerm2 image protocol`_, and `XTGETTCAP`_ support.

Run a default test::

   $ ucs-detect

Run a detailed test and save a YAML report::

   $ ucs-detect --save-yaml=data/my-terminal.yaml

Notable CLI options:

``--all``
  Test all codepoints and graphemes. By default, only codepoints and graphemes
  known to have failed in any terminal (contested) are tested.

``--rerun <yaml-file>``
  Re-test a terminal using parameters from a previous YAML report.

``--test-only <category>``
  Test a single category: ``wide``, ``zwj``, ``vs16``, ``vs15``, ``lang``,
  ``unicode``, ``terminal``, ``sri``, ``sfz``, ``ri``, or ``all`` (default).

``--limit-category-time <seconds>``
  Time budget per test category, auto-adjusts sampling (0=unlimited).

``--stop-at-error <pattern>``
  Pause on errors matching *pattern* for interactive investigation. Values:
  ``all``, ``zwj``, ``wide``, ``sri``, ``sfz``, ``ri``, ``vs16``, ``vs16n``, ``vs15``, ``lang``, or a
  specific language name (e.g., ``Hindi``).

``--probe-silently``
  Minimal output, modifying only a single line.

``--save-json <path>``
  Save results as a JSON report.

``--no-terminal-test``
  Skip terminal feature detection.

``--no-languages-test``
  Skip language support testing.

ucs-browser
-----------

.. figure:: https://dxtz6bzwq9sxx.cloudfront.net/ucs-browser.gif
   :alt: video demonstration of running ucs-detect

``ucs-browser`` is an interactive terminal browser for visually inspecting
unicode character width rendering. It displays characters with pipe (``|``)
alignment markers that should align correctly in any terminal with proper
Unicode support.

::

   $ ucs-browser

Modes are toggled with keyboard shortcuts:

- ``0``: Reset to default (wide characters)
- ``1`` / ``2``: Narrow (1-cell) or Wide (2-cell) characters
- ``c``: Combining characters
- ``g``: Grapheme clusters (``[`` / ``]`` to adjust width)
- ``z``: Emoji ZWJ sequences
- ``5``: VS-15 (text style)
- ``6``: VS-16 space kludge
- ``7``: VS-16 (emoji style)
- ``w``: Toggle with/without variation selector
- ``U``: Toggle uncommon CJK extensions
- ``t``: Toggle correction tables (wcstwidth vs wcswidth)
- ``v``: Select Unicode version
- ``-`` / ``+``: Adjust name column width

Modes may also be directly entered by CLI options (see ``ucs-browser --help``)

Navigation follows less(1) conventions: ``j``/``k`` for lines, ``f``/``b`` for
pages, ``q`` to quit.

Example files are created using ucs-browser, and are published in the source repository at url
https://github.com/jquast/ucs-detect/tree/master/docs/ucs_example_files

Use ``--no-correction`` when generating example files to disable terminal-specific
width correction tables, producing output that reflects wcwidth defaults. Example
file generation is handled by ``tox -e make_tables``.


Test Results
------------

Results for over 30 terminals on Linux, Mac, and Windows are published at
https://ucs-detect.readthedocs.io/results.html

Individual YAML reports are in the ``data`` folder:
https://github.com/jquast/ucs-detect/tree/master/data

Related articles:

- `ucs-detect test results`_ (November 2023, release 1.0.4)
- `State of Terminal Emulation 2025`_ (November 2025, release 1.0.8)
- `Perfecting Terminal Character Width Using Correction Tables` (June 2026, release https://www.jeffquast.com/post/perfecting-terminal-character-width-using-correction-tables/

Updating Results
----------------

Results are published in HTML and yaml, for use in code generation for publishing "correction
tables", and may become outdated as they improve Unicode support. Submit a pull request to update
YAML data files.

Re-test an existing terminal::

    $ ucs-detect --rerun data/contour.yaml

Submit results for a new terminal::

    $ ucs-detect --save-yaml=data/jeffs-own-terminal.yaml

Commit and make a PR. To preview documentation changes, create a *draft pull request*. A
readthedocs.org build status will appear -- click "Details" for an HTML preview.

Problem Analysis
----------------

Use ``--stop-at-error`` to investigate discrepancies interactively::

    $ ucs-detect --stop-at-error 'Hindi'

Example output::

    Failure in language 'Hindi' (Hindi-2-01):
    +---+-----------+--------+----------+---------+-------------------------+
    | # | Codepoint | Python | Category | wcwidth |           Name          |
    +---+-----------+--------+----------+---------+-------------------------+
    | 1 |   U+0915  | \u0915 |    Lo    |    1    |   DEVANAGARI LETTER KA  |
    | 2 |   U+094D  | \u094d |    Mn    |    0    |  DEVANAGARI SIGN VIRAMA |
    | 3 |   U+0928  | \u0928 |    Lo    |    1    |   DEVANAGARI LETTER NA  |
    | 4 |   U+093F  | \u093f |    Mc    |    0    | DEVANAGARI VOWEL SIGN I |
    +---+-----------+--------+----------+---------+-------------------------+
    +----+
    | क्नि |
    +----+

    measured by terminal: 3
    measured by wcwidth:  2

    Shell
    -----
    printf '\xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xa8\xe0\xa4\xbf\n'

    Python
    ------
    python -c "print('\u0915\u094d\u0928\u093f')"

    press return for next error, or n for non-stop:


Batch Testing
-------------

The general workflow to gather results and create documentation is, in combined serial and parallel order:

.. code-block:: bash

    tox -e docker_build,docker_verify,docker_run_series,docker_screenshots &
    tox -e system_verify,system_run_series,system_screenshots
    wait
    tox -e docs

For reproducible isolated runs, the project provides a Docker image with Xvfb and all linux terminal
emulators pre-installed.  All Docker operations are managed through ``tox`` targets:

.. code-block:: bash

    # one-time buildx builder setup
    tox -e docker_buildx_setup

    # build the image (with cache)
    tox -e docker_build

    # verify all terminals installed (group --version check)
    tox -e docker_verify

    # run ucs-detect on all terminals
    tox -e docker_run_series

    # this accepts extra 'run-series.py' arguments,
    tox -e docker_run_series -- --timeout 600 --run-only "foot,kitty"

    # generate screenshots
    tox -e docker_screenshots

Unfortunately, many terminals have to be excluded from docker:

- Not Linux or not X11 compatible
- GPU-accelerated and not compatible with Xvfb,
- massive number of build dependencies
- JS/Electron stuff (chromium?) for some reason.
- Cannot reliably set geometry
- Tests with ucs-detect fine, but cannot screenshot for any reason

This requires installing those terminals on the developer's host system.  Use the 'system' targets
to run these:

.. code-block:: bash

    # verify all terminals installed (group --version check)
    tox -e system_verify

    # run ucs-detect on all terminals
    tox -e system_run_series

    # generate screenshots
    tox -e system_screenshots

The script ``run-series.py`` is an X11 automation for testing all linux terminals. When ``-e program
[arguments]`` or similar is not supported, keystrokes are injected into the target application to
launch ``ucs-detect`` by configuration.

Updating ucs-detect
-------------------

ucs-detect contains auto-generated tables of codepoints and grapheme sequences derived from
Unicode.org, UDHR data, and python wcwidth code. Therefor, ucs-detect tables should be updated
anytime:

- new release or revisions of unicode.org data files
- new languages or revisions of UDHR data files
- python wcwidth that affects wcswidth measurement

To update these tables and then perform automatic reformatting, run::

    tox -e make_tables,format

UDHR Data
---------

Language testing uses the `Universal Declaration of Human Rights`_ (UDHR)
dataset, translated into 500+ languages, as a test corpus for zero-width
characters (Mn — Nonspacing Mark), combining characters (Mc — Spacing Mark),
and language-specific scripts.

Source data: https://github.com/eric-muller/udhr/

The UDHR provides practical coverage of common complex grapheme clusters across the
world's languages, serving as an indicator of a terminal's support for combining
marks across diverse scripts.

History
-------

- 2.3.2 (2026-06-10): Bugfix regression in VS15/16 reporting.

- 2.3.1 (2026-06-08): Remove erroneous ``Pillow`` dependency of pypi package.

- 2.3.0 (2026-06-08): Integrate with wcwidth>=0.8.1, which offers a new `wcstwidth()`_ function
  and some specification changes, and update ZWJ, grapheme, and contested tables.  As a circular
  dependency on our published results, wcwidth's new specification also artificially "caps" all
  graphemes to a maximum of width 2, matching more terminal emulators for width measurement
  (ghostty, wezterm, foot, mlterm). New NARROW width tracking detects narrow characters that display
  as wide.  Contested tables introduced: only codepoints known to fail in any terminal are tested,
  use ``--all`` to thoroughly test all codepoints.  ``ucs-browser`` has new ``t`` key to toggle
  correction tables and ``--no-correction`` mode.

- 2.2.1 (2026-06-01): Bugfix 'ENQ' response capture (PuTTY) and profiling Enrich source repository
  with more tools, like ``make-screenshots.py``, expanded XTGETTCAP detection and results table,
  record XTVERSION, TERM_PROGRAM directly. Record cpu and memory resource usage, and introduce
  ``run-series.py``, used with or without docker for batch testing with parallel execution (Linux
  only).

- 2.1.0 (2026-04-17): Add more testing for standalone and flags (RI), kitty text sizing
  protocol, make ucs-browser compatible with older python versions, and some changes
  to allow ucs-detect to integrate as a network service (see ``telnet modem.xyz``)

- 2.0.2 (2026-02-28): Some timing bugfixes caused features to sometimes report "No" support,
  and provide major speed enhancement to terminal test with integration of latest blessed
  release.

- 2.0.1 (2026-02-05): Add ``--probe-silently`` mode, ``--save-json``, time measurements with RTT and
  ping-like statistics, and telnetlib3 shell support for testing over telnet. Bugfix iTerm2 image
  feature detection.

- 2.0.0 (2026-02-01):  More correct results with up-to-date wcwidth_, loads of new CLI options like
  ``--rerun``, ``--limit-category-time`` and remove CLI arguments ``--unicode-version``,
  ``--shell``, ``--quick``, and ``--no-emit-osc1337``. The ``wcwidth-browser`` program has been
  migrated from wcwidth_, and setup.py was migrated to pyproject.toml. Requires Python 3.8.

- 1.0.8 (2025-11-02): Added detection of DEC Private Modes, testing
  of Variation Selector 15, Sixel graphics and pixel size, and
  automatic software version (XTVERSION and ^E answerback).

- 1.0.7 (2024-01-06): Add python 3.10 compatibility for yaml file save and
  update wcwidth requirement to 0.2.13.

- 1.0.6 (2023-12-15): Distribution fix for UDHR data and bugfix for python 3.8
  through 3.11. *ucs-detect* Welcomes `@GalaxySnail
  <https://github.com/GalaxySnail/>`_ as a new project contributor.

- 1.0.5 (2023-11-13): Set minimum wcwidth release version requirement.

- 1.0.4 (2023-11-13): Add support for Emoji with VS-16 and more complete testing.
  Published test results.

- 1.0.3 (2023-10-28): Drop python 2 support. Add more advanced testing. Changes
  default behavior when called without arguments, use ``ucs-detect --quick
  --shell`` to use the new release with matching previous release behavior.

- 0.0.4 (2020-06-20): Initial releases and bugfixes

.. _wcwidth: https://github.com/jquast/wcwidth
.. _`wcstwidth()`: https://wcwidth.readthedocs.io/en/latest/intro.html#wcstwidth
.. _`Query Cursor Position`: https://blessed.readthedocs.io/en/latest/location.html#finding-the-cursor
.. _`resize(1)`: https://github.com/joejulian/xterm/blob/master/resize.c
.. _Specification: https://wcwidth.readthedocs.io/en/latest/specs.html
.. _`Terminal.exe`: https://ucs-detect.readthedocs.io/sw_results/Terminalexe.html#terminalexe
.. _`ucs-detect test results`: https://www.jeffquast.com/post/ucs-detect-test-results/
.. _`State of Terminal Emulation 2025`: https://www.jeffquast.com/post/state-of-terminal-emulation-2025/
.. _`Universal Declaration of Human Rights`: https://en.wikipedia.org/wiki/Universal_Declaration_of_Human_Rights
.. _`Bracketed Paste`: https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-Bracketed-Paste-Mode
.. _`Synchronized Output`: https://github.com/contour-terminal/vt-extensions/blob/8a555bd24d8616c595e6c934a33555b62bd4dcd1/synchronized-output.md
.. _`Mouse SGR`: https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h3-Extended-coordinates
.. _`Grapheme Clustering`: https://github.com/contour-terminal/terminal-unicode-core
.. _`Kitty Keyboard protocol`: https://sw.kovidgoyal.net/kitty/keyboard-protocol/
.. _Sixel: https://en.wikipedia.org/wiki/Sixel
.. _ReGIS: https://en.wikipedia.org/wiki/ReGIS
.. _Kitty: https://sw.kovidgoyal.net/kitty/graphics-protocol/
.. _`iTerm2 image protocol`: https://iterm2.com/documentation-images.html
.. _XTGETTCAP: https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h3-Operating-System-Commands
.. _libvte: https://wiki.gnome.org/Projects/VTE
.. _prettytable: https://github.com/jazzband/prettytable
.. _Arch Linux: https://archlinux.org/
