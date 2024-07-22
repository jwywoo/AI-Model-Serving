def get_prediction(request):
    
    return {
        "longitude": request.longitude,
        "latitude": request.latitude
    }