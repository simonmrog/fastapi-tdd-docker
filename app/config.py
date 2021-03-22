import logging
from pydantic import BaseSettings, AnyUrl

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    ENVIRONMENT: str
    TESTING: bool
    DATABASE_URL: AnyUrl


settings = Settings()
