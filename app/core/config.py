import os
from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI CRUD Demo"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = Field(
        default="sqlite:///./app.db",
        description="Database connection string"
    )
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 