from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = None
    CORS_ALLOW_ORIGIN: str = None

    class Config:
        env_file = ".env"
