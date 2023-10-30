ucs-detect
==========

Without any arguments,

    $ ucs-detect

The tool, ``ucs-detect``, tests the Unicode support level of the terminal
emulator for Wide character, Emoji sequence, and Language support and displays a
brief summary of the results.  Add --save-yaml argument to store a detailed
report.

.. figure:: https://dxtz6bzwq9sxx.cloudfront.net/ucs-detect.gif
   :alt: video demonstration of executing ucs-detect

Versions prior to 1.0 served only a single purpose, to export an
sh_-compatible line for export of ``UNICODE_VERSION``, to continue
this purpose, use ``--shell --quick``, for example:

    $ ucs-detect --shell --quick
    UNICODE_VERSION=15.0.0; export UNICODE_VERSION


Installation & Usage
--------------------

To install:

::

   $ pip install -U ucs-detect


UNICODE_VERSION
---------------

The environment variable, ``UNICODE_VERSION`` is used by the python wcwidth_
library, which contains every past unicode table version, to determine how
dependent python programs, such as IPython_ render wide and zero-width
characters.

Create sh_-compatible line for export::

    $ ucs-detect --shell --quick
    UNICODE_VERSION=15.0.0; export UNICODE_VERSION

    $ eval "$(ucs-detect --quick --shell)"
    $ echo $UNICODE_VERSION
    15.0.0

Problem
-------

Chinese, Japanese, Korean, and Emoticon characters are "double-wide", occupying
2 cells, instead of 1, and some other special characters are "zero-width", which
do not occopy any cells at all, or modify the previous cell as a "combining"
character.

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

History
=======

``1.0.3``, *2023-10-28*: More advanced tests, **drop python 2 support**, change
    default behavior when called without arguments. Use CLI arguments,
    ``ucs-detect --quick --shell`` to use the new release with matching previous
    release behavior.

``0.0.4``, *2020-06-20*: Initial releases and bugfixes

.. _IPython: https://ipython.org/
.. _python-prompt-toolkit: https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/PROJECTS.rst#projects-using-prompt_toolkit
.. _sh: https://en.wikipedia.org/wiki/Bourne_shell
.. _vercel/hyper: https://github.com/vercel/hyper
.. _wcwidth.c: https://www.cl.cam.ac.uk/~mgk25/ucs/wcwidth.c
.. _wcwidth: https://github.com/jquast/wcwidth
.. _`Query Cursor Position`: https://blessed.readthedocs.io/en/latest/location.html#finding-the-cursor
.. _`resize(1)`: https://github.com/joejulian/xterm/blob/master/resize.c
