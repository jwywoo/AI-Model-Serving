from enum import Enum
from datetime import date

# 대정, 구좌, 영실, 서광, 진달래밭, 새별오름, 애월, 외도
columns_1 = ['observatoryName', 'lowestTemperatureTime', 'highestTemperatureTime', 'maximumWindSpeedTime', 'maximumWindSpeedDirection']

# 제주남원, 제주가시리, 중문
columns_2 = ['observatoryName', 'lowestTemperatureTime', 'highestTemperature', 'highestTemperatureTime', 'maximumWindSpeedTime', 'maximumWindSpeedDirection', 'averageWindSpeed']

# 대흘 
columns_3 = ['observatoryName', 'lowestTemperatureTime', 'highestTemperature', 'highestTemperatureTime', 'maximumWindSpeedTime', 'maximumWindSpeedDirection']

#어리목
columns_4 = ['observatoryName', 'lowestTemperatureTime', 'highestTemperatureTime', 'maximumWindSpeedTime']

# 월정, 마라도
columns_5 = ['baseDate', 'averageTemperature', 'lowestTemperature', 'highestTemperature', 'dailyRainfall', 'maximumWindSpeed']

class ObsEnum(Enum):
    # 마라도
    obs_726 = {
        "observatoryName": "마라도",
		"longitude": "126.2679",
		"latitude": "33.1221",
        "last_update": date(2024,7,2),
        "exclude": columns_5,
    }
    # 외도
    obs_864 = {
        "observatoryName": "외도",
		"longitude": "126.4317",
		"latitude": "33.4769",
        "exclude":columns_1,
        "last_update": date(2024,7,2),
    }
    # 대정
    obs_793 = {
        "observatoryName": "대정",	
		"longitude": "126.2263",
		"latitude": "33.2410",
        "exclude":columns_1,
        "last_update": date(2024,7,2),
    }
    # 중문
    obs_328 = {
		"observatoryName": "중문",
		"longitude": "126.4060",
		"latitude": "33.2494",
        "exclude":columns_2,
        "last_update": date(2024,7,2),
    }
    # 제주남원
    obs_780 = {
        "observatoryName": "제주남원",
		"longitude": "126.7044",
		"latitude": "33.2772",
        "exclude":columns_2,
        "last_update": date(2024,7,2),
    }
    # 대흘
    obs_330 = {
		"observatoryName": "대흘",
		"longitude": "126.6495",
		"latitude": "33.5008",
        "exclude":columns_3,
        "last_update": date(2024,7,2),
    }
    # 구좌
    obs_781 = {
		"observatoryName": "구좌",
		"longitude": "126.8777",
		"latitude": "33.5199",
        "exclude":columns_1,
        "last_update": date(2024,7,2),
    }
    # 진달래밭
    obs_870 = {
		"observatoryName": "진달래밭",
		"longitude": "126.5557",
		"latitude": "33.3698",
        "exclude":columns_1,
        "last_update": date(2024,7,2),
    }
    # 영실
    obs_869 = {
        "observatoryName": "영실",
		"longitude": "126.4964",
		"latitude": "33.3483",
        "exclude":columns_1,
        "last_update": date(2024,7,2),
    }
    # 서광
    obs_752 = {
		"observatoryName": "서광",	
		"longitude": "126.3060",
		"latitude": "33.3046",
        "exclude":columns_1,
        "last_update": date(2024,7,2),
    }
    # 새별오름
    obs_883 = {
        "observatoryName": "새별오름",
		"longitude": "126.3599",
		"latitude": "33.3623",
        "exclude":columns_1,
        "last_update": date(2024,7,2),
    }
    # 어리목
    obs_753 = {
		"observatoryName": "어리목",
		"longitude": "126.4959",
		"latitude": "33.3930",
        "exclude":columns_4,
        "last_update": date(2024,7,2),
    }
    # 월정
    obs_861 = {
		"observatoryName": "월정",
		"longitude": "126.7781",
		"latitude": "33.5623",
		"exclude": columns_5,
        "last_update": date(2024,7,2),
    }
    # 제주가시리
    obs_890 = {
		"observatoryName": "제주가시리",
		"longitude": "126.7336",
		"latitude": "33.3854",
        "exclude":columns_2,
        "last_update": date(2024,7,2),
    }
    # 애월
    obs_893 = {
		"observatoryName": "애월",
		"longitude": "126.3275",
		"latitude": "33.4659",
        "exclude":columns_1,
        "last_update": date(2024,7,2),
    }