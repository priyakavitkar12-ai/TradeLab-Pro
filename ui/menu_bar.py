"""
TradeLab Pro
Menu Bar
"""

from PySide6.QtGui import QAction


class MenuBar:

    def __init__(self, window):
        self.window = window
        self.menu_bar = window.menuBar()
        self.build()

    def build(self):

        file_menu = self.menu_bar.addMenu("&File")
        data_menu = self.menu_bar.addMenu("&Data")
        scanner_menu = self.menu_bar.addMenu("&Scanner")
        strategy_menu = self.menu_bar.addMenu("&Strategy")
        backtest_menu = self.menu_bar.addMenu("&Backtest")
        reports_menu = self.menu_bar.addMenu("&Reports")
        tools_menu = self.menu_bar.addMenu("&Tools")
        help_menu = self.menu_bar.addMenu("&Help")

        exit_action = QAction("Exit", self.window)
        exit_action.triggered.connect(self.window.close)

        file_menu.addAction(exit_action)