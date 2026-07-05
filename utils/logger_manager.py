"""
TradeLab Pro
Logger Manager

Provides centralized logging for the application.
"""

from pathlib import Path
from loguru import logger


class LoggerManager:
    """
    Centralized logger for TradeLab Pro.
    """

    _initialized = False

    @classmethod
    def initialize(cls):
        """
        Initialize the logger only once.
        """

        if cls._initialized:
            return

        # Create logs folder if it doesn't exist
        Path("logs").mkdir(exist_ok=True)

        # Remove default logger
        logger.remove()

        # Console logger
        logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "{message}"
)

        # File logger
        logger.add(
    "logs/application.log",
    level="INFO",
    rotation="10 MB",
    retention="30 days",
    enqueue=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

        cls._initialized = True

    @classmethod
    def info(cls, message: str):
        logger.info(message)

    @classmethod
    def warning(cls, message: str):
        logger.warning(message)

    @classmethod
    def error(cls, message: str):
        logger.error(message)

    @classmethod
    def debug(cls, message: str):
        logger.debug(message)

    @classmethod
    def critical(cls, message: str):
        logger.critical(message)