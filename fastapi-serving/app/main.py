from fastapi import FastAPI
from .routers import prediction

app = FastAPI()

app.include_router(prediction.router)

@app.get("/")
async def root():
    return {"message": "This is root"}

