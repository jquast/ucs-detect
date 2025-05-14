import time
import functools
import sys

import blessed
import ucs_detect
import ucs_detect.table_wide


CSI_0_C = {
    '\x1b[?6c': {
        'software': ['PuTTy', 'st'],
        'sixel': False,
    },
    '\x1b[?1;2c': {
        'software': ['Apple Terminal', 'vimterm', 'xterm.js']
    },
    '\x1b[?62c': {
        'software': ['kitty'],
        'kitty_graphics': True,
    },
    '\x1b[?62;4c': {
        'software': ['iTerm2'],
        'sixel': True,
        'inline_images': True,
    },
    '\x1b[?65;1;9c': {
        'software': ['xfce', 'guake'],
        # hard to say, xfce does, guake does not!
        'sixel': False,
    },
    '\x1b[?65;4;6;18;22c': {
        'software': ['wezTerm'],
        'sixel': True,
        'inline_images': True,
        'kitty_graphics': True,
    },
    '\x1b[?63;1;2;3;4;7;29c': {
        'software': ['mlterm'],
        'sixel': True,
    },
    '\x1b[?63;1;2;4;6;9;15;22c': {
        'software': ['xterm'],
        'sixel': True,
    },
    '\x1b[?64;1;9;15;18;21;22c': {
        'software': ['terminology'],
        'sixel': False,
    },
    '\x1b[=67;84;101;114;109;1;312c':
    {
        'software': ['SyncTerm'],
        'sixel': True,
        'inline_images': False,
    },
    '\x1b[?64;1;2;4;6;9;15;21;22;28;29c': {
        'software': ['mintty'],
        'sixel': True,
    },
    '\x1b[?65;1;2;3;4;6;7;8;9;15;18;21;22;29;39;42;44c': {
        'software': ['rlogin'],
        'sixel': True,
    },
}

ALL_DEC_PRIVATE_MODES = {
    # sources ..
    # https://github.com/hackerb9/lsix/issues/41
    # https://terminalguide.namepad.de/mode/
    # https://chromium.googlesource.com/apps/libapps/+/master/hterm/doc/ControlSequences.md#decset
    # https://github.com/mintty/mintty/wiki/CtrlSeqs
    # https://codeberg.org/dnkl/foot/src/branch/master/csi.c
    # https://gist.github.com/christianparpart/d8a62cc1ab659194337d73e399004036
    1: 'Application Cursor Keys',
    2: 'Designate USASCII for character sets G0-G3, and set VT100 mode',
    3: '132 Column Mode',
    4: 'Smooth (Slow) Scroll',
    5: 'Reverse Video',
    6: 'Origin Mode',
    7: 'Wraparound Mode',
    8: 'Auto-repeat Keys',
    9: 'Send Mouse X & Y on button press',
    10: 'Show toolbar',
    12: 'Start blinking cursor',
    18: 'Print form feed',
    19: 'Set print extent to full screen',
    25: 'Show Cursor',
    30: 'Show scrollbar',
    35: 'Enable font-shifting functions',
    38: 'Enter Tektronix Mode',
    40: 'Allow 80 - 132 (DECCOLM) Mode',
    41: 'more(1) fix',
    42: 'Enable Nation Replacement Character sets',
    44: 'Turn On Margin Bell',
    45: 'Reverse-wraparound Mode',
    46: 'Start Logging',
    47: 'Use Alternate Screen Buffer',
    66: 'Application keypad',
    67: 'Backarrow key sends backspace',
    69: 'left and right margin (DECLRMM)',
    80: 'enable sixel scrolling',
    95: 'Do not Clear Screen on Mode ?3 Change (DECNCSM)',
    1000: 'Send Mouse X & Y on button press and release',
    1001: 'Use Hilite Mouse Tracking',
    1002: 'Use Cell Motion Mouse Tracking',
    1003: 'Use All Motion Mouse Tracking',
    1004: 'Send FocusIn/FocusOut events',
    1005: 'Enable Extended Mouse Mode (UTF-8)',
    1006: 'Enable Extended Mouse Mode (SGR)',
    1007: 'Enable Alternate Scroll Mode',
    1010: 'Scroll to bottom on tty output',
    1011: 'Scroll to bottom on key press',
    1015: 'Enable Extended Mouse Mode (urxvt)',
    1016: 'Mouse reporting by pixels (MOUSE_SGR_PIXELS)',
    1034: 'Interpret "meta" key, sets eighth bit',
    1035: 'Enable special modifiers for Alt and NumLock keys',
    1036: 'Send ESC when Meta modifies a key',
    1037: 'Send DEL from the editing-keypad Delete key',
    1039: 'Send ESC when Alt modifies a key',
    1040: 'Keep selection even if not highlighted',
    1041: 'Use the CLIPBOARD selection',
    1042: 'Enable Urgency window manager hint when Ctrl+G is received',
    1043: 'Enable raising of the window when Ctrl+G is received',
    1047: 'Use Alternate Screen Buffer',
    1048: 'Save cursor as in DECSC',
    1049: 'Combine 1047 and 1048 modes and clear',
    1050: 'Set terminfo/termcap function-key mode',
    1051: 'Set Sun function-key mode',
    1052: 'Set HP function-key mode',
    1053: 'Set SCO function-key mode',
    1060: 'Set legacy keyboard emulation (X11R6)',
    1061: 'Set VT220 keyboard emulation',
    1070: 'Sixel use private palette',
    2001: 'left button places cursor on command line',
    2002: 'middle button pastes at current mouse position',
    2003: 'double right-click deletes selection until mouse position',
    2004: 'Set bracketed paste mode',
    2026: 'Synchronized Output',
    2027: 'Grapheme Cluster Boundary support',
    2500: 'Bidirectional "Box mirroring"',
    2501: 'Bidirectional autodetection',
    7700: 'Ambiguous width reporting',
    7723: 'Bidirectional reflow',
    7766: 'Scrollbar hiding',
    7767: 'Font change reporting',
    7796: 'Bidirectional enabled current line',
    8452: 'Adjust cursor position after emitting sixel',
    77096: 'Bidirectional rendering',
}

SCREEN_RATIOS = [(4, 3), (16, 9), (16, 10), (21, 9), (32, 9)]
DEFAULT_FONT_WIDTH = 640 // 80
DEFAULT_FONT_HEIGHT = 400 // 25
def yesno_bool(string):
    return string.lower() in ('yes', 'true', '1')

KITTY_OPTIONS = {
    'name': ('kitty-query-name', str),
    'software_version': ('kitty-query-version', str),
    'font_family': ('kitty-query-font_family', str),
    'font_size': ('kitty-query-font_size', int),
    'bold_font': ('kitty-query-bold_font', str),
    'bold_italic_font': ('kitty-query-bold_italic_font', str),
    # 'allow_hyperlinks': ('kitty-query-allow_hyperlinks', yesno_bool),
    # 'kitty_clipboard_control': ('kitty-query-clipboard_control', str),
}
#('name', 'version', 'font_family', 'font_size', 'bold_font', 'bold_italic_font', 'allow_hyperlinks', 'clipboard_control')

def nearest_float_fraction(target, fraction_ceiling=100):
    """
    Return nearest fraction of a float value, with denominator less than fraction_ceiling
    """
    best_numerator = 0
    best_denominator = 1
    best_difference = abs(target)

    for denominator in range(1, fraction_ceiling):
        for numerator in range(int(target * denominator) - 1, int(target * denominator) + 2):
            if numerator < 0:
                continue
            fraction = numerator / denominator
            difference = abs(target - fraction)
            if difference < best_difference:
                best_numerator = numerator
                best_denominator = denominator
                best_difference = difference

    return best_numerator, best_denominator

def nearest_fraction(numerator: int, denominator: int, fractions: list[tuple[int, int]]):
    """
    return nearest fraction of 'fractions', given a numerator and denominator
    """
    closest_pair = None
    min_difference = float('inf')

    for tgt_numerator, tgt_denominator in fractions:
        difference = abs(numerator / denominator - tgt_numerator / tgt_denominator)
        if difference < min_difference:
            min_difference = difference
            closest_pair = (tgt_numerator, tgt_denominator)

    return closest_pair
    

def get_terminal_attributes(term, writer, query_str, end='', timeout=3):
    with term.cbreak():
        stime = time.time()
        writer(f'{query_str}')
        resp = term.inkey(timeout=timeout)
        rtt = min(0.1, time.time() - stime)
        if not resp:
            result = ''
        else:
            result = resp
            while True:
                resp = term.inkey(timeout=rtt)
                if resp:
                    result += resp
                    if end and result.endswith(end):
                        break
                    continue
                break
    return result


def get_tiocgwinsz(term, writer):
    # parse TIOCGWINSZ for terminal and font size
    cells_size=(term.width, term.height)
    pixels_size=(term._height_and_width().ws_xpixel, term._height_and_width().ws_ypixel)
    return {
        'COLUMNS': cells_size[0],
        'LINES': cells_size[1],
        'pixels_width': pixels_size[0],
        'pixels_height': pixels_size[1],
    }


def maybe_determine_screen_ratio(attrs):    
    result = {}
    if attrs['pixels_width'] and attrs['pixels_height']:
        screen_ratio = ':'.join(map(str, nearest_fraction(attrs['pixels_width'], attrs['pixels_height'], SCREEN_RATIOS)))
        screen_ratio_name = {
            '4:3': 'VGA',
            '16:9': 'HD',
            '16:10': 'WSXGA',
            '21:9': 'UWHD',
            '32:9': 'WQHD',
        }[screen_ratio]
        # well, not perfectly actual, but nearest fraction
        screen_ratio_actual = ':'.join(map(str, nearest_float_fraction(attrs['pixels_width'] / attrs['pixels_height'])))
        result.update({
            'screen_ratio': screen_ratio,
            'screen_ratio_actual': screen_ratio_actual,
            'screen_ratio_name': screen_ratio_name,
        })
    return result

def determine_private_dec_modes(term, writer, all_modes):
    # Determine *only* mode 2027 support https://mitchellh.com/writing/grapheme-clusters-in-terminals
    # unless all_modes=True.
    #
    # We only care about mode 2027 because it effects unicode parsing. It's very
    # convenient to gather all terminal mode information since we are already
    # testing so many terminals. However, I expect that any terminal that
    # support "grapheme processing" are modes 1 or 3 (set) by default, they are
    # never toggled off (2), and there are even a few that perform grapheme
    # processing, such as kitty, but return 0 (unknown).
    #
    # So this really isn't all that great of an indicator !
    #
    #result_mode2027 = get_terminal_attributes(term, writer, '\x1b[?2027$p', end='$y', timeout=1)
    modes_digits = [2027] if not all_modes else ALL_DEC_PRIVATE_MODES.keys()
    result = {'modes': {}}
    n_fails = 0
    max_fails = 10
    for idx, mode_digits in enumerate(modes_digits):
        result_reply = get_terminal_attributes(term, writer, f'\x1b[?{mode_digits};$p', end='$y', timeout=1)
        if not result_reply:
            n_fails += 1
            if idx == 0:
                # this terminal doesn't appear to respond to our first DEC inquiry
                break
            elif n_fails >= max_fails:
                # this terminal responds to some, but not others? too much time to
                # inquire about them all -- give up after 10 tries
                break
        else:
            if result_reply.startswith(f'\x1b[?{mode_digits};') and result_reply.endswith('$y'):
                value = result_reply[len(f'\x1b[?{mode_digits};'):-len('$y')]
                try:
                    result['modes'][mode_digits] = {
                        # note that 0 and 4 have effectively the same meaning,
                        'value': int(value),
                        # translate the obtuse dec descriptions to human readable ones
                        'value_description': {
                            0: 'no support',       # NOT RECOGNIZED 
                            1: 'toggled on',       # SET 
                            2: 'toggled off',      # RESET 
                            3: 'always on',        # PERMANENTLY SET 
                            4: 'always off',       # PERMANENTLY RESET 
                        }[int(value)],
                        'mode_description': ALL_DEC_PRIVATE_MODES[int(mode_digits)],
                        }
                except (ValueError, KeyError):
                    result['modes'][mode_digits] = {'_invalid_response': result}
                    pass
    return result

def encode_xtgettcap(string):
    # convert given string to 2-byte hexedecimal pairs for each character
    return ''.join([f'{ord(c):02x}' for c in string])

def decode_xtgettcap(string):
    # convert given string to 2-byte hexedecimal pairs for each character
    try:
        return ''.join([chr(int(string[i:i+2], 16)) for i in range(0, len(string), 2)])
    except ValueError:
        return ''

def decode_xtgettcap_response(string):
    if string.startswith('\x1bP0+r') and string.endswith('\x1b\\'):
        # "not supported"
        return "no"
    if string.startswith('\x1bP1+r') and string.endswith('\x1b\\'):
        maybe_key_value = string[len('\x1bP1+r'):-len('\x1b\\')]
        if '=' in maybe_key_value:
            key, value = map(decode_xtgettcap, maybe_key_value.split('=', 1))
            return value
        return decode_xtgettcap(maybe_key_value)
    return ''

def do_terminal_detection(all_modes=False):
    writer = functools.partial(print, end="", flush=True, file=sys.stderr)
    term = blessed.Terminal()
    attrs = {
        'ttype': term.kind,
        'number_of_colors': term.number_of_colors,
    }
    attrs.update(get_tiocgwinsz(term, writer))
    attrs.update(determine_private_dec_modes(term, writer, all_modes=all_modes))
    attrs.update(maybe_determine_software_and_sixel(term, writer))
    attrs.update(maybe_determine_software(term, writer))
    attrs.update(maybe_update_kitty_attributes(term, writer, attrs))
    attrs.update(maybe_determine_font_size(term, writer, attrs))
    attrs.update(maybe_determine_pixel_size(term, writer, attrs))
    attrs.update(maybe_determine_screen_ratio(attrs))

    return attrs

def update_iterm2_attributes(term, writer, attrs):
    result = {}
    if attrs.get('software') == 'iTerm2':
        result_reportCellSize = get_terminal_attributes(term, writer, '\x1b]1337;ReportCellSize\a', timeout=1)
        if result_reportCellSize.startswith('\x1b]1337;ReportCellSize=') and result_reportCellSize.endswith('\x1b\\'):
            cell_size = result_reportCellSize[len('\x1b]1337;ReportCellSize='):-len('\x1b\\')]
            font_height, font_width, *maybe_scale = map(int, map(float, cell_size.split(';')))
            result['font_height'], result['font_width'] = font_height, font_width
            if len(maybe_scale):
                # '1.0', where retina displays are '2.0'
                # https://github.com/hackerb9/lsix/issues/44#issuecomment-2041562851
                attrs['font_scale'] = maybe_scale[0]

def maybe_update_kitty_attributes(term, writer, attrs):
    result = {}
    print('attrs=',attrs)
    if 'kitty' in attrs.get('software', {}):
        for field, (query_field_name, query_field_type) in KITTY_OPTIONS.items():
            result[field] = query_field_type(decode_xtgettcap_response(get_terminal_attributes(term, writer, f'\x1bP+q{encode_xtgettcap(query_field_name)}\x1b\\', end='\x1b\\', timeout=1)))
    return result
 
def maybe_determine_software(term, writer):
    result = {}
    result_xtversion = get_terminal_attributes(term, writer, '\x1b[>q', end='\x1b\\', timeout=1)
    if result_xtversion and result_xtversion.startswith('\x1bP>|') and result_xtversion.endswith('\x1b\\'):
        # parse 'XTVERSION' into software & version string, I wish they all did this, it would make
        # our jobs so much easier !!
        xtversion = result_xtversion[len('\x1bP>|'):-len('\x1b\\')]
        if ' ' in xtversion:
            software, result['software_version'] = xtversion.split(' ', 1)
        elif '(' in xtversion:
            software, result_software_version = xtversion.split('(', 1)
            result['software_version'] = result_software_version.split(')', 1)[0]
        else:
            software = xtversion
        result['software'] = [software]
    return result

def maybe_determine_software_and_sixel(term, writer):
    # Parse "primary display attributes"
    result = {}
    result_pda = get_terminal_attributes(term, writer, f'\x1b[c', end='c', timeout=1)
    if result_pda in CSI_0_C:
        result.update(CSI_0_C[result_pda])

    # if the DA fingerprint is not known, fallback to "does it sixel?" method,
    # sixel support: '4' is one of the primary device attributes,
    # from https://vt100.net/docs/vt510-rm/chapter4.html:
    # Ext     Description               Ext   Description
    # 1      132 columns                18    Windowing capability
    # 2      Printer port extension     21    Horizontal scrolling
    # 4      Sixel extension            23    Greek extension
    # 6      Selective erase            24    Turkish extension
    # 7      DRCS                       42    ISO Latin 2 character set
    # 8      UDK                        44    PCTerm
    # 9      NRCS                       45    Soft key map
    # 12     SCS extension              46    ASCII emulation
    # 15     Technical character set   
    elif result_pda.startswith('\x1b[?') and result_pda.endswith('c'):
        try:
            attribute_values = list(map(int, result_pda[len('\x1b[?'):-len('c')].split(';')))
        except ValueError:
            pass
        else:
            result['sixel'] = 4 in attribute_values
    if result_pda:
        result['_PrimaryDeviceAttributeResponse'] = result_pda
    return result

def maybe_determine_pixel_size(term, writer, attrs):
    result = {}
    if attrs.get('pixels_width') and attrs.get('pixels_height') and attrs.get('sixel'):
        # if window size was determined by TIOCGWINSZ, then can skip the less
        # accurate and slower methods of terminal interrogation
        return {}
    # some terminals (SyncTerm, windows Terminal) use '0' for the pixel size
    # result of TIOCGWINSZ, and maybe this also be the case over ssh or telnet (?)
    # in any case, we depend on the "dtterm window manipulation extensions" that all
    # xterm-derived terminals generally support,
    result_window_size = get_terminal_attributes(term, writer, '\x1b[14t', end='t', timeout=1)
    if result_window_size:
        result['_XTWINOPS_14Response'] = result_window_size
    if result_window_size and result_window_size.startswith('\x1b[4;') and result_window_size.endswith('t'):
        width_height = result_window_size[len('\x1b[4;'):-len('t')]
        win_height, win_width, *_ = map(int, width_height.split(';'))
        result.update({
            "pixels_height": win_height,
            "pixels_width": win_width,
        })
    # fallback to the less reliable method, this should be supported by any terminal that
    # supports sixel. It is not the actual size of the window, but "pixels available for sixel"
    # see https://github.com/contour-terminal/contour/issues/656#issuecomment-1114633736, while
    # some people suggest that 14t is *preferred*, while others believe the opposite,
    # https://github.com/hackerb9/lsix/issues/44#issuecomment-2043650231
    result_xtsmgraphics = get_terminal_attributes(term, writer, '\x1b[?2;1;0S', end='S', timeout=1)
    if result_xtsmgraphics:
        result['_XTSMGRAPHICSResponse'] = result_xtsmgraphics
        if result_xtsmgraphics.startswith('\x1b[?2;0;') and result_xtsmgraphics.endswith('S'):
            width_height = attrs['XTSMGRAPHICS.CREGSXTSM'][len('\x1b[?2;0;'):-len('S')]
            win_width, win_height, *_ = map(int, width_height.split(';'))
            result.update({
                "pixels_width": win_width,
                "pixels_height": win_height,
                "sixel": True,
            })
    elif not (attrs.get("pixels_width") and attrs.get("pixels_height")):
        # Terrible! Assume a basic 4:3 VGA 640x400 screen and font
        result.update({
            "pixels_width": DEFAULT_FONT_WIDTH * attrs['COLUMNS'],
            "pixels_height": DEFAULT_FONT_WIDTH * attrs['LINES'],
        })
    return result

def maybe_determine_font_size(term, writer, attrs):
    # if font_height and width is already deteremined (iTerm2), do not perform interrogation
    result = {}
    if ('font_height' in attrs and 'font_width' in attrs):
        return result
    
    result_font_cell_size = get_terminal_attributes(term, writer, '\x1b[16t', end='t', timeout=1)
    if result_font_cell_size:
        result['_XTWINOPS_16Response'] = result_font_cell_size 
    if result_font_cell_size and result_font_cell_size.startswith('\x1b[6;') and result_font_cell_size.endswith('t'):
        cell_size = result_font_cell_size[len('\x1b[6;'):-len('t')]
        font_height, font_width = map(int, cell_size.split(';'))
        result.update({
            "font_height": font_height,
            "font_width": font_width
        })
    else:
        result['font_height'] = DEFAULT_FONT_HEIGHT
        result['font_width'] = DEFAULT_FONT_WIDTH
    return result


if __name__ == '__main__':
    result = do_terminal_detection(all_modes='--all-modes' in sys.argv)
    import json
    json.dump(result, sys.stdout, indent=4, sort_keys=True)
