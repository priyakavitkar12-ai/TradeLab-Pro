from config.config_manager import ConfigManager


def main():

    config = ConfigManager()

    print("=" * 50)
    print(config.get("application.name"))
    print(config.get("application.version"))
    print(config.get("database.path"))
    print("=" * 50)


if __name__ == "__main__":
    main()