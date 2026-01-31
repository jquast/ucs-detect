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
    ("u8", "DA request"),
    ("u9", "DA response"),
)
