import logging
from pydantic import BaseSettings, AnyUrl
from functools import lru_cache


log = logging.getLogger(__name__)


class Settings(BaseSettings):
    ENVIRONMENT: str
    TESTING: bool
    DATABASE_URL: AnyUrl


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
