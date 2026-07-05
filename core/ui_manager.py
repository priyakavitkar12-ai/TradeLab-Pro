"""
TradeLab Pro
UI Manager
"""

import sys

from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow


class UIManager:

    _app = None
    _window = None

    @classmethod
    def initialize(cls):

        print("1. Creating QApplication")

        cls._app = QApplication.instance()

        if cls._app is None:
            cls._app = QApplication(sys.argv)

        print("2. Creating MainWindow")

        cls._window = MainWindow()

        print("3. Showing Window")

        cls._window.show()

    @classmethod
    def run(cls):

        print("4. Entering Event Loop")

        cls._app.exec()

        print("5. Application Closed")