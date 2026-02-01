"""
A terminal browser, similar to less(1) for testing printable width of unicode.

This displays the full range of unicode points for 1 or 2-character wide
ideograms, with pipes ('|') that should always align for any terminal that
supports utf-8.

Interactive Keys:
  Navigation:
    k, y, UP          Scroll backward 1 line
    j, e, ENTER, DOWN Scroll forward 1 line
    f, SPACE, PGDOWN  Scroll forward 1 page
    b, PGUP           Scroll backward 1 page
    F, SHIFT-DOWN     Scroll forward 10 pages
    B, SHIFT-UP       Scroll backward 10 pages
    HOME              Go to top
    G, END            Go to bottom
    Ctrl-L            Refresh screen

  Mode Switching:
    0                 Exit VS mode (return to normal mode)
    1                 Narrow width (normal) / Narrow base filter (VS mode)
    2                 Wide width (normal) / Wide base filter (VS mode)
    5                 Switch to VS-15 mode (text style)
    6                 Switch to VS-16 space kludge mode
    7                 Switch to VS-16 mode (emoji style)
    c                 Toggle combining character mode
    g                 Toggle grapheme cluster mode
    z                 Toggle ZWJ emoji mode
    U                 Toggle uncommon CJK extensions
    w                 Toggle with/without variation selector (VS mode only)
    [                 Decrease grapheme width (grapheme mode only)
    ]                 Increase grapheme width (grapheme mode only)

  Display Adjustment:
    -, _              Decrease character name display length by 2
    +, =              Increase character name display length by 2
    v                 Select Unicode version

  Exit:
    q, Q              Quit browser

Note:
  Only one of --combining, --vs15, --vs16, --vs16-space-kludge, --graphemes,
  or --zwj can be used at a time.
  The --without-vs option only applies when using --vs15 or --vs16.

  In VS mode, the display shows:
    - W/VS: Characters displayed with variation selector
    - WO/VS: Base characters displayed without variation selector
"""
# pylint: disable=C0103,W0622
#         Invalid constant name "echo"
#         Invalid constant name "flushout" (col 4)

# std imports
import os
import sys
import signal
import string
import argparse
import functools
import unicodedata

# 3rd party
import blessed
import requests
import urllib3.util

# local
from wcwidth import ZERO_WIDTH, wcwidth, list_versions, _wcmatch_version
from ucs_detect.measure import _is_uncommon
from ucs_detect.table_lang import LANG_GRAPHEMES
from ucs_detect.table_zwj import EMOJI_ZWJ_SEQUENCES

#: print function alias, does not end with line terminator.
echo = functools.partial(print, end='')
flushout = functools.partial(print, end='', flush=True)

#: printable length of highest unicode character description
LIMIT_UCS = 0x3fffd
UCS_PRINTLEN = len(f'{LIMIT_UCS:0x}')

#: URL for emoji variation sequences data file.
URL_EMOJI_VARIATION = (
    'https://unicode.org/Public/latest/ucd/emoji/'
    'emoji-variation-sequences.txt'
)

#: Cache directory and filename for downloaded unicode data.
CACHE_DIR = os.path.join(
    os.environ.get('XDG_CACHE_HOME', os.path.expanduser('~/.cache')),
    'ucs-detect',
)
CACHE_EMOJI_VS = os.path.join(CACHE_DIR, 'emoji-variation-sequences.txt')

#: HTTP fetch parameters matching wcwidth/bin/update-tables.py pattern.
CONNECT_TIMEOUT = int(os.environ.get('CONNECT_TIMEOUT', '10'))
READ_TIMEOUT = int(os.environ.get('READ_TIMEOUT', '30'))
FETCH_BLOCKSIZE = int(os.environ.get('FETCH_BLOCKSIZE', '4096'))
MAX_RETRIES = int(os.environ.get('MAX_RETRIES', '10'))
BACKOFF_FACTOR = float(os.environ.get('BACKOFF_FACTOR', '1.0'))

#: Module-level flag, set True by --refresh-unicode CLI argument.
REFRESH_UNICODE = False


def get_http_session():
    """Create a requests session with retry configuration."""
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'ucs-browser/1.0 (https://github.com/jquast/ucs-detect)'
    })
    retries = urllib3.util.Retry(
        total=MAX_RETRIES,
        connect=MAX_RETRIES,
        read=MAX_RETRIES,
        backoff_factor=BACKOFF_FACTOR,
        backoff_jitter=BACKOFF_FACTOR,
    )
    adapter = requests.adapters.HTTPAdapter(max_retries=retries)
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    return session


def fetch_emoji_variation_sequences():
    """
    Fetch emoji-variation-sequences.txt, using cache when available.

    :returns: path to local cached file.
    :rtype: str
    """
    if os.path.exists(CACHE_EMOJI_VS) and not REFRESH_UNICODE:
        return CACHE_EMOJI_VS

    os.makedirs(CACHE_DIR, exist_ok=True)
    session = get_http_session()
    print(f"Fetching {URL_EMOJI_VARIATION}: ", end='', flush=True)
    resp = session.get(URL_EMOJI_VARIATION,
                       timeout=(CONNECT_TIMEOUT, READ_TIMEOUT))
    resp.raise_for_status()
    with open(CACHE_EMOJI_VS, 'wb') as fout:
        for chunk in resp.iter_content(FETCH_BLOCKSIZE):
            fout.write(chunk)
    print('ok')
    return CACHE_EMOJI_VS


def readline(term, width):
    """A rudimentary readline implementation."""
    text = ''
    while True:
        inp = term.inkey()
        if inp.code == term.KEY_ENTER:
            break
        if inp.code == term.KEY_ESCAPE:
            text = ''
            break
        if not inp.is_sequence and len(text) < width:
            text += inp
            echo(inp)
            flushout()
        elif inp.code in (term.KEY_BACKSPACE, term.KEY_DELETE):
            if text:
                text = text[:-1]
                echo('\b \b')
            flushout()
    return text


class WcWideCharacterGenerator:
    """Generator yields unicode characters of the given ``width``."""

    # pylint: disable=R0903
    #         Too few public methods (0/2)
    def __init__(self, width, unicode_version, include_uncommon=True):
        """
        Class constructor.

        :param width: generate characters of given width.
        :param str unicode_version: Unicode Version for render.
        :param bool include_uncommon: include uncommon CJK extensions.
        :type width: int
        """
        self.characters = (
            chr(idx) for idx in range(LIMIT_UCS)
            if wcwidth(chr(idx), unicode_version=unicode_version) == width
            and (include_uncommon or not _is_uncommon(idx)))

    def __iter__(self):
        """Special method called by iter()."""
        return self

    def __next__(self):
        """Special method called by next()."""
        while True:
            ucs = next(self.characters)
            try:
                name = string.capwords(unicodedata.name(ucs))
            except ValueError:
                continue
            return (ucs, name)


class WcCombinedCharacterGenerator:
    """Generator yields unicode characters with combining."""

    # pylint: disable=R0903
    #         Too few public methods (0/2)

    def __init__(self, width, unicode_version):
        """
        Class constructor.

        :param int width: generate characters of given width.
        :param str unicode_version: Unicode version.
        """
        self.characters = []
        letters_o = ('o' * width)
        for (begin, end) in ZERO_WIDTH[_wcmatch_version(unicode_version)]:
            for val in [_val for _val in
                        range(begin, end + 1)
                        if _val <= LIMIT_UCS]:
                self.characters.append(
                    letters_o[:1] +
                    chr(val) +
                    letters_o[wcwidth(chr(val)) + 1:])
        self.characters.reverse()

    def __iter__(self):
        """Special method called by iter()."""
        return self

    def __next__(self):
        """
        Special method called by next().

        :return: unicode character and name, as tuple.
        :rtype: tuple[unicode, unicode]
        :raises StopIteration: no more characters
        """
        while True:
            if not self.characters:
                raise StopIteration
            ucs = self.characters.pop()
            try:
                name = string.capwords(unicodedata.name(ucs[1]))
            except ValueError:
                continue
            return (ucs, name)


class WcVariationSequenceGenerator:
    """Generator yields emoji variation sequences from emoji-variation-sequences.txt."""

    # pylint: disable=R0903
    #         Too few public methods (0/2)

    def __init__(self, base_width, unicode_version, variation_selector='VS15'):
        """
        Class constructor.

        :param int base_width: filter by base character width (1 or 2).
        :param str unicode_version: Unicode version.
        :param str variation_selector: 'VS15' or 'VS16'.
        """
        self.sequences = []

        # Determine which variation selector we're looking for
        vs_hex = 'FE0E' if variation_selector == 'VS15' else 'FE0F'

        filepath = fetch_emoji_variation_sequences()

        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                # Skip comments and empty lines
                if line.startswith('#') or not line.strip():
                    continue

                # Only process lines with our target variation selector
                if vs_hex not in line:
                    continue

                # Parse line format: "0023 FE0E  ; text style;  # (1.1) NUMBER SIGN"
                parts = line.split(';')
                if len(parts) < 2:
                    continue

                codepoints = parts[0].strip().split()
                if len(codepoints) < 2:
                    continue

                try:
                    base_cp = int(codepoints[0], 16)
                    vs_cp = int(codepoints[1], 16)
                except ValueError:
                    continue

                # Check base character width matches our filter
                if wcwidth(chr(base_cp),
                           unicode_version=unicode_version) != base_width:
                    continue

                # Extract name from comment
                comment_parts = line.split('#')
                if len(comment_parts) >= 2:
                    # Format: "# (1.1) NUMBER SIGN"
                    name_part = comment_parts[1].strip()
                    # Remove version info like "(1.1) "
                    if ')' in name_part:
                        name = name_part.split(')', 1)[1].strip()
                    else:
                        name = name_part
                    name = string.capwords(name)
                else:
                    name = "UNKNOWN"

                # Create the variation sequence
                sequence = chr(base_cp) + chr(vs_cp)
                self.sequences.append((sequence, name))

        self.sequences.reverse()

    def __iter__(self):
        """Special method called by iter()."""
        return self

    def __next__(self):
        """
        Special method called by next().

        :return: variation sequence and name, as tuple.
        :rtype: tuple[str, str]
        :raises StopIteration: no more sequences
        """
        if not self.sequences:
            raise StopIteration
        return self.sequences.pop()


class WcSpaceKludgeGenerator:
    """Generator yields VS-16 eligible base chars with trailing space instead of VS-16."""

    def __init__(self, base_width, unicode_version):
        """
        Class constructor.

        :param int base_width: filter by base character width (1 or 2).
        :param str unicode_version: Unicode version.
        """
        self.sequences = []
        filepath = fetch_emoji_variation_sequences()

        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                if 'FE0F' not in line:
                    continue
                parts = line.split(';')
                if len(parts) < 2:
                    continue
                codepoints = parts[0].strip().split()
                if len(codepoints) < 2:
                    continue
                try:
                    base_cp = int(codepoints[0], 16)
                except ValueError:
                    continue
                if wcwidth(chr(base_cp),
                           unicode_version=unicode_version) != base_width:
                    continue
                comment_parts = line.split('#')
                if len(comment_parts) >= 2:
                    name_part = comment_parts[1].strip()
                    if ')' in name_part:
                        name = name_part.split(')', 1)[1].strip()
                    else:
                        name = name_part
                    name = string.capwords(name)
                else:
                    name = "UNKNOWN"
                self.sequences.append((chr(base_cp) + ' ', name))

        self.sequences.reverse()

    def __iter__(self):
        """Special method called by iter()."""
        return self

    def __next__(self):
        """Special method called by next()."""
        if not self.sequences:
            raise StopIteration
        return self.sequences.pop()


def _available_grapheme_widths():
    """Return sorted list of widths available in LANG_GRAPHEMES."""
    return sorted({w for w, _ in LANG_GRAPHEMES})


class WcGraphemeGenerator:
    """Generator yields unique graphemes from LANG_GRAPHEMES for a given width."""

    def __init__(self, width):
        """
        Class constructor.

        :param int width: grapheme display width to browse.
        """
        seen = set()
        self.graphemes = []
        for gw, lang_entries in LANG_GRAPHEMES:
            if gw != width:
                continue
            for lang, graphemes in lang_entries:
                for g in graphemes:
                    if g not in seen:
                        seen.add(g)
                        self.graphemes.append((g, lang))
        self._idx = 0

    def __iter__(self):
        """Special method called by iter()."""
        return self

    def __next__(self):
        """Special method called by next()."""
        if self._idx >= len(self.graphemes):
            raise StopIteration
        result = self.graphemes[self._idx]
        self._idx += 1
        return result


class WcZwjGenerator:
    """Generator yields ZWJ emoji sequences from EMOJI_ZWJ_SEQUENCES."""

    def __init__(self):
        """Class constructor."""
        self.sequences = []
        for _version, seqs in EMOJI_ZWJ_SEQUENCES:
            for seq in seqs:
                ucs = ''.join(chr(cp) for cp in seq)
                name = unicodedata.name(chr(seq[0]), f'U+{seq[0]:04X}')
                self.sequences.append((ucs, name))
        self._idx = 0

    def __iter__(self):
        """Special method called by iter()."""
        return self

    def __next__(self):
        """Special method called by next()."""
        if self._idx >= len(self.sequences):
            raise StopIteration
        result = self.sequences[self._idx]
        self._idx += 1
        return result


class Style:
    """Styling decorator class instance for terminal output."""

    # pylint: disable=R0903
    #         Too few public methods (0/2)
    @staticmethod
    def attr_major(text):
        """Non-stylized callable for "major" text, for non-ttys."""
        return text

    @staticmethod
    def attr_minor(text):
        """Non-stylized callable for "minor" text, for non-ttys."""
        return text

    delimiter = '│'
    continuation = ' …'
    header_hint = '─'
    header_fill = '═'
    name_len = 10
    alignment = 'right'

    def __init__(self, **kwargs):
        """
        Class constructor.

        Any given keyword arguments are assigned to the class attribute
        of the same name.
        """
        for key, val in kwargs.items():
            setattr(self, key, val)


class Screen:
    """Represents terminal style, data dimensions, and drawables."""

    intro_msg_fmt = ('Delimiters ({delim}) should align, '
                     'unicode version is {version}.')

    def __init__(self, term, style, wide=2):
        """Class constructor."""
        self.term = term
        self.style = style
        self.wide = wide

    @property
    def header(self):
        """Text of joined segments producing full heading."""
        return self.head_item * self.num_columns

    @property
    def hint_width(self):
        """Width of a column segment."""
        return sum((len(self.style.delimiter),
                    self.wide,
                    len(self.style.delimiter),
                    len(' '),
                    UCS_PRINTLEN + 2,
                    len(' '),
                    self.style.name_len,))

    @property
    def head_item(self):
        """Text of a single column heading."""
        delimiter = self.style.attr_minor(self.style.delimiter)
        hint = self.style.header_hint * self.wide
        heading = f'{delimiter}{hint}{delimiter}'

        def alignment(*args):
            if self.style.alignment == 'right':
                return self.term.rjust(*args)
            return self.term.ljust(*args)

        txt = alignment(heading, self.hint_width, self.style.header_fill)
        return self.style.attr_major(txt)

    def msg_intro(self, version):
        """Introductory message disabled above heading."""
        return self.term.center(self.intro_msg_fmt.format(
            delim=self.style.attr_minor(self.style.delimiter),
            version=self.style.attr_minor(version))).rstrip()

    @property
    def row_ends(self):
        """Bottom of page."""
        return self.term.height - 1

    @property
    def num_columns(self):
        """Number of columns displayed."""
        if self.term.is_a_tty:
            return self.term.width // self.hint_width
        return 1

    @property
    def num_rows(self):
        """Number of rows displayed."""
        return self.row_ends - self.row_begins - 1

    @property
    def row_begins(self):
        """Top row displayed for content."""
        # pylint: disable=R0201
        # Method could be a function (col 4)
        return 2

    @property
    def page_size(self):
        """Number of unicode text displayed per page."""
        return self.num_rows * self.num_columns


class Pager:
    """A less(1)-like browser for browsing unicode characters."""
    # pylint: disable=too-many-instance-attributes

    #: screen state for next draw method(s).
    STATE_CLEAN, STATE_DIRTY, STATE_REFRESH = 0, 1, 2

    def __init__(self, term, screen, character_factory,
                 variation_selector=None, show_variation_selector=True,
                 include_uncommon=True):
        """
        Class constructor.

        :param term: blessed Terminal class instance.
        :type term: blessed.Terminal
        :param screen: Screen class instance.
        :type screen: Screen
        :param character_factory: Character factory generator.
        :type character_factory: callable returning iterable.
        :param variation_selector: Variation selector mode.
        :type variation_selector: str or None
        :param show_variation_selector: Whether to display variation selector.
        :type show_variation_selector: bool
        :param bool include_uncommon: include uncommon CJK extensions.
        """
        self.term = term
        self.screen = screen
        self.character_factory = character_factory
        self.variation_selector = variation_selector
        self.show_variation_selector = show_variation_selector
        self.include_uncommon = include_uncommon
        self.grapheme_mode = False
        self.grapheme_width = 1
        self.zwj_mode = False
        self.base_width_filter = screen.wide
        self.unicode_version = 'auto'
        self.dirty = self.STATE_REFRESH
        self.last_page = 0
        self._page_data = list()

    def on_resize(self, *args):
        """Signal handler callback for SIGWINCH."""
        # pylint: disable=W0613
        #         Unused argument 'args'
        assert self.term.width >= self.screen.hint_width, (
            f'Screen too small: {self.term.width}, '
            f'must be at least {self.screen.hint_width}')
        self._set_lastpage()
        self.dirty = self.STATE_REFRESH

    def _reinitialize(self):
        """Re-initialize page data and trigger a resize/redraw."""
        self.initialize_page_data()
        self.on_resize(None, None)

    def _set_lastpage(self):
        """Calculate value of class attribute ``last_page``."""
        self.last_page = (
            (len(self._page_data) - 1) // self.screen.page_size
        )

    def display_initialize(self):
        """Display 'please wait' message, and narrow build warning."""
        echo(self.term.home + self.term.clear)
        echo(self.term.move_y(self.term.height // 2))
        echo(self.term.center('Initializing page data ...').rstrip())
        flushout()

    def initialize_page_data(self):
        """Initialize the page data for the given screen."""
        # pylint: disable=attribute-defined-outside-init
        if self.term.is_a_tty:
            self.display_initialize()

        if self.zwj_mode:
            self.character_generator = WcZwjGenerator()
        elif self.grapheme_mode:
            self.character_generator = WcGraphemeGenerator(self.grapheme_width)
        elif self.variation_selector == 'SPACE_KLUDGE':
            self.character_generator = WcSpaceKludgeGenerator(
                self.base_width_filter, self.unicode_version)
        elif self.variation_selector:
            self.character_generator = WcVariationSequenceGenerator(
                self.base_width_filter, self.unicode_version,
                self.variation_selector)
        elif self.character_factory == WcWideCharacterGenerator:
            self.character_generator = self.character_factory(
                self.screen.wide, self.unicode_version,
                include_uncommon=self.include_uncommon)
        else:
            self.character_generator = self.character_factory(
                self.screen.wide, self.unicode_version)

        self._page_data = list()
        while True:
            try:
                self._page_data.append(next(self.character_generator))
            except StopIteration:
                break
        self._set_lastpage()

    def page_data(self, idx, offset):
        """
        Return character data for page of given index and offset.

        :param int idx: page index.
        :param int offset: scrolling region offset of current page.
        :returns: list of tuples in form of ``(ucs, name)``
        :rtype: list[(unicode, unicode)]
        """
        size = self.screen.page_size

        while offset < 0 and idx:
            offset += size
            idx -= 1
        offset = max(0, offset)

        while offset >= size:
            offset -= size
            idx += 1

        if idx == self.last_page:
            offset = 0
        idx = min(max(0, idx), self.last_page)

        start = (idx * self.screen.page_size) + offset
        end = start + self.screen.page_size
        return (idx, offset), self._page_data[start:end]

    def _run_notty(self, writer):
        """Pager run method for terminals that are not a tty."""
        page_idx = page_offset = 0
        while True:
            npage_idx, _ = self.draw(writer, page_idx + 1, page_offset)
            if npage_idx == self.last_page:
                break
            page_idx = npage_idx
            self.dirty = self.STATE_DIRTY

    def _run_tty(self, writer, reader):
        """Pager run method for terminals that are a tty."""
        signal.signal(signal.SIGWINCH, self.on_resize)

        page_idx = page_offset = 0
        while True:
            if self.dirty:
                page_idx, page_offset = self.draw(writer,
                                                  page_idx,
                                                  page_offset)
                self.dirty = self.STATE_CLEAN
            inp = reader(timeout=0.25)
            if inp is not None:
                nxt, noff = self.process_keystroke(inp,
                                                   page_idx,
                                                   page_offset)
                if self.dirty:
                    continue
            if not self.dirty:
                self.dirty = nxt != page_idx or noff != page_offset
            page_idx, page_offset = nxt, noff
            if page_idx == -1:
                return

    def run(self, writer, reader):
        """
        Pager entry point.

        :param callable writer: callable writes to output stream.
        :param callable reader: callable reads keystrokes from input stream.
        """
        self.initialize_page_data()
        if not self.term.is_a_tty:
            self._run_notty(writer)
        else:
            self._run_tty(writer, reader)

    def process_keystroke(self, inp, idx, offset):
        """
        Process keystroke ``inp``, adjusting screen parameters.

        :param inp: return value of blessed.Terminal.inkey().
        :type inp: blessed.keyboard.Keystroke
        :param int idx: page index.
        :param int offset: scrolling region offset of current page.
        :returns: tuple of next (idx, offset).
        :rtype: (int, int)
        """
        if inp.lower() in ('q', 'Q'):
            return (-1, -1)
        self._process_keystroke_commands(inp)
        idx, offset = self._process_keystroke_movement(inp, idx, offset)
        return idx, offset

    def _process_keystroke_commands(self, inp):
        """Process keystrokes that issue commands (side effects)."""
        if inp in ('1', '2', '5', '6', '7') and (self.grapheme_mode or self.zwj_mode):
            return
        elif inp in ('1', '2'):
            new_width = int(inp)
            if self.variation_selector:
                if self.base_width_filter != new_width:
                    self.base_width_filter = new_width
                    if not self.show_variation_selector:
                        self.screen.wide = new_width
                    self._reinitialize()
            else:
                if self.screen.wide != new_width:
                    self.screen.wide = new_width
                    self._reinitialize()
        elif inp == '0':
            if self.variation_selector or self.grapheme_mode or self.zwj_mode:
                self.variation_selector = None
                self.grapheme_mode = False
                self.zwj_mode = False
                self._reinitialize()
        elif inp == '5':
            if self.variation_selector != 'VS15':
                self.variation_selector = 'VS15'
                self.base_width_filter = 1
                if self.show_variation_selector:
                    self.screen.wide = 1
                else:
                    self.screen.wide = self.base_width_filter
                self._reinitialize()
        elif inp == '7':
            if self.variation_selector != 'VS16':
                self.variation_selector = 'VS16'
                self.base_width_filter = 1
                if self.show_variation_selector:
                    self.screen.wide = 2
                else:
                    self.screen.wide = self.base_width_filter
                self._reinitialize()
        elif inp == '6':
            if self.variation_selector != 'SPACE_KLUDGE':
                self.variation_selector = 'SPACE_KLUDGE'
                self.base_width_filter = 1
                self.screen.wide = 2
                self._reinitialize()
        elif inp == 'c':
            self.variation_selector = None
            self.character_factory = (
                WcWideCharacterGenerator
                if self.character_factory != WcWideCharacterGenerator
                else WcCombinedCharacterGenerator)
            self._reinitialize()
        elif inp == 'U':
            self.include_uncommon = not self.include_uncommon
            self._reinitialize()
        elif inp == 'g':
            self.grapheme_mode = not self.grapheme_mode
            if self.grapheme_mode:
                self.zwj_mode = False
                self.variation_selector = None
                self.screen.wide = self.grapheme_width
            else:
                self.screen.wide = self.base_width_filter
            self._reinitialize()
        elif inp == 'z':
            self.zwj_mode = not self.zwj_mode
            if self.zwj_mode:
                self.grapheme_mode = False
                self.variation_selector = None
                self.screen.wide = 2
            else:
                self.screen.wide = self.base_width_filter
            self._reinitialize()
        elif inp == ']' and self.grapheme_mode:
            widths = _available_grapheme_widths()
            idx = widths.index(self.grapheme_width) if self.grapheme_width in widths else 0
            if idx < len(widths) - 1:
                self.grapheme_width = widths[idx + 1]
                self.screen.wide = self.grapheme_width
                self._reinitialize()
        elif inp == '[' and self.grapheme_mode:
            widths = _available_grapheme_widths()
            idx = widths.index(self.grapheme_width) if self.grapheme_width in widths else 0
            if idx > 0:
                self.grapheme_width = widths[idx - 1]
                self.screen.wide = self.grapheme_width
                self._reinitialize()
        elif inp == 'w':
            if self.variation_selector:
                self.show_variation_selector = (
                    not self.show_variation_selector
                )
                if self.show_variation_selector:
                    self.screen.wide = (
                        1 if self.variation_selector == 'VS15' else 2
                    )
                else:
                    self.screen.wide = self.base_width_filter
                self.on_resize(None, None)
        elif inp in ('_', '-'):
            nlen = max(1, self.screen.style.name_len - 2)
            if nlen != self.screen.style.name_len:
                self.screen.style.name_len = nlen
                self.on_resize(None, None)
        elif inp in ('+', '='):
            nlen = min(self.term.width - 8,
                       self.screen.style.name_len + 2)
            if nlen != self.screen.style.name_len:
                self.screen.style.name_len = nlen
                self.on_resize(None, None)
        elif inp == 'v':
            with self.term.location(x=0, y=self.term.height - 2):
                print(self.term.clear_eos())
                input_selection_msg = (
                    "--> Enter unicode version [{versions}] ("
                    "current: {self.unicode_version}):".format(
                        versions=', '.join(list_versions()),
                        self=self))
                echo('\n'.join(self.term.wrap(
                    input_selection_msg,
                    subsequent_indent='    ')))
                echo(' ')
                flushout()
                inp = readline(
                    self.term,
                    width=max(map(len, list_versions())))
                if inp.strip() and inp != self.unicode_version:
                    self.unicode_version = _wcmatch_version(inp)
                    self.initialize_page_data()
                self.on_resize(None, None)

    def _process_keystroke_movement(self, inp, idx, offset):
        """Process keystrokes that adjust index and offset."""
        term = self.term
        if inp in ('y', 'k') or inp.code in (term.KEY_UP,):
            offset -= self.screen.num_columns
        elif inp in ('e', 'j') or inp.code in (term.KEY_ENTER,
                                               term.KEY_DOWN,):
            offset = offset + self.screen.num_columns
        elif inp in ('f', ' ') or inp.code in (term.KEY_PGDOWN,):
            idx += 1
        elif inp == 'b' or inp.code in (term.KEY_PGUP,):
            idx = max(0, idx - 1)
        elif inp == 'F' or inp.code in (term.KEY_SDOWN,):
            idx = max(0, idx + 10)
        elif inp == 'B' or inp.code in (term.KEY_SUP,):
            idx = max(0, idx - 10)
        elif inp.code == term.KEY_HOME:
            idx, offset = (0, 0)
        elif inp == 'G' or inp.code == term.KEY_END:
            idx, offset = (self.last_page, 0)
        elif inp == '\x0c':
            self.dirty = True
        return idx, offset

    def draw(self, writer, idx, offset):
        """
        Draw the current page view to ``writer``.

        :param callable writer: callable writes to output stream.
        :param int idx: current page index.
        :param int offset: scrolling region offset of current page.
        :returns: tuple of next (idx, offset).
        :rtype: (int, int)
        """
        while self.dirty:
            self.draw_heading(writer)
            self.dirty = self.STATE_CLEAN
            (idx, offset), data = self.page_data(idx, offset)
            for txt in self.page_view(data):
                writer(txt)
        self.draw_status(writer, idx)
        flushout()
        return idx, offset

    def draw_heading(self, writer):
        """
        Conditionally redraw screen when ``dirty`` attribute is REFRESH.

        :param callable writer: callable writes to output stream.
        :return: True if class attribute ``dirty`` is ``STATE_REFRESH``.
        :rtype: bool
        """
        if self.dirty == self.STATE_REFRESH:
            writer(''.join(
                (self.term.home, self.term.clear,
                 self.screen.msg_intro(version=self.unicode_version),
                 '\n', self.screen.header, '\n',)))
            return True
        return False

    def mode_label(self):
        """
        Return a label describing the current browsing mode.

        :return: Mode label string.
        :rtype: str
        """
        if self.zwj_mode:
            label = "ZWJ"
        elif self.grapheme_mode:
            label = f"GRAPHEME w={self.grapheme_width}"
        elif self.variation_selector == 'SPACE_KLUDGE':
            label = "VS16-SPACE-KLUDGE"
        elif self.variation_selector:
            width_label = ("NARROW" if self.base_width_filter == 1
                           else "WIDE")
            vs_display = ("W/VS" if self.show_variation_selector
                          else "WO/VS")
            label = f"{width_label}+{self.variation_selector}+{vs_display}"
        elif self.character_factory == WcCombinedCharacterGenerator:
            label = "COMBINING"
        else:
            label = "NARROW" if self.screen.wide == 1 else "WIDE"
        if self.include_uncommon:
            label += "+ALL"
        return label

    def draw_status(self, writer, idx):
        """
        Conditionally draw status bar when output terminal is a tty.

        :param callable writer: callable writes to output stream.
        :param int idx: current page position index.
        """
        if self.term.is_a_tty:
            writer(self.term.hide_cursor())
            style = self.screen.style
            writer(self.term.move(self.term.height - 1))
            if idx == self.last_page:
                last_end = '(END)'
            else:
                last_end = f'/{self.last_page}'

            mode = self.mode_label()

            txt = ('Page {idx}{last_end} - [{mode}] - '
                   '{q} to quit, [keys: {keyset}]'
                   .format(idx=style.attr_minor(f'{idx}'),
                           last_end=style.attr_major(last_end),
                           mode=style.attr_major(mode),
                           keyset=style.attr_major('kjfbvc012567gzwU[]-='),
                           q=style.attr_minor('q')))
            writer(self.term.center(txt).rstrip())

    def page_view(self, data):
        """
        Generator yields text for the current unicode pageview.

        :param list[(unicode, unicode)] data: current page data as
            tuple of ``(ucs, name)``.
        :returns: generator for full-page text for display
        """
        if self.term.is_a_tty:
            yield self.term.move(self.screen.row_begins, 0)
        clear_eol = self.term.clear_eol
        clear_eos = self.term.clear_eos

        col = 0
        for ucs, name in data:
            val = self.text_entry(ucs, name)
            col += 1
            if col == self.screen.num_columns:
                col = 0
                if self.term.is_a_tty:
                    val = ''.join((val, clear_eol, '\n'))
                else:
                    val = ''.join((val.rstrip(), '\n'))
            yield val

        if self.term.is_a_tty:
            yield ''.join((clear_eol, '\n', clear_eos))

    def text_entry(self, ucs, name):
        """
        Display a single column segment row describing ``(ucs, name)``.

        :param str ucs: target unicode point character string.
        :param str name: name of unicode point.
        :return: formatted text for display.
        :rtype: unicode
        """
        style = self.screen.style
        delimiter = style.attr_minor(style.delimiter)
        multi_cp = (self.zwj_mode or self.grapheme_mode
                     or (len(ucs) > 1 and self.variation_selector))

        if multi_cp:
            disp_ucs = style.attr_major(ucs)
            hex_label = '+'.join(f'{ord(c):04X}' for c in ucs)
            total_len = UCS_PRINTLEN + 2 + 1 + style.name_len
            if len(hex_label) > total_len:
                hex_label = hex_label[:total_len - 1] + '…'
            hex_label = f'{hex_label:<{total_len}s}'
            if style.alignment == 'right':
                return f'{hex_label} {delimiter}{disp_ucs}{delimiter}'
            return f'{delimiter}{disp_ucs}{delimiter} {hex_label}'

        if len(name) > style.name_len:
            idx = max(0, style.name_len - len(style.continuation))
            name = ''.join((name[:idx],
                            style.continuation if idx else ''))
        if style.alignment == 'right':
            fmt = ' '.join(('0x{val:0>{ucs_printlen}x}',
                            '{name:<{name_len}s}',
                            '{delimiter}{ucs}{delimiter}'
                            ))
        else:
            fmt = ' '.join(('{delimiter}{ucs}{delimiter}',
                            '0x{val:0>{ucs_printlen}x}',
                            '{name:<{name_len}s}'))
        val = ord(ucs)
        disp_ucs = style.attr_major(ucs)

        return fmt.format(name_len=style.name_len,
                          ucs_printlen=UCS_PRINTLEN,
                          delimiter=delimiter,
                          name=name,
                          ucs=disp_ucs,
                          val=val)


def validate_args(opts):
    """Validate result of parse_args() and return keyword arguments."""
    if opts['--wide'] is None:
        opts['--wide'] = 2
    else:
        assert opts['--wide'] in ("1", "2"), opts['--wide']
    if opts['--alignment'] is None:
        opts['--alignment'] = 'left'
    else:
        assert opts['--alignment'] in ('left', 'right'), opts['--alignment']
    opts['--wide'] = int(opts['--wide'])

    exclusive_opts = [opts.get('--combining', False),
                      opts.get('--vs15', False),
                      opts.get('--vs16', False)]
    assert sum(bool(opt) for opt in exclusive_opts) <= 1, \
        "Only one of --combining, --vs15, or --vs16 can be used"

    opts['character_factory'] = WcWideCharacterGenerator
    opts['variation_selector'] = None
    opts['base_width_filter'] = opts['--wide']
    opts['display_width'] = opts['--wide']
    opts['show_variation_selector'] = not opts.get('--without-vs', False)

    if opts.get('--combining'):
        opts['character_factory'] = WcCombinedCharacterGenerator
    elif opts.get('--vs15'):
        opts['variation_selector'] = 'VS15'
        if opts['show_variation_selector']:
            opts['display_width'] = 1
        else:
            opts['display_width'] = opts['base_width_filter']
    elif opts.get('--vs16'):
        opts['variation_selector'] = 'VS16'
        if opts['show_variation_selector']:
            opts['display_width'] = 2
        else:
            opts['display_width'] = opts['base_width_filter']
    elif opts.get('--vs16-space-kludge'):
        opts['variation_selector'] = 'SPACE_KLUDGE'
        opts['base_width_filter'] = 1
        opts['display_width'] = 2
    elif opts.get('--graphemes'):
        opts['grapheme_mode'] = True
        opts['display_width'] = 1
    elif opts.get('--zwj'):
        opts['zwj_mode'] = True
        opts['display_width'] = 2

    return opts


def main_browser(opts):
    """Program entry point for interactive browser."""
    global REFRESH_UNICODE
    REFRESH_UNICODE = opts.get('--refresh-unicode', False)

    from ucs_detect.terminal import make_terminal
    term = make_terminal()
    style = Style()

    if term.number_of_colors:
        style = Style(attr_major=term.magenta,
                      attr_minor=term.bright_cyan,
                      alignment=opts['--alignment'])
    style.name_len = 10

    screen = Screen(term, style, wide=opts['display_width'])
    pager = Pager(term, screen, opts['character_factory'],
                  variation_selector=opts['variation_selector'],
                  show_variation_selector=opts['show_variation_selector'],
                  include_uncommon=opts.get('--include-uncommon', False))

    if opts['variation_selector']:
        pager.base_width_filter = opts['base_width_filter']
    if opts.get('grapheme_mode'):
        pager.grapheme_mode = True
    if opts.get('zwj_mode'):
        pager.zwj_mode = True

    with term.location(), term.cbreak(), \
            term.fullscreen(), term.hidden_cursor():
        pager.run(writer=echo, reader=term.inkey)
    return 0


def parse_args():
    """Parse command-line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description='A terminal browser for testing printable '
                    'width of unicode.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Interactive Keys:
  Navigation:
    k, y, UP          Scroll backward 1 line
    j, e, ENTER, DOWN Scroll forward 1 line
    f, SPACE, PGDOWN  Scroll forward 1 page
    b, PGUP           Scroll backward 1 page
    F, SHIFT-DOWN     Scroll forward 10 pages
    B, SHIFT-UP       Scroll backward 10 pages
    HOME              Go to top
    G, END            Go to bottom
    Ctrl-L            Refresh screen

  Mode Switching:
    0                 Exit VS mode (return to normal mode)
    1                 Narrow width (normal) / Narrow base filter (VS mode)
    2                 Wide width (normal) / Wide base filter (VS mode)
    5                 Switch to VS-15 mode (text style)
    6                 Switch to VS-16 space kludge mode
    7                 Switch to VS-16 mode (emoji style)
    c                 Toggle combining character mode
    g                 Toggle grapheme cluster mode
    z                 Toggle ZWJ emoji mode
    U                 Toggle uncommon CJK extensions
    w                 Toggle with/without variation selector (VS mode only)
    [                 Decrease grapheme width (grapheme mode only)
    ]                 Increase grapheme width (grapheme mode only)

  Display Adjustment:
    -, _              Decrease character name display length by 2
    +, =              Increase character name display length by 2
    v                 Select Unicode version

  Exit:
    q, Q              Quit browser

Notes:
  Only one of --combining, --vs15, --vs16, --vs16-space-kludge, --graphemes,
  or --zwj can be used at a time.
  The --without-vs option only applies when using --vs15 or --vs16.

  In VS mode, the display shows:
    - W/VS: Characters displayed with variation selector
    - WO/VS: Base characters displayed without variation selector
""")

    parser.add_argument(
        '--wide', metavar='<n>', type=str, default=None,
        help='Browser 1 or 2 character-wide cells.')
    parser.add_argument(
        '--alignment', metavar='<str>', type=str, default='left',
        help='Choose left or right alignment. (default: left)')

    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        '--combining', action='store_true',
        help='Use combining character generator.')
    mode_group.add_argument(
        '--vs15', action='store_true',
        help='Browse emoji variation sequences with VS-15 (text style).')
    mode_group.add_argument(
        '--vs16', action='store_true',
        help='Browse emoji variation sequences with VS-16 (emoji style).')
    mode_group.add_argument(
        '--vs16-space-kludge', action='store_true',
        help='Browse VS-16 eligible chars with trailing space instead of VS-16.')
    mode_group.add_argument(
        '--graphemes', action='store_true',
        help='Browse language grapheme clusters (use [ and ] to change width).')
    mode_group.add_argument(
        '--zwj', action='store_true',
        help='Browse emoji ZWJ (Zero-Width Joiner) sequences.')

    parser.add_argument(
        '--without-vs', action='store_true',
        help='Display base characters without variation selector.')
    parser.add_argument(
        '--include-uncommon', action='store_true', default=False,
        help='Include uncommon CJK extensions (toggle with U key).')
    parser.add_argument(
        '--refresh-unicode', action='store_true',
        help='Force re-download of emoji-variation-sequences.txt '
             'from unicode.org.')

    args = parser.parse_args()

    return {
        '--wide': args.wide,
        '--alignment': args.alignment,
        '--combining': args.combining,
        '--vs15': args.vs15,
        '--vs16': args.vs16,
        '--vs16-space-kludge': args.vs16_space_kludge,
        '--graphemes': args.graphemes,
        '--zwj': args.zwj,
        '--without-vs': args.without_vs,
        '--include-uncommon': args.include_uncommon,
        '--refresh-unicode': args.refresh_unicode,
        '--help': False,
    }


def main():
    """CLI entry point."""
    sys.exit(main_browser(validate_args(parse_args())))
