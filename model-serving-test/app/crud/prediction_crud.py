from ..enum.obs_enum import ObsEnum

def get_prediction(request):
    selected_obs = find_obs(request=request)
    print(selected_obs)
    return {
        "longitude": request.longitude,
        "latitude": request.latitude
    }

def find_obs(request):
    for obs in ObsEnum:
        obs_info = obs.value
        obs_long = float(obs_info['longitude'])
        obs_lat = float(obs_info['latitude'])
        if (request.longitude==obs_long and request.latitude == obs_lat):
            return obs_info
    return None