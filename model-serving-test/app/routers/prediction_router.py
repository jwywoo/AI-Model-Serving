from fastapi import APIRouter
from ..crud.prediction_crud import get_prediction
from ..schema.prediction_request_schema import PredictionRequestDto
from ..schema.prediction_response_schema import PredictionResponseDto, PredictionsResponseDto
from typing import List

router = APIRouter()

@router.post("/predict", response_model=PredictionsResponseDto)
def read_prediction(request: PredictionRequestDto):
    return get_prediction(request)
