ucs-detect
==========

This CLI utility determines the Unicode Version of a terminal, and prints an
sh_-compatible variable for export::

    $ ucs-detect
    UNICODE_VERSION=12.0.0; export UNICODE_VERSION

This environment variable is then used by the python wcwidth_ library, to
determine how dependent python programs, such as IPython_ and others using
`python-prompt-toolkit`_ render zero-width and wide unicode characters.

If this variable is not exported, the python wcwidth_ library assumes the
latest.

Installation & Usage
--------------------

From an sh_-compatible shell:

::

   pip install -U ucs-detect
   eval "$(ucs-detect)"

To make this automatic, add this statement to your shell (bash) profile::

  if [ -z "$UNICODE_VERSION" ] && command -v ucs-detect >/dev/null; then
      eval "$(ucs-detect)"
  fi

Problem
-------

Chinese, Japanese, Korean, and Emoticon characters are "double-wide", occupying
2 cells, instead of 1, and some other special characters are "zero-width".

Any terminal application that formats and displays these characters may have
trouble determining how it will be displayed to the end-user.  Here is one such
example, from `vercel/hyper`_ terminal:

.. figure:: hyper-example.png
   :alt: An example of misaligned wide characters by the Hyper Terminal
   :figwidth: image

This problem happens often, because the Unicode Consortium releases new versions
of the Unicode Standard periodically, but the source code of libraries and
applications are not updated at the same time, or at all!

Many languages and libraries continue to conform only to Unicode 5.0, which is
the last version of `wcwidth.c`_ released by Markus Kuhn in 2007.

Solution
--------

The most important factor is to determine: **What version of unicode is the
Terminal using?**

This program, ``ucs-detect``, is able to **automatically detect** the version of
unicode that the connecting Terminal supports. The python wcwidth_ library
supports **all** Unicode versions, 4.1.0 through 12.1.0 at time of this writing,
and so it is able to select and match the correct width, by selecting for the
given value of the ``UNICODE_VERSION`` environment variable.

With this solution, we can correctly determine the ``UNICODE_VERSION`` of
`vercel/hyper`_ terminal as ``5.1.0``, and the cells that were previously
mis-aligned are now aligned correctly:

.. figure:: hyper-example-fixed.png
   :alt: An example of corrected alignment by Hyper Terminal
   :figwidth: image

How it works
------------

The unicode version is determined using the `Query Cursor Position`_ terminal
sequence, which asks, *"where is the cursor?"* using a special sequence, and
conforming terminals reply.

By displaying a series of Wide Unicode characters for each Unicode version
expected to advance the cursor by 2 cells, the very last version that
successfully advances 2 cells determines the version of Unicode supported by the
Terminal.

This solution of using `Query Cursor Position`_ and exporting an sh_ variable is
precisely the same solution used by the `resize(1)`_ program distributed with
X11, which determines the terminal size over transports that are not capable of
communicating or forwarding it (such as over a serial line).

Further
-------

I hope that this CLI tool is provisional!  I'd like to see all Terminals
automatically export the environment variable, ``UNICODE_VERSION`` and that this
tool would not be required.

If you would like to read more about this tool and the related problems I hope to
address with the ``UNICODE_VERSION`` environment variable, have a look at this
companion article, https://jeffquast.com/post/terminal_wcwidth_solution/

wcwidth support in Terminals
============================

Using this tool, I have collected a list of wide unicode support version levels
in various terminal emulators on Mac and Linux. This list is not kept
up-to-date, but only to serve as an empirical demonstration of the need for
version level selection (and detection).
.

.. list-table:: Wide Unicode Versions in Terminals
   :header-rows: 1

   * - OS
     - Application
     - Application Version
     - Unicode Version
   * - Debian Linux 10 (buster)
     - Gnome-terminal
     - 3.30.2
     - 11.0.0
   * - Debian Linux 10 (buster)
     - XTerm
     - 344
     - 11.0.0
   * - Debian Linux 10 (buster)
     - urxvt-unicode
     - 9.22
     - 11.0.0
   * - Debian Linux 10 (buster)
     - Konsole
     - 18.04.0
     - 13.0.0
   * - Debian Linux 10 (buster)
     - Guake
     - 3.4.0
     - 11.0.0
   * - Debian Linux 10 (buster)
     - yakuake
     - 3.0.5
     - 13.0.0
   * - Debian Linux 10 (buster)
     - Terminator
     - 1.91
     - 11.0.0
   * - Debian Linux 10 (buster)
     - Eterm
     - 0.9.6
     - 4.1.0
   * - Debian Linux 10 (buster)
     - xfce4-terminal
     - 0.8.7.4
     - 11.0.0
   * - Debian Linux 10 (buster)
     - pterm
     - 0.70
     - 9.0.0
   * - Debian Linux 10 (buster)
     - st
     - 0.8.2
     - 11.0.0
   * - Debian Linux 10 (buster)
     - LXTerminal
     - 0.3.2
     - 11.0.0
   * - Debian Linux 10 (buster)
     - sakura
     - 3.6.2
     - 11.0.0
   * - Debian Linux 10 (buster)
     - PuTTY
     - 0.70
     - 9.0.0
   * - Debian Linux 10 (buster)
     - Alacritty
     - 0.4.1
     - 12.1.0
   * - Debian Linux 10 (buster)
     - tilix
     - 1.8.9
     - 11.0.0
   * - Debian Linux 10 (buster)
     - termit
     - 3.0.0
     - 11.0.0
   * - Debian Linux 10 (buster)
     - Terminal.app (GNUStep)
     - 0.9.9
     - 4.1.0
   * - Debian Linux 10 (buster)
     - qterminal
     - 0.414.1
     - 12.0.0
   * - Debian Linux 10 (buster)
     - mlterm
     - 3.8.6
     - 10.0.0
   * - Debian Linux 10 (buster)
     - MATE Terminal
     - 1.20.2
     - 11.0.0
   * - Debian Linux 10 (buster)
     - lilyterm
     - 0.9.9.4
     - 11.0.0
   * - Debian Linux 10 (buster)
     - kitty
     - 0.13.3
     - 11.0.0
   * - OSX 10.15.5 ("Catalina")
     - Terminal.app
     - 2.10(433)
     - 12.1.0
   * - OSX 10.15.5 ("Catalina")
     - iTerm2
     - 3.3.9
     - 8.0.0 / 12.1.0
   * - OSX 10.15.5 ("Catalina")
     - XTerm
     - 326
     - 9.0.0
   * - OSX 10.15.5 ("Catalina")
     - alacritty
     - 0.4.2
     - 12.1.0
   * - OSX 10.15.5 ("Catalina")
     - hyper
     - 3.0.2
     - 5.1.0
   * - OSX 10.15.5 ("Catalina")
     - kitty
     - 0.18.1
     - 13.0.0
   * - OSX 10.15.5 ("Catalina")
     - ZOC Terminal
     - 87.25.8
     - 5.1.0
   * - OSX 10.15.5 ("Catalina")
     - Cathode.app
     - 2.4.1
     - 4.1.0
   * - OSX 10.15.5 ("Catalina")
     - Upterm
     - 0.4.4
     - 4.1.0

.. _IPython: https://ipython.org/
.. _python-prompt-toolkit: https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/PROJECTS.rst#projects-using-prompt_toolkit
.. _sh: https://en.wikipedia.org/wiki/Bourne_shell
.. _vercel/hyper: https://github.com/vercel/hyper
.. _wcwidth.c: https://www.cl.cam.ac.uk/~mgk25/ucs/wcwidth.c
.. _wcwidth: https://github.com/jquast/wcwidth
.. _`Query Cursor Position`: https://blessed.readthedocs.io/en/latest/location.html#finding-the-cursor
.. _`resize(1)`: https://github.com/joejulian/xterm/blob/master/resize.c
