from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    GOOGLE_AI_API_KEY: str
    LANGSMITH_TRACING: bool = Field(True)
    LANGSMITH_API_KEY: str


setings = Settings()  # pyright: ignore[reportCallIssue]
