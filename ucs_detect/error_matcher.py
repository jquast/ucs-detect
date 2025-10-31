"""
Error matching and filtering for interactive debugging.
"""
from typing import Optional

class ErrorMatcher:
    def __init__(self, filter_value: Optional[str] = None):
        self.filter_value = filter_value.lower() if filter_value else None
        self.enabled = bool(filter_value)
        self.user_disabled = False

    def matches_test_type(self, test_type: str) -> bool:
        if not self.enabled or self.user_disabled:
            return False

        # Match specific test types
        if self.filter_value in ('zwj', 'wide', 'vs16', 'vs15'):
            return test_type == self.filter_value

        return False

    def matches_language(self, language: str) -> bool:
        if not self.enabled or self.user_disabled:
            return False

        # Match all languages
        if self.filter_value == 'lang':
            return True

        # Fuzzy case-insensitive matching
        return self.filter_value in language.lower()

    def disable(self):
        self.user_disabled = True
