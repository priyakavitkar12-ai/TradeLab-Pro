"""
TradeLab Pro
Page Manager
"""

from PySide6.QtWidgets import QStackedWidget

from ui.pages.dashboard_page import DashboardPage
from ui.pages.scanner_page import ScannerPage
from ui.pages.reports_page import ReportsPage


class PageManager(QStackedWidget):

    def __init__(self):
        super().__init__()

        self.dashboard = DashboardPage()
        self.scanner = ScannerPage()
        self.reports = ReportsPage()

        self.addWidget(self.dashboard)   # Index 0
        self.addWidget(self.scanner)     # Index 1
        self.addWidget(self.reports)     # Index 2