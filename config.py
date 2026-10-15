import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # The bot token is loaded strictly from the environment or the .env file
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "YOUR_PRODUCTION_TOKEN_HERE")
    
    # Simulated AI assistant API key for standalone operation
    AI_API_KEY: str = os.getenv("AI_API_KEY", "mock_key_claude_3_5")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
