from enum import Enum

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    APP_NAME: str = Field(default="Quart Back", env="APP_NAME")
    APP_DESCRIPTION: str | None = Field(default=None, env="APP_DESCRIPTION")
    APP_VERSION: str | None = Field(default=None, env="APP_VERSION")
    LICENSE_NAME: str | None = Field(default=None, env="LICENSE_NAME")
    CONTACT_NAME: str | None = Field(default=None, env="CONTACT_NAME")
    CONTACT_EMAIL: str | None = Field(default=None, env="CONTACT_EMAIL")
    PASSWORD_URL: str | None = Field(default=None, env="PASSWORD_URL")

    QUART_APP: str | None = Field(default="app.main", env="QUART_APP")

    model_config = SettingsConfigDict(env_file=".env")


class CryptSettings(BaseSettings):
    JWT_SECRET_KEY: str = Field(env="JWT_SECRET_KEY")
    CRYPTKEY: str = Field(env="CRYPTKEY")
    ALGORITHM: str = Field(env="ALGORITHM", default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(env="ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(env="REFRESH_TOKEN_EXPIRE_DAYS", default=7)

    model_config = SettingsConfigDict(env_file=".env")


class DiskSettings(BaseSettings):
    APP_DISK: str = Field(env="APP_DISK")

    model_config = SettingsConfigDict(env_file=".env")


class AWSSettings(BaseSettings):
    AWS_SECRET: str | None = Field(default=None, env="AWS_SECRET")
    AWS_KEY: str | None = Field(default=None, env="AWS_KEY")
    AWS_BUCKET: str | None = Field(default=None, env="AWS_BUCKET")
    AWS_REGION: str | None = Field(default=None, env="AWS_REGION")

    model_config = SettingsConfigDict(env_file=".env")

class SMTPSettings(BaseSettings):
    SMTP_BASE_URL: str | None = Field(default=None, env="SMTP_BASE_URL")
    SMTP_BASE_URL_ADM: str | None = Field(default=None, env="SMTP_BASE_URL_ADM")
    SMTP_EMAIL_SENDER: str | None = Field(default=None, env="SMTP_EMAIL_SENDER")
    SMTP_USERNAME: str | None = Field(default=None, env="SMTP_USERNAME")
    SMTP_EMAIL_PASSWORD: str | None = Field(default=None, env="SMTP_EMAIL_PASSWORD")

    model_config = SettingsConfigDict(env_file=".env")


class RedisCacheSettings(BaseSettings):
    REDIS_CACHE_HOST: str = Field(env="REDIS_CACHE_HOST", default="localhost")
    REDIS_CACHE_PORT: int = Field(env="REDIS_CACHE_PORT", default=6379)

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def REDIS_CACHE_URL(self) -> str:
        return f"redis://{self.REDIS_CACHE_HOST}:{self.REDIS_CACHE_PORT}"


class RedisQueueSettings(BaseSettings):
    REDIS_QUEUE_HOST: str = Field(env="REDIS_QUEUE_HOST", default="localhost")
    REDIS_QUEUE_PORT: int = Field(env="REDIS_QUEUE_PORT", default=6379)

    model_config = SettingsConfigDict(env_file=".env")


class ClientSideCacheSettings(BaseSettings):
    CLIENT_CACHE_MAX_AGE: int = Field(env="CLIENT_CACHE_MAX_AGE", default=60)

    model_config = SettingsConfigDict(env_file=".env")


class RedisRateLimiterSettings(BaseSettings):
    REDIS_RATE_LIMIT_HOST: str = Field(env="REDIS_RATE_LIMIT_HOST", default="localhost")
    REDIS_RATE_LIMIT_PORT: int = Field(env="REDIS_RATE_LIMIT_PORT", default=6379)

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def REDIS_RATE_LIMIT_URL(self) -> str:
        return f"redis://{self.REDIS_RATE_LIMIT_HOST}:{self.REDIS_RATE_LIMIT_PORT}"


class DefaultRateLimitSettings(BaseSettings):
    DEFAULT_RATE_LIMIT_LIMIT: int = Field(env="DEFAULT_RATE_LIMIT_LIMIT", default=10)
    DEFAULT_RATE_LIMIT_PERIOD: int = Field(env="DEFAULT_RATE_LIMIT_PERIOD", default=3600)

    model_config = SettingsConfigDict(env_file=".env")


class TestSettings(BaseSettings):
    QUART_DEBUG: int | None = Field(default=0, env="QUART_DEBUG")


class DatabaseSettings(BaseSettings):
    DATABASE_USER: str = Field(env="DATABASE_USER", default="postgres")
    DATABASE_PASS: str = Field(env="DATABASE_PASS", default="postgres")
    DATABASE_HOST: str = Field(env="DATABASE_HOST", default="localhost")
    DATABASE_PORT: int = Field(env="DATABASE_PORT", default=5432)
    DATABASE_NAME: str = Field(env="DATABASE_DB", default="DATABASE_NAME")
    DATABASE_SYNC_PREFIX: str = Field(env="DATABASE_SYNC_PREFIX", default="postgresql://")
    DATABASE_ASYNC_PREFIX: str = Field(env="DATABASE_ASYNC_PREFIX", default="postgresql+asyncpg://")

    model_config = SettingsConfigDict(env_file=".env")

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
    ENVIRONMENT: EnvironmentOption = Field(env="ENVIRONMENT", default="local")

    model_config = SettingsConfigDict(env_file=".env")


class Settings(
    AppSettings,
    DatabaseSettings,
    CryptSettings,
    DiskSettings,
    AWSSettings,
    SMTPSettings,
    TestSettings,
    # RedisCacheSettings,
    ClientSideCacheSettings,
    # RedisQueueSettings,
    # RedisRateLimiterSettings,
    DefaultRateLimitSettings,
    EnvironmentSettings,
):
    pass


settings = Settings()
