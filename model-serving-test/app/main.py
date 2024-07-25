from fastapi import FastAPI
from .routers import prediction_router
from .core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Router
app.include_router(prediction_router.router)

# Cors
origins = [
    "http://127.0.0.1:8000 ",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "this is message and root"}

# Remove it
# @app.get("/config")
# async def get_config():
#     return {"project_key": settings.project_key}