from fastapi import APIRouter
from ..crud.prediction import get_prediction

router = APIRouter()

@router.get("/predict")
def read_prediction():
    return get_prediction()