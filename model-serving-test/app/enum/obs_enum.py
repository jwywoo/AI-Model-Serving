from enum import Enum
from datetime import date

# 대정, 구좌, 영실, 서광, 진달래밭, 새별오름, 애월, 외도
columns_1 = ['baseDate', 'averageTemperature', 'lowestTemperature', 'highestTemperature', 'dailyRainfall', 'maximumWindSpeed', 'averageWindSpeed']

# 제주남원, 제주가시리, 중문
columns_2 = ['baseDate', 'averageTemperature', 'lowestTemperature', 'dailyRainfall', 'maximumWindSpeed']

# 대흘 
columns_3 = ['baseDate', 'averageTemperature', 'lowestTemperature', 'dailyRainfall', 'maximumWindSpeed', 'averageWindSpeed']

#어리목
columns_4 = ['baseDate', 'averageTemperature', 'lowestTemperature', 'highestTemperature', 'dailyRainfall', 'maximumWindSpeed', 'maximumWindSpeedDirection', 'averageWindSpeed']

# 월정, 마라도 -> done
columns_5 = ['baseDate', 'averageTemperature', 'lowestTemperature', 'highestTemperature', 'dailyRainfall', 'maximumWindSpeed']

class ObsEnum(Enum):
    # 마라도
    obs_726 = {
        "observatoryName": "마라도",
		"longitude": "126.2679",
		"latitude": "33.1221",
        "last_update": date(2024,7,2),
        "include": columns_5,
        "path_to_model":"app/trained_models/마라도_esm_model.pkl",
    }
    # 외도
    obs_864 = {
        "observatoryName": "외도",
		"longitude": "126.4317",
		"latitude": "33.4769",
        "include":columns_1,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/외도_esm_model.pkl",
    }
    # 대정
    obs_793 = {
        "observatoryName": "대정",	
		"longitude": "126.2263",
		"latitude": "33.2410",
        "include":columns_1,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/대정_esm_model.pkl",
    }
    # 중문
    obs_328 = {
		"observatoryName": "중문",
		"longitude": "126.4060",
		"latitude": "33.2494",
        "include":columns_2,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/중문_esm_model.pkl",
    }
    # 제주남원
    obs_780 = {
        "observatoryName": "제주남원",
		"longitude": "126.7044",
		"latitude": "33.2772",
        "include":columns_2,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/제주남원_esm_model.pkl",
    }
    # 대흘
    obs_330 = {
		"observatoryName": "대흘",
		"longitude": "126.6495",
		"latitude": "33.5008",
        "include":columns_3,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/대흘_esm_model.pkl",
    }
    # 구좌
    obs_781 = {
		"observatoryName": "구좌",
		"longitude": "126.8777",
		"latitude": "33.5199",
        "include":columns_1,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/구좌_esm_model.pkl",
    }
    # 진달래밭
    obs_870 = {
		"observatoryName": "진달래밭",
		"longitude": "126.5557",
		"latitude": "33.3698",
        "include":columns_1,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/진달래밭_esm_model.pkl",
    }
    # 영실
    obs_869 = {
        "observatoryName": "영실",
		"longitude": "126.4964",
		"latitude": "33.3483",
        "include":columns_1,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/영실_esm_model.pkl",
    }
    # 서광
    obs_752 = {
		"observatoryName": "서광",	
		"longitude": "126.3060",
		"latitude": "33.3046",
        "include":columns_1,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/서광_esm_model.pkl",
    }
    # 새별오름
    obs_883 = {
        "observatoryName": "새별오름",
		"longitude": "126.3599",
		"latitude": "33.3623",
        "include":columns_1,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/새별오름_esm_model.pkl",
    }
    # 어리목
    obs_753 = {
		"observatoryName": "어리목",
		"longitude": "126.4959",
		"latitude": "33.3930",
        "include":columns_4,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/어리목_esm_model.pkl",
    }
    # 월정
    obs_861 = {
		"observatoryName": "월정",
		"longitude": "126.7781",
		"latitude": "33.5623",
		"include": columns_5,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/월정_esm_model.pkl",
    }
    # 제주가시리
    obs_890 = {
		"observatoryName": "제주가시리",
		"longitude": "126.7336",
		"latitude": "33.3854",
        "include":columns_2,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/제주가시리_esm_model.pkl",
    }
    # 애월
    obs_893 = {
		"observatoryName": "애월",
		"longitude": "126.3275",
		"latitude": "33.4659",
        "include":columns_1,
        "last_update": date(2024,7,2),
        "path_to_model":"app/trained_models/애월_esm_model.pkl",
    }