# Machine Learning Model Server: Model & API Docs

## Hypothesis

현재로 부터 3일전의 날씨들은 현재 날씨의 특징이 될 수 있다. 그 중에서도 강수량과 관련성이 높은 특징들을 내일의 강수 여부를 구분하는 특징으로 사용할 수 있다.

## Used Model

### Ensemble Model: Voting

- Support Vector Machine(SVM)
- Logistic Regression
- KNN

## API Docs

예측한 결과를 생성하여 하여 클라이언트에 보내기 위해 **FastAPI** 웹프레임워크로 클라이언트의 요청을 받고 처리할 수 있는 **Model Serving Server**를 만들었다.

총 두개의 API를 만들었고 사용방법은 아래와 같다.

1. 특정 장소를 기반으로 예측 결과 반환: 현재 부터 4일 후 까지의 예측 결과를 반환한다.
    - Request Structure(Request DTO)

        ```python
        # schema/prediction_request_schema.py
        from pydantic import BaseModel
        class PredictionRequestDto(BaseModel):
            obs_code : int
        ```

    - Response Structure(Response DTO)

        ```python
        # schema/prediction_response_schema.py
        from pydantic import BaseModel
        class PredictionResponseDto(BaseModel):
            obs_name : str
            predicted_date : str


        class RainingResponseDto(PredictionResponseDto):
            raining_status : bool
            raining_amount : float

        class NoRainingResponseDto(PredictionResponseDto):
            raining_status : bool
        ```

    - Method

        ```python
        # routers/prediction_router.py
        router = APIRouter()

        @router.post("/predict")
        def read_prediction(request: PredictionRequestDto):
            return get_prediction(request)
        
        # crud/prediction_crud.py
        def get_prediction(request):
            # find obs
            ...
            # get model
            ...
            # generate prediction
            return {
                "data": [prediction1, preditionc2, ....]
            }
        ```

    - Response

        ```JSON
        {
            "data": [
                {
                    "obs_name": "마라도",
                    "predicted_date": "20240725",
                    "raining_status": true,
                    "raining_amount": 0
                },
                {
                    "obs_name": "마라도",
                    "predicted_date": "20240726",
                    "raining_status": true,
                    "raining_amount": 0
                },
                {
                    "obs_name": "마라도",
                    "predicted_date": "20240727",
                    "raining_status": true,
                    "raining_amount": 0
                },
                {
                    "obs_name": "마라도",
                    "predicted_date": "20240728", 
                    "raining_status": true,
                    "raining_amount": 0
                }
            ]
        }
        ```

2. Getting predictions of Jeju Island
    - Implementation in progress

아래의 링크를 통해 현재 사용 가능한 API 요청들을 확인 할 수 있고 테스트 해볼 수 있다.

[Swagger: API Docs](https://assemblytown.com/docs)

## 추가 구현 사항

1. API 서버 안정화
    - 모델 최적화 및 Internal Server Error 문제 대응
2. 모델 데이터 최신화 및 자동화 pipeline 생성
3. Github Action과 Docker hub을 이용한 배포 자동화
4. Kubernetese를 활용한 대규모 요청에 대한 대응 능력 확보