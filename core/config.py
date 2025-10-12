from dotenv import load_dotenv
import os


class Config:
    def __init__(self):

        load_dotenv()

        self.BOT_TOKEN = self._get_required("BOT_TOKEN")
        self.ADMIN_ID = self._get_required('ADMIN_ID')
        self.BOT_AUTHOR = self._get_required('BOT_AUTHOR')
        self.BOT_VERSION = self._get_required('BOT_VERSION')

    def _get_required(self, key: str) -> str:
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

    def __str__(self):
        attributes = {}
        for key, value in self.__dict__.items():
            attributes[key] = value

        attrs_str = ', '.join(f"{k}={v}" for k, v in attributes.items())
        return f"Config({attrs_str})"


config = Config()
