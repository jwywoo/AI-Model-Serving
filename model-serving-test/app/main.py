from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .routers import prediction_router
from .core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Router
app.include_router(prediction_router.router)

# Exception
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Please try again later."},
    )

# Cors
origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
    "http://localhost:8000",
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