from config.config_manager import ConfigManager
from utils.logger_manager import LoggerManager


def main():

    LoggerManager.initialize()

    LoggerManager.info("TradeLab Pro Started")

    config = ConfigManager()

    LoggerManager.info(
        f"Application : {config.get('application.name')}"
    )

    LoggerManager.info(
        f"Version : {config.get('application.version')}"
    )

    LoggerManager.info(
        f"Database : {config.get('database.path')}"
    )

    print("=" * 50)
    print(config.get("application.name"))
    print(config.get("application.version"))
    print(config.get("database.path"))
    print("=" * 50)


if __name__ == "__main__":
    main()