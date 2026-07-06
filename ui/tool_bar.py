"""
TradeLab Pro
Application Toolbar
"""

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


class ToolBar:

    def __init__(self, window):
        self.window = window
        self.toolbar = QToolBar("Main Toolbar")

        self.toolbar.setMovable(False)

        self.window.addToolBar(self.toolbar)

        self.build()

    def build(self):

        new_action = QAction("New", self.window)
        open_action = QAction("Open", self.window)
        save_action = QAction("Save", self.window)
        import_action = QAction("Import", self.window)
        scan_action = QAction("Scan", self.window)
        backtest_action = QAction("Backtest", self.window)
        settings_action = QAction("Settings", self.window)

        self.toolbar.addAction(new_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(open_action)
        self.toolbar.addAction(save_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(import_action)
        self.toolbar.addAction(scan_action)
        self.toolbar.addAction(backtest_action)
        self.toolbar.addSeparator()

        self.toolbar.addAction(settings_action)