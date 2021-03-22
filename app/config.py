import logging
from pydantic import BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    ENVIRONMENT: str = "dev"
    TESTING: bool = False


settings = Settings()
