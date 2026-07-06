"""
TradeLab Pro
Market Overview Card
"""

from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class MarketCard(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("marketCard")

        layout = QVBoxLayout(self)

        title = QLabel("Market Overview")
        title.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
            color:white;
        """)

        nifty = QLabel("Nifty 50      ▲ 25,235")
        bank = QLabel("Bank Nifty    ▼ 56,210")
        gold = QLabel("Gold          ▲ 98,500")

        for label in (nifty, bank, gold):
            label.setStyleSheet("""
                font-size:15px;
                color:#DDDDDD;
            """)

        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(nifty)
        layout.addWidget(bank)
        layout.addWidget(gold)
        layout.addStretch()

        self.setStyleSheet("""
            QFrame#marketCard{
                background:#2B2B2B;
                border:1px solid #444;
                border-radius:12px;
            }
        """)