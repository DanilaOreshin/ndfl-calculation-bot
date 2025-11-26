import os

from dotenv import load_dotenv


class BotConfig:
    def __init__(self) -> None:

        load_dotenv()

        self.BOT_TOKEN = self._get_required("BOT_TOKEN")
        self.BOT_ADMIN_ID = int(self._get_required('BOT_ADMIN_ID'))
        self.BOT_DEVELOPER = self._get_required('BOT_DEVELOPER')
        self.BOT_VERSION = self._get_required('BOT_VERSION')

        self.LIMITS_LIST = [2_400_000.00, 5_000_000.00, 20_000_000.00, 50_000_000.00]
        self.PERCENTS_LIST = [13.00, 15.00, 18.00, 20.00, 22.00]

        self.MAX_YEAR_GROSS = 1_000_000_000_000.00
        self.MAX_FLOAT_VALUE = 100_000_000.00

    @staticmethod
    def _get_required(key: str) -> str:
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Missing required environment variable: {key}")
        return value

    # def _get_optional(self, key: str, default: any = None, type_cast: type = str) -> any:
    #     value = os.getenv(key)
    #     if value is None:
    #         return default
    #     try:
    #         return type_cast(value) if type_cast else value
    #     except (ValueError, TypeError):
    #         return default

    def __str__(self) -> str:
        attributes = {}
        for key, value in self.__dict__.items():
            attributes[key] = value

        attrs_str = ', '.join(f"{k}={v}" for k, v in attributes.items())
        return f"Config({attrs_str})"


config = BotConfig()
