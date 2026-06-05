"""Error matching and filtering for interactive debugging."""

from typing import Optional


class ErrorMatcher:
    """Match and filter errors by test type or language."""

    def __init__(self, filter_value: Optional[str] = None):
        """Initialize with optional filter value."""
        self.filter_value = filter_value.lower() if filter_value else None
        self.enabled = bool(filter_value)
        self.user_disabled = False

    @property
    def active(self) -> bool:
        """Return whether the matcher is active."""
        return self.enabled and not self.user_disabled

    def matches_test_type(self, test_type: str) -> bool:
        """Return whether the given test type matches the filter."""
        if not self.active:
            return False
        if self.filter_value == 'all':
            return True
        if self.filter_value in ('zwj', 'wide', 'narrow', 'vs16', 'vs16n', 'vs15'):
            return test_type == self.filter_value
        return False

    def matches_language(self, language: str) -> bool:
        """Return whether the given language matches the filter."""
        if not self.active:
            return False
        if self.filter_value in ('all', 'lang'):
            return True
        return self.filter_value in language.lower()

    def disable(self):
        """Disable the matcher."""
        self.user_disabled = True
