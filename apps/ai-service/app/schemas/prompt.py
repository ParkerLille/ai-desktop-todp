from pydantic import BaseModel


class PromptVersionSchema(BaseModel):
    key: str
    version: str
