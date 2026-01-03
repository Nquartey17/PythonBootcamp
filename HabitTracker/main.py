import os

import requests
from dotenv import load_dotenv

pixela_endpoint = "https://pixe.la/v1/users"
load_dotenv()
token_key = os.getenv("token")

#Create a new pixela account
user_params = {
    "token": token_key,
    "username": "nquartey",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)