from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    client_id: str = "**********************"
    client_secret: str = "******************"
    api_123_url: str = "https://open-api.123pan.com"
    database_host: str = "localhost"
    database_port: int = 3306
    database_user: str = "admin"
    database_password: str = "******************"
    user_id: str = "********************"
    parent_file_id: str = "********************"

    class Config:
        env_file = ".env"

settings = Settings()
