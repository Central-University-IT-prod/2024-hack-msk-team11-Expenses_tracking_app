import os

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

SECRET_KEY = "{{sensitive_data}}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    secret: str = "SECRET"

    db_host: str = os.getenv("DB_HOST", "db")
    db_port: int = os.getenv("DB_PORT", 5432)
    db_user: str = os.getenv("DB_USER", "postgres")
    db_password: str = os.getenv("DB_PASSWORD", "password")
    db_name: str = os.getenv("DB_NAME", "postgres")
    next_public_api_url: str

    @computed_field  # type: ignore[misc]
    @property
    def database_url(self) -> str:
        return URL.create(
            drivername="postgresql+asyncpg",
            host=self.db_host,
            port=self.db_port,
            username=self.db_user,
            password=self.db_password,
            database=self.db_name,
        ).render_as_string(hide_password=False)


settings = Settings()
