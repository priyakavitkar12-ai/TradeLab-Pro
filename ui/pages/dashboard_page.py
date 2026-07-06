"""
TradeLab Pro
Dashboard Page
"""

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("TradeLab Pro Dashboard")

        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            padding:20px;
        """)

        layout.addWidget(title)

        self.setLayout(layout)