"""Shared utility functions used across scripts and the ucs_detect package."""


def find_best_failure(records):
    """Find the midpoint failure from a list of failure records."""
    if not records:
        return None
    sorted_records = sorted(records, key=lambda r: r.get("measured_by_wcwidth", 0))
    return sorted_records[len(sorted_records) // 2]


def safe_name(name):
    """Return a filesystem-safe version of *name*."""
    return "".join(c if c.isalnum() or c in "-_" else "_" for c in name)


def decode_wchars(escaped):
    """Decode a unicode-escape-encoded string like ``\\u0915`` to the actual unicode text."""
    return bytes(escaped, "utf-8").decode("unicode-escape")
