ucs-detect
==========

Without any arguments,

::

    $ ucs-detect

``ucs-detect`` automatically tests the Unicode version and support level of a
terminal emulator for Wide character, Emoji Zero Width Joiner (ZWJ) sequences,
Emoji Variation Selector-16 (VS-16) sequences, and Zero-Width or combining
characters by supported Language.  A brief report is then printed to stdout.

.. figure:: https://dxtz6bzwq9sxx.cloudfront.net/ucs-detect.gif
   :alt: video demonstration of running ucs-detect

Installation & Usage
--------------------

To install or upgrade:

::

   $ pip install -U ucs-detect


To use::

   $ ucs-detect


To run a detailed test and store a yaml report to disk::

   $ ucs-detect --save-yaml=data/my-terminal.yaml --limit-codepoints=5000 --limit-words=5000 --limit-errors=500

Test Results
------------

More than twenty modern terminals for Windows, Linux, and Mac were tested,
their results have been collected into this repository and a detailed
summary is published at URL https://ucs-detect.readthedocs.io/results.html

An article describing the development of ucs-detect and summarizing the results
for the 1.0.4 release of ucs-detect (November 2023) is published at
https://www.jeffquast.com/post/ucs-detect-test-results/

Individual yaml data file reports for these terminals may also be inspected at
the repository folder ``data``,
https://github.com/jquast/ucs-detect/tree/master/data

Please note that results will be shared with Terminal Emulator projects and this
information may become out of date as they improve their support for Unicode.
Please do not expect the maintainers of ucs-detect to update these data files. If
you wish for this report to be corrected for any given Terminal, please feel free
to submit a pull request with an update to the yaml data files.

Problem
-------

Many East Asian languages contain Wide (W) or Fullwidth (F) characters, meaning
that each character occupies 2 cells instead of 1. Further, many languages
contain special combining characters that are "zero width", meaning they do not
occupy any cells, only modifying the previous one as a "combining" character.
Finally, there are "Zero Width Joiner" and "Variation Selector-16" characters
that are used in sequence for Emoji characters.

A terminal application that displays these characters may have trouble
determining how it will be displayed to the end-user.  This problem
happens often, because the Unicode Consortium releases new versions
of the Unicode Standard periodically, but the source code of libraries
and applications are not updated at the same time, or at all!

Finally, a terminal emulator may have varying levels of support. For example, at
time of this writing, Microsoft's `Terminal.exe`_ supports up to Unicode 15.0 for
Wide characters, is missing support for 27 characters of Unicode 13.0, has no
support for Emoji ZWJ, fully supports all VS-16 sequences, but fails to
correctly categorize many Zero-Width for 88 or more of the world's languages. 


Solution
--------

The most important factor is to determine whether the Terminal Emulator complies
with the Specification_ published by the python wcwidth_ library.

This program, ``ucs-detect``, is able to **automatically detect** the version
and feature level support of unicode that the connecting Terminal supports for
WIDE, ZERO, ZWJ, and VS-16 characters.

How it works
------------

The solution in this program is the use of the `Query Cursor Position`_ terminal
sequence, which asks, *"where is the cursor?"*. This is a hidden sequence that a
Terminal Emulator automatically responds to.

By use of this sequence, and the data tables of the wcwidth_ library,
we can test for compliance of the python wcwidth_ library Specification_.

The use of `Query Cursor Position`_  is inspired by the `resize(1)`_ program
distributed with X11, which determines the terminal size over transports that
are not capable of communicating by signal or forwarding by environment value,
such as over a serial line. `resize(1)` simply moves to (999, 999) then asks,
"where is my cursor?" and the response is understood to be the terminal size.

UNICODE_VERSION (legacy)
------------------------

.. note:: This feature is planned for deprecation, see https://github.com/jquast/wcwidth/issues/104

Versions of *ucs-detect* prior to 1.0 served only a single purpose, to export an
sh_-compatible line for export of ``UNICODE_VERSION``. To continue this purpose,
use ``--shell --quick``, for example::

    $ ucs-detect --shell --quick
    UNICODE_VERSION=15.0.0; export UNICODE_VERSION

It is designed to be used interactively::

    $ eval "$(ucs-detect --quick --shell)"
    $ echo $UNICODE_VERSION
    15.0.0

The environment variable, ``UNICODE_VERSION`` is currently used by the python
wcwidth_ library, which contains every past unicode table version, to determine
how dependent python programs, such as IPython_ render wide and zero-width
characters.

History
=======

- 1.0.7 (2024-01-06): Add python 3.10 compatibility for yaml file save and
  update wcwidth requirement to 0.2.13.

- 1.0.6 (2023-12-15): Distribution fix for UDHR data and bugfix for python 3.8
  through 3.11. *ucs-detect* Welcomes `@GalaxySnail
  <https://github.com/GalaxySnail/>`_ as a new project contributor.

- 1.0.5 (2023-11-13): Set minimum wcwidth_ release version requirement.

- 1.0.4 (2023-11-13): Add support for Emoji with VS-16 and more complete testing.
  Published test results.

- 1.0.3 (2023-10-28): Drop python 2 support. Add more advanced testing. Changes
  default behavior when called without arguments, use ``ucs-detect --quick
  --shell`` to use the new release with matching previous release behavior.

- 0.0.4 (2020-06-20): Initial releases and bugfixes

.. _IPython: https://ipython.org/
.. _python-prompt-toolkit: https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/PROJECTS.rst#projects-using-prompt_toolkit
.. _sh: https://en.wikipedia.org/wiki/Bourne_shell
.. _wcwidth: https://github.com/jquast/wcwidth
.. _`Query Cursor Position`: https://blessed.readthedocs.io/en/latest/location.html#finding-the-cursor
.. _`resize(1)`: https://github.com/joejulian/xterm/blob/master/resize.c
.. _Specification: https://wcwidth.readthedocs.io/en/latest/specs.html
.. _`Terminal.exe`: https://ucs-detect.readthedocs.io/sw_results/Terminalexe.html#terminalexe
