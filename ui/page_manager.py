"""
TradeLab Pro
Page Manager
"""

from PySide6.QtWidgets import QStackedWidget

from ui.pages.dashboard_page import DashboardPage


class PageManager(QStackedWidget):

    def __init__(self):
        super().__init__()

        print("Page Manager initialized.")

        self.dashboard = DashboardPage()

        self.addWidget(self.dashboard)