"""
TradeLab Pro
Main Window
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QStatusBar

from ui.menu_bar import MenuBar
from ui.tool_bar import ToolBar
from ui.page_manager import PageManager
from ui.navigation_panel import NavigationPanel


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TradeLab Pro")
        self.resize(1400, 900)

        # Menu
        MenuBar(self)

        # Toolbar
        ToolBar(self)

        # Page Manager
        self.page_manager = PageManager()
        self.setCentralWidget(self.page_manager)

        # Navigation Panel
        self.navigation = NavigationPanel(self)
        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            self.navigation
        )

        # Status Bar
        self.create_statusbar()

    def create_statusbar(self):
        """
        Create application status bar.
        """

        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Ready")