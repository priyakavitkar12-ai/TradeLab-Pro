"""
TradeLab Pro
Main Window
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QStatusBar,
    QListWidget,
    QDockWidget,
    QWidget,
    QVBoxLayout,
)

from ui.menu_bar import MenuBar
from ui.tool_bar import ToolBar
from ui.page_manager import PageManager

class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TradeLab Pro")
        self.resize(1400, 900)

        # Menu & Toolbar
        MenuBar(self)
        ToolBar(self)

        self.page_manager = PageManager()

        # Navigation
        self.create_navigation()

        # Dashboard
        self.create_dashboard()

        # Status Bar
        self.create_statusbar()

    def create_navigation(self):

        self.navigation = QListWidget()

        self.navigation.addItems([
            "🏠 Dashboard",
            "📈 Scanner",
            "🧠 Strategy Builder",
            "📊 Backtesting",
            "📑 Reports",
            "⚙ Settings"
        ])

        dock = QDockWidget("Navigation", self)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea)
        dock.setWidget(self.navigation)

        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

    def create_dashboard(self):

        widget = QWidget()

        layout = QVBoxLayout()

        title = QLabel("TradeLab Pro Dashboard")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            padding:20px;
        """)

        layout.addWidget(title)

        widget.setLayout(layout)

        self.setCentralWidget(self.page_manager)

    def create_statusbar(self):

        self.setStatusBar(QStatusBar())

        self.statusBar().showMessage("Ready")