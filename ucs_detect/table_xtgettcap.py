"""
Curated list of terminfo capabilities to query via XTGETTCAP.

Reduced to capabilities that may differentiate terminal emulators for
fingerprinting purposes.

Each entry is (capname, description). See also:

- terminfo(5) man page
- https://sigwait.org/~alex/blog/2025/03/25/XTGETTCAP.html
- https://codeberg.org/dnkl/foot/issues/846
"""

XTGETTCAP_CAPABILITIES = (
    ("TN", "Terminal name"),
    ("Co", "Number of colors"),
    ("RGB", "Bits per color channel"),
    ("colors", "Max colors on screen"),
    ("pairs", "Max color-pairs"),
    ("bce", "Background color erase"),
    ("ccc", "Can redefine colors"),
    ("npc", "No pad character"),
    ("xenl", "Newline glitch"),
    ("acsc", "Graphic charset pairs"),
    ("sgr", "Define video attributes"),
    ("setab", "Set background color"),
    ("setaf", "Set foreground color"),
    ("sitm", "Enter italics mode"),
    ("smcup", "Start alt screen"),
    ("rmcup", "End alt screen"),
    ("kmous", "Mouse event prefix"),
    ("is2", "Initialization string"),
    ("rs1", "Reset string"),
    ("u6", "CPR response format"),
    ("u7", "CPR request"),
    ("u8", "DA response"),
    ("u9", "DA request"),
    # Keypad key sequences
    ("kcuu1", "Up arrow key"),
    ("kcud1", "Down arrow key"),
    ("kcub1", "Left arrow key"),
    ("kcuf1", "Right arrow key"),
    ("khome", "Home key"),
    ("kend", "End key"),
    ("knp", "Next page key"),
    ("kpp", "Previous page key"),
    ("kich1", "Insert character key"),
    ("kdch1", "Delete character key"),
    ("kbs", "Backspace key"),
    ("kcbt", "Back-tab key"),
    # Keypad application mode keys
    ("ka1", "Keypad upper left"),
    ("ka3", "Keypad upper right"),
    ("kb2", "Keypad center"),
    ("kc1", "Keypad lower left"),
    ("kc3", "Keypad lower right"),
    # Function keys
    ("kf1", "Function key F1"),
    ("kf2", "Function key F2"),
    ("kf3", "Function key F3"),
    ("kf4", "Function key F4"),
    ("kf5", "Function key F5"),
    ("kf6", "Function key F6"),
    ("kf7", "Function key F7"),
    ("kf8", "Function key F8"),
    ("kf9", "Function key F9"),
    ("kf10", "Function key F10"),
    ("kf11", "Function key F11"),
    ("kf12", "Function key F12"),
)
