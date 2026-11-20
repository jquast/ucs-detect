- TODO: copy blessed's cpr latency over, using the same screenshot process, and have it
  merge its results into the collected data, so we can write the data as a table and show
  its own screenshot of the colorful blessed cpr latency tool.
- crop detection: it should be possible by chosing emoji of vs-15, vs-16, and ZWJ
  that can be determined whether they were "cropped"
- similar to bug reported to 'extraterm', that it can be detected when "rendered width is not equal
  to cursor advance", which is different from cursor position report, there can be a kind of corruption,
  that is only seen in the early screenshot stage, where the "correction provided by wcstwidth" is
  *also* wrong.
  We should be able to re-use our cell spill code to determine when the correction is *also* wrong.
  if we encode this *extra* complication of difference, as another kind of spilling error, we might
  call a render spill error or something -- it mismatches the cursor position report, "this is 2
  cells" says the CPR response, but we display it, and it took up 4 cells, and the next grapheme
  painted into the 5th cell by actual paint -- their internal cursor position report is corrupted.
- rxvt has "leftover" for complex arabic/etc that "spills to the left", it
  also spills out over subsequent "draws ontop", they aren't ereased !
- iTerm2 font corruption on maldavian text
- xfce terminal corrupts/rewrites each character as it draws LTR, random strange
  characters from recent memory
- mintty has a lot of "font corruption", leftover visual displays when scrolling
- securecrt appears to draw some complex eastern language graphemes outside of window region (to
  left), and fails to undisplay them, they sort of "hang" there until a GUI operation (show drawer)
  causes them to refresh away
- at some point of a ucs-detect --all test, tabby corrupts existing fonts, english becomes chinese?!
- iTerm2 in some languages like Urdu and Yiddish, "bounce" or corrupt or alter previously written
  font glyphs as new ones are drawn ??
- Tecolot prints the tail of a long SGR chain as text: painting a cell with the ANSI, 256 color and
  truecolor forms of `48;2;48;0;64` leaves the literal characters `64m` in the first row, in the
  first painted cell after a control glyph, and the spillover control glyph reports 20 cells of ink
  to its right; every later cell on the page is drawn correctly, so the parser resynchronizes after
  echoing the fragment
- The spillover pages are painted twice now, the second pass overwriting any echoed fragment, and a
  terminal that reports truecolor receives one SGR form per cell instead of the ANSI, 256 color and
  truecolor chain
- iTerm2 counts 1676, 1786, and 1944 spilled of 8644 on three runs of the same page, even when the
  capture waits for two identical frames, so its renderer lands asynchronously and a single frame
  is never the same frame twice
- kitty takes the widest advance in U+0020..U+007F as its cell width, and GNU Unifont gives U+007F,
  a control character no page draws, a full-em glyph: every cell doubles, and ASCII carries 8px of
  trailing blank (16x16 instead of 8x16 at font_size=12).  Arguably a kitty bug, the maximum
  belongs over printable text or a representative advance.  terminals.yaml restores Unifont's
  half-em advance with `modify_font cell_width 50%`
- WezTerm defaults cell_width to 1em without consulting the font, doubling a half-em font the same
  way; `--config cell_width=0.5` restores it.  In the data, font_test_results.cell_width divided by
  cell_height above 0.75 finds the next terminal with this glitch, since Unifont's advance is half
  an em and undoubled terminals land near 0.5
- Unifont covers the base codepoint of every contested grapheme, so a terminal that consults its
  font list only for *missing* glyphs never reaches Noto Color Emoji: alacritty, st, xterm (two
  face names), rxvt-unicode (comma list), cool-retro-term (one fallback), XTerm.NET.  A fallback
  list is not a font stack that can prefer a font by presentation
- terminals that ask fontconfig for the generic `emoji` family render color emoji beside Unifont
  with no configuration: kitty, Ghostty, foot, WezTerm, Konsole (EmojiFont, defaults to Noto Color
  Emoji), Contour (bundled Noto Color Emoji), and the Pango/VTE group: gnome-terminal,
  xfce4-terminal, lxterminal, terminator, weston-terminal.  Pango sets family `emoji` with color
  required for VS16 and forbidden for VS15, so those five also get the selector right
- Rio selects one family and has no emoji presentation rules; `terminal-config/rio/config.toml`
  maps U+1F000-U+1FAFF to Noto Color Emoji through RIO_CONFIG_HOME.  The range also colors the 94
  astral VS15 bases inside it, which then lose text presentation.  kitty and Ghostty select by
  presentation and need no map; a coarse map there would cost the same 94 sequences
- Xft has no colored bitmap or COLR path, so st, xterm and rxvt-unicode cannot draw Noto Color
  Emoji at all, whether or not it is selected.  Zutty discards every codepoint above U+FFFF
  (`src/font.cc`), which excludes Noto Color Emoji, Unifont Upper and all astral emoji
- single family, coverage-only fallback, no emoji slot: qterminal, mlterm (aafont maps one family
  per charset), Otty (bundled fonts, no user selection), Terminology, termy, linux fbdev console.
  Electron and browser front ends (domterm, hyper, tabby, warp, xterm.js, extraterm) use a CSS
  stack, so Chromium picks Noto Color Emoji, but there is no per-range control
- terminator with Noto Emoji color or whatever causes them to render at like 20x their size,
  and then strangely cropped, they become "slivers" and other strange artifacts
