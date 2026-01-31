ucs-detect
==========

::

    $ ucs-detect

``ucs-detect`` tests a terminal emulator's Unicode support for Wide characters,
Emoji Zero Width Joiner (ZWJ) sequences, Variation Selector-16 (VS-16) and
VS-15 sequences, and zero-width combining characters across 500+ languages.

.. figure:: https://dxtz6bzwq9sxx.cloudfront.net/ucs-detect.gif
   :alt: video demonstration of running ucs-detect

Installation & Usage
--------------------

To install or upgrade::

   $ pip install -U ucs-detect

Run a default test::

   $ ucs-detect

Run a detailed test and save a YAML report::

   $ ucs-detect --save-yaml=data/my-terminal.yaml --limit-codepoints=5000 --limit-words=5000 --limit-errors=500

CLI Options
-----------

``--save-yaml=<path>``
  Save results as YAML.

``--rerun <yaml-file>``
  Re-test a terminal using parameters from a previous YAML report.

``--test-only <category>``
  Test a single category: ``wide``, ``zwj``, ``vs16``, ``vs15``, ``lang``,
  ``unicode``, ``terminal``, or ``all`` (default).

``--limit-codepoints <n>``
  Limit total codepoints tested per category.

``--limit-codepoints-wide-pct <n>``
  Percentage of wide characters to test (default: 20). Set to ``0`` for a
  complete test.

``--limit-errors <n>``
  Stop testing a category after *n* errors.

``--stop-at-error <pattern>``
  Pause on errors matching *pattern* for interactive investigation.

``--set-software-name <name>`` / ``--set-software-version <version>``
  Set terminal name and version for YAML output (skips interactive prompt).

``--detect-all-dec-modes``
  Test all DEC Private Modes.

``--include-uncommon-codepoints``
  Include uncommon CJK extension blocks.

``--timeout-cps <seconds>``
  Timeout per codepoint test (default: 1.0).

``--timeout-query <seconds>``
  Timeout for cursor position query (default: 0.2).

``--cursor-report-delay-ms <ms>``
  Additional delay before reading cursor position report.

``--no-terminal-test`` / ``--no-languages-test``
  Skip terminal feature detection or language testing.

ucs-browser
-----------

``ucs-browser`` is an interactive terminal browser for visually inspecting
unicode character width rendering. It displays characters with pipe (``|``)
alignment markers that should align correctly in any terminal with proper
Unicode support.

::

   $ ucs-browser

Modes are toggled with keyboard shortcuts:

- ``1`` / ``2``: Narrow (1-cell) or Wide (2-cell) characters
- ``c``: Combining characters
- ``g``: Grapheme clusters (``[`` / ``]`` to adjust width)
- ``z``: Emoji ZWJ sequences
- ``5``: VS-15 (text style)
- ``7``: VS-16 (emoji style)
- ``U``: Toggle uncommon CJK extensions
- ``v``: Select Unicode version

Navigation follows less(1) conventions: ``j``/``k`` for lines, ``f``/``b`` for
pages, ``q`` to quit.

CLI options::

   $ ucs-browser --wide 2
   $ ucs-browser --combining
   $ ucs-browser --vs16
   $ ucs-browser --zwj
   $ ucs-browser --graphemes

Test Results
------------

Results for 20+ terminals on Windows, Linux, and Mac are published at
https://ucs-detect.readthedocs.io/results.html

Individual YAML reports are in the ``data`` folder:
https://github.com/jquast/ucs-detect/tree/master/data

Related articles:

- `ucs-detect test results`_ (November 2023, release 1.0.4)
- `State of Terminal Emulation 2025`_ (November 2025, release 1.0.8)

Results are shared with terminal emulator projects and may become outdated as
they improve Unicode support. Submit a pull request to update YAML data files.

Problem
-------

East Asian languages use Wide (W) or Fullwidth (F) characters that occupy 2
cells. Many scripts use zero-width combining characters that modify adjacent
characters. Emoji sequences use Zero Width Joiner and Variation Selector-16
characters.

Terminal applications must determine the display width of these characters, but
the Unicode Standard is updated periodically while libraries and applications
lag behind — or never update.

Support also varies within a terminal. For example, Microsoft's `Terminal.exe`_
supports Unicode 15.0 Wide characters (missing 27 from 13.0), has no Emoji ZWJ
support, fully supports VS-16, yet fails on zero-width characters for 88+
languages.

Solution
--------

``ucs-detect`` measures terminal compliance with the Specification_ of the
wcwidth_ library for the latest Unicode version across WIDE, ZERO, ZWJ, VS-16,
and VS-15 codepoint sequences.

How it works
------------

``ucs-detect`` uses the `Query Cursor Position`_ terminal sequence to ask
*"where is the cursor?"* after printing test characters. By comparing the
reported cursor position against the wcwidth_ expected width, compliance is
measured.

This technique is inspired by `resize(1)`_, which determines terminal
dimensions over transports like serial lines by moving to (999, 999) and
querying cursor position.

Updating Results
----------------

Re-test an existing terminal::

    $ ucs-detect --rerun data/contour.yaml

This re-executes with the same parameters, overwriting the existing YAML file.

Submit results for a new terminal::

    $ ucs-detect --save-yaml=data/jeffs-own-terminal.yaml --limit-errors=1000

For slow terminals (e.g. libvte_, which may require 5+ hours), reduce the wide
character test size::

    $ ucs-detect --save-yaml=data/jeffs-own-terminal.yaml --limit-errors=1000 --limit-codepoints-wide-pct 2

The default ``--limit-codepoints-wide-pct`` is 20. Set to ``0`` for a complete
test of all wide characters.

Create a draft pull request with your changes. A readthedocs.org build status
will appear — click "Details" for an HTML preview.

Problem Analysis
----------------

Use ``--stop-at-error`` to investigate discrepancies interactively::

    $ ucs-detect --stop-at-error 'Hindi'

Example output::

    ucs-detect: testing language support: Hindi
    मानव

    Failure in language 'Hindi':
    +----------------------------+
    |            मानव             |
    +----------------------------+

    measured by terminal: 4
    measured by wcwidth:  3

    printf '\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xa8\xe0\xa4\xb5\n'
    from blessed import Terminal
    term = Terminal()
    y1, x1 = term.get_location(); print('मानव', end='', flush=True); y2, x2 = term.get_location()
    assert x2 - x1 == 3

UDHR Data
---------

Language testing uses the `Universal Declaration of Human Rights`_ (UDHR)
dataset, translated into 500+ languages, as a test corpus for zero-width
characters (Mn — Nonspacing Mark), combining characters (Mc — Spacing Mark),
and language-specific scripts.

Source data: https://github.com/eric-muller/udhr/

The UDHR provides practical coverage of complex grapheme clusters across the
world's languages, serving as an indicator of a terminal's support for combining
marks across diverse scripts.

History
-------

- 1.1.0 (2026-01-29): Test *only* the latest Unicode Version (17.0 at this time).
  Added ``ucs-browser`` interactive terminal browser for inspecting unicode
  character width. Replaced bundled UDHR text files with pre-computed language
  grapheme table for faster and more reliable language testing. Added
  prettytable_ for formatted output. Added ``--set-software-name``,
  ``--set-software-version``, ``--test-only``, ``--detect-all-dec-modes``,
  ``--cursor-report-delay-ms``, ``--timeout-cps``, ``--timeout-query``,
  ``--include-uncommon-codepoints``, and ``--limit-codepoints-wide-pct`` CLI
  options. Removed ``--unicode-version``, ``--shell``, ``--quick``, and
  ``--no-emit-osc1337``.

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
.. _`Query Cursor Position`: https://blessed.readthedocs.io/en/latest/location.html#finding-the-cursor
.. _`resize(1)`: https://github.com/joejulian/xterm/blob/master/resize.c
.. _Specification: https://wcwidth.readthedocs.io/en/latest/specs.html
.. _`Terminal.exe`: https://ucs-detect.readthedocs.io/sw_results/Terminalexe.html#terminalexe
.. _`ucs-detect test results`: https://www.jeffquast.com/post/ucs-detect-test-results/
.. _`State of Terminal Emulation 2025`: https://www.jeffquast.com/post/state-of-terminal-emulation-2025/
.. _`Universal Declaration of Human Rights`: https://en.wikipedia.org/wiki/Universal_Declaration_of_Human_Rights
.. _libvte: https://wiki.gnome.org/Projects/VTE
.. _prettytable: https://github.com/jazzband/prettytable
