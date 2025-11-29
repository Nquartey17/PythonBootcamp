import requests
from datetime import datetime
#Latitude and Longitude for Virginia
LAT = 37.431572
LONG = -78.656891


parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}

#This API won't work without parameters (error 400)
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0]) #Print the hour of 24 hour clock

time_now = datetime.now()

print(time_now)