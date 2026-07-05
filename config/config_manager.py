"""
TradeLab Pro
Configuration Manager

Author : TradeLab Pro
Version : 1.0.0
"""

from pathlib import Path
import json
from typing import Any


class ConfigManager:
    """
    Handles application configuration.

    Responsibilities:
    - Load configuration
    - Read values
    - Reload configuration
    """

    def __init__(self, config_file: str = "config/app.json"):
        self.config_path = Path(config_file)
        self.config = {}
        self.load()

    def load(self) -> None:
        """Load configuration from JSON file."""

        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )

        with open(self.config_path, "r", encoding="utf-8") as file:
            self.config = json.load(file)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Read nested configuration.

        Example:
            application.name
        """

        keys = key.split(".")
        value = self.config

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default

            if value is None:
                return default

        return value

    def reload(self) -> None:
        """Reload configuration file."""
        self.load()