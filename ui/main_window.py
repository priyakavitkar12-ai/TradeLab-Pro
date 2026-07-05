"""
TradeLab Pro
Main Window
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QStatusBar,
)


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TradeLab Pro")
        self.resize(1400, 900)

        self._build_ui()

    def _build_ui(self):

        label = QLabel("Welcome to TradeLab Pro")

        self.setCentralWidget(label)

        self.setStatusBar(QStatusBar())

        self.statusBar().showMessage("Ready")