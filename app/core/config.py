from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI GraphQL Example"
    DEBUG: bool = True

    class Config:
        env_file = ".env"


@lru_cache
def get_envs():
    return Settings()
