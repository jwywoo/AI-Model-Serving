from fastapi import FastAPI
from .routers import prediction_router

app = FastAPI()

app.include_router(prediction_router.router)

@app.get("/")
async def root():
    return {"message": "this is message and root"}