import requests


api_key = "INSERT_API_KEY_HERE"
api = "https://api.openweathermap.org/data/2.5/weather?q=Woodbridge,VA,US&appid=f6da2c90c159c35437fa837e6f7b4869"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

LAT = 37.431572
LONG = -78.656891
API_RAIN_CODE = 700

weather_parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
for hours in weather_data["list"]:
    if int(hours["weather"][0]["id"]) < API_RAIN_CODE:
        print("It's raining, bring an umbrella")
