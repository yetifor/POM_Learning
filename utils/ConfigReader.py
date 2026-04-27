import os
import json


class ConfigReader:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Конфигурационный файл не найден: {config_path}")

        with open(config_path, "r") as file:
            self.config = json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __del__(self):
        ConfigReader.__instance = None
