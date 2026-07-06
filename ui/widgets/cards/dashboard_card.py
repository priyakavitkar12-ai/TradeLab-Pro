"""
TradeLab Pro
Dashboard Card Widget
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class DashboardCard(QFrame):
    """
    Reusable dashboard card.
    """

    def __init__(self, title, value, subtitle=""):
        super().__init__()

        self.setFixedSize(260, 140)

        self.setObjectName("dashboardCard")

        layout = QVBoxLayout(self)

        layout.setContentsMargins(18, 15, 18, 15)
        layout.setSpacing(6)

        # Title
        titleLabel = QLabel(title)
        titleLabel.setAlignment(Qt.AlignLeft)
        titleLabel.setStyleSheet("""
            font-size:14px;
            color:#BDBDBD;
            font-weight:500;
        """)

        # Value
        valueLabel = QLabel(value)
        valueLabel.setAlignment(Qt.AlignCenter)
        valueLabel.setStyleSheet("""
            font-size:34px;
            font-weight:bold;
            color:#00D26A;
        """)

        # Subtitle
        subtitleLabel = QLabel(subtitle)
        subtitleLabel.setAlignment(Qt.AlignCenter)
        subtitleLabel.setStyleSheet("""
            font-size:12px;
            color:#8A8A8A;
        """)

        layout.addWidget(titleLabel)
        layout.addStretch()
        layout.addWidget(valueLabel)
        layout.addWidget(subtitleLabel)

        self.setStyleSheet("""
            QFrame#dashboardCard{
                background:#2B2B2B;
                border:1px solid #444444;
                border-radius:12px;
            }
        """)