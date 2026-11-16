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
