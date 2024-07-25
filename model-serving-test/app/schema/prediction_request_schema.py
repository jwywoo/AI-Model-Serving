from pydantic import BaseModel

class PredictionRequestDto(BaseModel):
    longitude : float
    latitude : float
 