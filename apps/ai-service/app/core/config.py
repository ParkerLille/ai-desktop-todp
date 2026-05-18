from pydantic import BaseModel, Field


class AppConfig(BaseModel):
    app_name: str = Field(default="AI Desktop Todo AI Service")
    environment: str = Field(default="development")
