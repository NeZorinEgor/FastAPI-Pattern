from pathlib import Path
from datetime import timedelta
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent


class _Auth:
    PRIVATE_JWT_KEY_PATH: Path = BASE_DIR / "auth" / "certs" / "jwt-private.pem"
    PUBLIC_JWT_KEY_PATH: Path = BASE_DIR / "auth" / "certs" / "jwt-public.pem"
    ALGORITHM: str = "RS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: timedelta = timedelta(minutes=240)
    REFRESH_TOKEN_EXPIRE_DAYS: timedelta = timedelta(days=1)
    BAN_MESSAGE: str = "BANNED"


class Settings(BaseSettings):
    APP_PORT: int
    APP_HOST: str
    # Database
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    # Filestorage
    S3_HOST: str
    S3_BUCKETS: str
    GATEWAY_LISTEN: str
    SERVICES: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    # Cache | broker
    REDIS_HOST: str
    REDIS_PORT: str

    @property
    def postgres_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def s3_endpoint_url(self) -> str:
        return f"http://{settings.S3_HOST}:{settings.GATEWAY_LISTEN}"

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    model_config = SettingsConfigDict(env_file=".env.example")


settings = Settings() # noqa
