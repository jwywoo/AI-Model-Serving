import requests
from datetime import datetime, timedelta, date
import joblib
import pandas as pd
import numpy as np
from ..core.config import settings

from ..enum.obs_enum import ObsEnum

def get_prediction(request):
    # find obs
    selected_obs = find_obs(request=request)
    # update df to recent data
    df_up_to_date = weather_recent(obs=selected_obs)
    print("here? 1")
    if (df_up_to_date is None):
        return {
            "message": "Errorrrrrr"
        }
    # Preprocessing
    num_cols = df_up_to_date.drop(columns=['baseDate']).columns
    temp_df = df_up_to_date[num_cols].apply(pd.to_numeric, errors='coerce')
    df_interpolated = temp_df.interpolate(method='linear', axis=0)
    df_interpolated['baseDate'] = df_up_to_date['baseDate']
    preprocessed_data = data_preprocessing(df_interpolated)

    # Prediction
    last_row = preprocessed_data.iloc[-1]
    last_row_df = last_row.to_frame().T.drop(columns=["baseDate", "dailyRainfall"])
    model = joblib.load(selected_obs['path_to_model'])
    model_prediction = model.predict(last_row_df)[0]


    if (model_prediction == 1):
        return {
            "location": selected_obs['observatoryName'],
            "message": "비 내린다!!!!"
        }
    else: 
        return {
            "location": selected_obs['observatoryName'],
            "message": "비 안내린다!!!!"
        }
    
# Supporting Methods
# finding observatory based on given request
def find_obs(request):
    print("find_obs")
    for obs in ObsEnum:
        obs_info = obs.value
        obs_long = float(obs_info['longitude'])
        obs_lat = float(obs_info['latitude'])
        if (request.longitude==obs_long and request.latitude == obs_lat):
            return obs_info
    return None

# Updating recent weather data
def weather_recent(obs):
    print("weather_recent")
    obs_name = obs['observatoryName']
    obs_last_update = obs['last_update']
    now = datetime.now().date()
    df_up_to_date = pd.DataFrame(columns=obs['include'])
    while (obs_last_update < now):
        project_key = settings.project_key
        year_month_day = obs_last_update.strftime("%Y%m%d")
        url = f'https://open.jejudatahub.net/api/proxy/1aD5taat1attaa51Db1511b51ab9Da19/{project_key}?searchDate={year_month_day}&observatoryName={obs_name}'
        response = requests.get(url=url)
        if response.status_code == 200:
            try:
                print(f"Status 200 JSON for {year_month_day}")
                response_json = response.json()
                df_up_to_date = pd.concat([df_up_to_date, json_parsing_200(response_json, obs, year_month_day)], ignore_index=True)
            except ValueError as e:
                print(f"Error decoding JSON for {year_month_day}: {e}")
                print(response.text)
        else:
            return None
        obs_last_update+=timedelta(days=1)
    return df_up_to_date

# Parsing
def json_parsing_200(data, obs, base_date):
    given_data =data['data']
    if (len(given_data) != 0):
        given_data = given_data[0]
        df = pd.DataFrame()
        for column in obs['include']:
            df[column] = [given_data.get(column)]
        return df
    else:
        df = pd.DataFrame()
        for column in obs['include']:
            df[column] = [np.nan]
        df['baseDate'] = [base_date]
        return df

# Preprocessing
def data_preprocessing(df):
    print("preprocessing")
    data = df.sort_values('baseDate')
    prev_day_1 = data.shift(1).drop(columns=['baseDate'])
    prev_day_2 = data.shift(2).drop(columns=['baseDate'])
    prev_day_3 = data.shift(3).drop(columns=['baseDate'])


    combined_data = pd.concat([data['baseDate'], data['dailyRainfall'],prev_day_1.add_suffix('_prev1'), prev_day_2.add_suffix('_prev2'), prev_day_3.add_suffix('_prev3')], axis=1)
    combined_data = combined_data.dropna()
    combined_data = combined_data.reset_index(drop=True)

    return combined_data