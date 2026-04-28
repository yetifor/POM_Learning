import os
import json


class ConfigReader:
    DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
    _instances = {}

    def __new__(cls, config_path=None):
        if config_path is None:
            config_path = cls.DEFAULT_CONFIG_PATH
            config_path = os.path.abspath(config_path)
        if config_path in cls._instances:
            return cls._instances[config_path]

        instance = super().__new__(cls)
        instance._config_path = config_path
        instance._load_config()
        cls._instances[config_path] = instance
        return instance

    def _load_config(self):
        if not os.path.exists(self._config_path):
            raise FileNotFoundError(f"Конфигурационный файл не найден: {self._config_path}")

        with open(self._config_path, "r") as file:
            self.config = json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __del__(self):
        ConfigReader.__instance = None
