from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI(title="AI Desktop Todo AI Service")
app.include_router(api_router, prefix="/v1")
