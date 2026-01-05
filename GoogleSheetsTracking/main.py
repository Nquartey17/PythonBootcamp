from datetime import datetime
import requests
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = os.environ["SHEET_ENDPOINT"]
WEIGHT_KG = 74
HEIGHT_CM = 185
AGE = 26
GENDER = "male"

activity_log = input("Enter your exercise and duration: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

query_config = {
    "query": activity_log,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER
}

response = requests.post(url=exercise_endpoint,json=query_config,headers=headers,)
result = response.json()

today = datetime.now()

for exercise in result["exercises"]:
    sheety_config = {
        "workout": {
            "date": today.strftime("%Y%m%d"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
      }
    }
    sheet_response = requests.post(url=sheety_endpoint, json=sheety_config,auth=(USERNAME,PASSWORD))
    print(sheet_response.text)


