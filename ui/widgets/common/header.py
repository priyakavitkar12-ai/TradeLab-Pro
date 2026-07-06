"""
TradeLab Pro
Header Widget
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
)


class Header(QWidget):

    def __init__(self, title: str):
        super().__init__()

        layout = QHBoxLayout(self)

        titleLabel = QLabel(title)

        titleLabel.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:white;
        """)

        refreshButton = QPushButton("Refresh")

        refreshButton.setFixedSize(100, 36)

        layout.addWidget(titleLabel)

        layout.addStretch()

        layout.addWidget(refreshButton)