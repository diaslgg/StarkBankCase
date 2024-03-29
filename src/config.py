from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


# environment variables configuration
class Settings(BaseSettings):
    private_key: str
    project_id: str
    type_of_environment: str
    url_database: str

    model_config = SettingsConfigDict(env_file=".env")


def get_settings():
    return Settings()
