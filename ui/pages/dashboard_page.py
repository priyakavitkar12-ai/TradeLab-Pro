"""
TradeLab Pro
Dashboard Page
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
)

from ui.widgets.common.header import Header
from ui.widgets.cards.dashboard_card import DashboardCard


class DashboardPage(QWidget):
    """
    Dashboard Page
    """

    def __init__(self):
        super().__init__()

        # Main Layout
        main_layout = QVBoxLayout(self)

        # Header
        header = Header("Dashboard")
        main_layout.addWidget(header)

        # Card Grid
        grid = QGridLayout()
        grid.setSpacing(20)
        grid.setAlignment(Qt.AlignTop)

        # Card 1
        grid.addWidget(
            DashboardCard(
                "NSE Stocks",
                "2345",
                "Available"
            ),
            0,
            0
        )

        # Card 2
        grid.addWidget(
            DashboardCard(
                "Watchlist",
                "12",
                "Stocks"
            ),
            0,
            1
        )

        # Card 3
        grid.addWidget(
            DashboardCard(
                "Scanner Hits",
                "5",
                "Today"
            ),
            0,
            2
        )

        # Card 4
        grid.addWidget(
            DashboardCard(
                "Open Trades",
                "2",
                "Running"
            ),
            0,
            3
        )

        # Add Grid to Main Layout
        main_layout.addLayout(grid)

        # Push everything to top
        main_layout.addStretch()