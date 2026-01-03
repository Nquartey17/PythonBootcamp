import os
import requests
from dotenv import load_dotenv

# view graph here -> "https://pixe.la/v1/users/nquartey/graphs/graph1.html"
USERNAME = "nquartey"

pixela_endpoint = "https://pixe.la/v1/users"
load_dotenv()
TOKEN_KEY = os.getenv("token")

user_params = {
    "token": TOKEN_KEY,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#Create a new pixela account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "5k graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

#Create a header so token can be used to authenticate user
headers = {
    "X-USER-TOKEN": TOKEN_KEY
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)