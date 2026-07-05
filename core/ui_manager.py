"""
TradeLab Pro
UI Manager
"""

from core.theme_manager import ThemeManager
from core.window_manager import WindowManager


class UIManager:
    """
    Initializes all UI components.
    """

    @classmethod
    def initialize(cls):
        ThemeManager.initialize()
        WindowManager.initialize()