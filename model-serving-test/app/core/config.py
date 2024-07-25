from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    project_key: str

    class Config:
        env_file = '.env'

settings = Settings()