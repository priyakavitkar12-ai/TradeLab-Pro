"""
TradeLab Pro
Navigation Panel
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget, QDockWidget


class NavigationPanel(QDockWidget):

    def __init__(self, window):
        super().__init__("Navigation")

        self.window = window

        self.list = QListWidget()

        self.list.addItems([
            "Dashboard",
            "Scanner",
            "Reports"
        ])

        self.setWidget(self.list)

        self.setAllowedAreas(Qt.LeftDockWidgetArea)

        self.list.currentRowChanged.connect(
            self.change_page
        )

    def change_page(self, index):

        self.window.page_manager.setCurrentIndex(index)