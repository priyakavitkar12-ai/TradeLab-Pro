"""
TradeLab Pro
Database Manager
"""

from database.session import engine
from database.models import Base
from utils.logger_manager import LoggerManager


class DatabaseManager:
    """
    Handles database initialization.
    """

    @classmethod
    def initialize(cls):
        """
        Create all database tables.
        """
        Base.metadata.create_all(bind=engine)
        LoggerManager.info("SQLite database initialized.")