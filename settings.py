import functools
import logging
import pathlib

import pydantic

__all__ = ["Settings"]

PROJECT_BASE_DIR = pathlib.Path(__file__).resolve().parent
PROJECT_BASE_URL = 'https://some app on heroku.com'


class SettingsClass(pydantic.BaseSettings):
    # base
    PROJECT_NAME: str = pydantic.Field(default="XTB Forex Bot")
    BASE_DIR: pydantic.DirectoryPath = pydantic.Field(default=PROJECT_BASE_DIR)
    SECRET_KEY: str = pydantic.Field(default="SECRET")
    ORIGINS_LIST: list = pydantic.Field(default=["*"], env="ORIGINS")
    DEBUG: bool = pydantic.Field(default=False)
    RELOAD: bool = pydantic.Field(default=False)
    HOST: str = pydantic.Field(default="127.0.0.1")
    PORT: int = pydantic.Field(default=8000)
    # logging
    COLOR_LOGS: bool = pydantic.Field(default=False)
    LOGGER_NAME: str = pydantic.Field(default="MAIN_LOGGER")
    LOGGER_LEVEL: int = pydantic.Field(default=logging.INFO)

    PROD_SERVER_URL: str = pydantic.Field(default=PROJECT_BASE_URL)

    
    class Config:
        env_file = PROJECT_BASE_DIR / ".env"


@functools.lru_cache()
def get_settings() -> SettingsClass:
    return SettingsClass()


Settings: SettingsClass = get_settings()