from functools import lru_cache

from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    KEY_LENGTH: int
    POSTGRES_HOST: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
