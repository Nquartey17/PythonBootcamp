import requests
import os

api_key = os.getenv('owm_api_key')
api = "https://api.openweathermap.org/data/2.5/weather?q=Woodbridge,VA,US&appid=f6da2c90c159c35437fa837e6f7b4869"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

LAT = 37.431572
LONG = -78.656891

weather_parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key
}
response = requests.get(OWM_Endpoint, params=weather_parameters)
print(response.json())
