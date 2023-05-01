from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI GraphQL Example"
    DEBUG: bool = True

    class Config:
        env_file = ".env"
