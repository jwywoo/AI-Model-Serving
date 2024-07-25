from fastapi import APIRouter
from ..crud.prediction_crud import get_prediction
from ..schema.prediction_request_schema import PredictionRequestDto
router = APIRouter()

@router.post("/predict")
def read_prediction(request: PredictionRequestDto):
    return get_prediction(request)
