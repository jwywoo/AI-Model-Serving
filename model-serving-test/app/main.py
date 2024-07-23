from fastapi import FastAPI
from .routers import prediction_router
from .core.config import settings

app = FastAPI()

app.include_router(prediction_router.router)


@app.get("/")
async def root():
    return {"message": "this is message and root"}

# Remove it
# @app.get("/config")
# async def get_config():
#     return {"project_key": settings.project_key}