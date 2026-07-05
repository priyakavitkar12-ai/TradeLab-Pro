"""
TradeLab Pro
Theme Manager
"""

class ThemeManager:
    """
    Handles application themes.
    """

    _current_theme = "dark"

    @classmethod
    def initialize(cls):
        print("Theme Manager initialized.")

    @classmethod
    def get_theme(cls):
        return cls._current_theme

    @classmethod
    def set_theme(cls, theme: str):
        cls._current_theme = theme