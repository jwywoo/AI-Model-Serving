from pydantic import BaseModel
class PredictionResponseDto(BaseModel):
    obs_name : str
    predicted_date : str


class RainingResponseDto(PredictionResponseDto):
    raining_status : bool
    raining_amount : float

class NoRainingResponseDto(PredictionResponseDto):
    raining_status : bool
