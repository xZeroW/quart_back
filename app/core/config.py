from enum import Enum

from pydantic import EmailStr, Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    APP_NAME: str = Field(default="Quart Back")
    APP_DESCRIPTION: str | None = Field(default=None)
    APP_VERSION: str | None = Field(default=None)
    LICENSE_NAME: str | None = Field(default=None)
    CONTACT_NAME: str | None = Field(default=None)
    CONTACT_EMAIL: EmailStr | None = Field(default=None)
    PASSWORD_URL: str | None = Field(default=None)

    QUART_APP: str | None = Field(default="app.main")
    QUART_SCHEMA_CONVERT_CASING: bool = Field(default=False)


class CryptSettings(BaseSettings):
    JWT_SECRET_KEY: str = Field(default="JWT_SECRET_KEY")
    CRYPTKEY: str = Field(default="CRYPTKEY")
    ALGORITHM: str = Field(default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7)


class DiskSettings(BaseSettings):
    APP_DISK: str = Field(default="s3")


class AWSSettings(BaseSettings):
    AWS_SECRET: str | None = Field(default=None)
    AWS_KEY: str | None = Field(default=None)
    AWS_BUCKET: str | None = Field(default=None)
    AWS_REGION: str | None = Field(default=None)


class SMTPSettings(BaseSettings):
    SMTP_BASE_URL: str | None = Field(default=None)
    SMTP_BASE_URL_ADM: str | None = Field(default=None)
    SMTP_EMAIL_SENDER: EmailStr | None = Field(default=None)
    SMTP_USERNAME: str | None = Field(default=None)
    SMTP_EMAIL_PASSWORD: str | None = Field(default=None)


class RedisCacheSettings(BaseSettings):
    REDIS_CACHE_HOST: str = Field(default="localhost")
    REDIS_CACHE_PORT: int = Field(default=6379)

    @property
    def REDIS_CACHE_URL(self) -> str:
        return f"redis://{self.REDIS_CACHE_HOST}:{self.REDIS_CACHE_PORT}"


class RedisQueueSettings(BaseSettings):
    REDIS_QUEUE_HOST: str = Field(default="localhost")
    REDIS_QUEUE_PORT: int = Field(default=6379)


class ClientSideCacheSettings(BaseSettings):
    CLIENT_CACHE_MAX_AGE: int = Field(default=60)


class RedisRateLimiterSettings(BaseSettings):
    REDIS_RATE_LIMIT_HOST: str = Field(default="localhost")
    REDIS_RATE_LIMIT_PORT: int = Field(default=6379)

    @property
    def REDIS_RATE_LIMIT_URL(self) -> str:
        return f"redis://{self.REDIS_RATE_LIMIT_HOST}:{self.REDIS_RATE_LIMIT_PORT}"


class DefaultRateLimitSettings(BaseSettings):
    DEFAULT_RATE_LIMIT_LIMIT: int = Field(default=10)
    DEFAULT_RATE_LIMIT_PERIOD: int = Field(default=3600)


class TestSettings(BaseSettings):
    QUART_DEBUG: int | None = Field(default=0)


class DatabaseSettings(BaseSettings):
    DATABASE_USER: str = Field(default="postgres")
    DATABASE_PASS: str = Field(default="postgres")
    DATABASE_HOST: str = Field(default="localhost")
    DATABASE_PORT: int = Field(default=5432)
    DATABASE_NAME: str = Field(default="DATABASE_NAME")
    DATABASE_SYNC_PREFIX: str = Field(default="postgresql://")
    DATABASE_ASYNC_PREFIX: str = Field(default="postgresql+asyncpg://")

    @property
    def DATABASE_URI(self) -> str:
        return (
            f"{self.DATABASE_USER}:{self.DATABASE_PASS}@"
            f"{self.DATABASE_HOST}:{self.DATABASE_PORT}/"
            f"{self.DATABASE_NAME}"
        )

    @property
    def DATABASE_URL(self) -> str:
        return f"{self.DATABASE_ASYNC_PREFIX}{self.DATABASE_URI}"


class EnvironmentOption(Enum):
    LOCAL = "local"
    STAGING = "staging"
    PRODUCTION = "production"


class EnvironmentSettings(BaseSettings):
    ENVIRONMENT: EnvironmentOption = Field(default="local")


class Settings(
    AppSettings,
    DatabaseSettings,
    CryptSettings,
    DiskSettings,
    AWSSettings,
    SMTPSettings,
    TestSettings,
    RedisCacheSettings,
    ClientSideCacheSettings,
    RedisQueueSettings,
    RedisRateLimiterSettings,
    DefaultRateLimitSettings,
    EnvironmentSettings,
):
    pass


settings = Settings()
