from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    FILE_TYPES : list[str]
    MAX_FILE_SIZE : int

    model_config = SettingsConfigDict(env_file=".env")

    def get_settings():
      return Settings()



