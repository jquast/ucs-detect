Fonts
=====

The test terminals render every language and emoji cell with two fonts: GNU Unifont for text, and
Noto Color Emoji for cells whose presentation is emoji.  Unifont 18.0.01 covers Unicode 18.0 in
116,638 glyphs across two files, ``unifont`` for the basic multilingual plane and ``unifont_upper``
for planes 1 to 3, and it covers the base codepoint of all 8,644 contested graphemes.  Noto Color
Emoji joins all 1,614 RGI ZWJ sequences, colors the 213 VS16 bases and draws the 262 regional
indicator flags, none of which Unifont can join or color.

A terminal reaches Noto Color Emoji only if it selects a font by emoji presentation, or by an
explicit codepoint map.  An ordered fallback list does not help: Unifont has a glyph for every
contested codepoint, so a terminal that consults its font list only for missing glyphs stops at
Unifont and draws the monochrome shape.

Selection mechanisms
--------------------

.. list-table::
   :header-rows: 1

   * - Terminals
     - Mechanism
     - Configuration
   * - kitty, Ghostty, foot, WezTerm, Konsole, Contour, gnome-terminal, xfce4-terminal,
       lxterminal, terminator, weston-terminal
     - The terminal asks fontconfig for the generic ``emoji`` family when the cell is emoji
       presentation, and honours VS15 and VS16.
     - none beyond installing Noto Color Emoji
   * - kitty, Ghostty, Rio
     - An explicit codepoint map sends a range to a named family.
     - see below
   * - alacritty, st, xterm, rxvt-unicode, cool-retro-term, XTerm.NET
     - Multiple families, consulted only for codepoints the previous font lacks.
     - Unifont wins every cell, Noto Color Emoji is never reached

Emoji presentation terminals ask for the generic family, which fontconfig resolves through
``60-generic.conf`` on a stock system.  The generated ``system-fonts.conf`` in ``fonts/`` replaces
that file when ``FONTCONFIG_FILE`` is set, which ``run-series.py`` and ``make-screenshots.py`` both
do, so it carries its own ``emoji`` alias to Noto Color Emoji.

Explicit maps
-------------

kitty and Ghostty also select by presentation, so their map is needed only to override a specific
range.  Rio has no emoji presentation logic and needs the map.  ``terminal-config/rio/config.toml``
maps ``U+1F000`` to ``U+1FAFF`` and is loaded through ``RIO_CONFIG_HOME``.

Rio's map is by base codepoint, so the 94 astral VS15 bases inside the range render as emoji and
lose their text presentation.  Splitting them out needs one entry per base, because VS15 and VS16
bases interleave.  kitty and Ghostty need no map for that reason.

.. code-block:: toml

   [fonts]
   family = "Unifont"

   [[fonts.symbol-map]]
   start = "1F000"
   end = "1FAFF"
   font-family = "Noto Color Emoji"

Where color is impossible
-------------------------

st, xterm and rxvt-unicode draw through Xft, which has no colored bitmap or COLR path, so Noto
Color Emoji renders as nothing there even when it is selected.  Zutty discards codepoints above
``U+FFFF``, which excludes every astral emoji and Unifont Upper with them.  qterminal, mlterm,
Otty, Terminology and termy accept one family and fall back only on coverage, so they show the
Unifont shape.

Installing
----------

The Docker image installs ``noto-fonts-emoji`` from pacman, which puts ``NotoColorEmoji.ttf`` in
``/usr/share/fonts/noto``, and ``ucs_detect/fonts.py`` finds it there and adds its directory and the
``emoji`` alias to the fontconfig file.  On a host, install the distribution package
(``noto-fonts-emoji`` on Arch, ``fonts-noto-color-emoji`` on Debian and Ubuntu); no font needs to be
removed, because the ``emoji`` family is a distinct name rather than a substitution.
