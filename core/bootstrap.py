"""
TradeLab Pro
Bootstrap Manager

Responsible for starting all application services.
"""

from config.config_manager import ConfigManager
from database.database_manager import DatabaseManager
from utils.logger_manager import LoggerManager
from core.ui_manager import UIManager


class Bootstrap:
    """
    Starts all core services in the correct order.
    """

    @classmethod
    def start(cls):

        # Initialize Logger
        LoggerManager.initialize()
        LoggerManager.info("Logger initialized.")

        # Load Configuration
        config = ConfigManager()
        LoggerManager.info("Configuration loaded.")

        # Initialize Database
        DatabaseManager.initialize()
        LoggerManager.info("Database initialized.")

        # Initialize UI
        UIManager.initialize()

        # Application Information
        LoggerManager.info(
            f"Application : {config.get('application.name')}"
        )

        LoggerManager.info(
            f"Version : {config.get('application.version')}"
        )

        LoggerManager.info("Bootstrap completed.")

        # Start Qt Event Loop
        UIManager.run()