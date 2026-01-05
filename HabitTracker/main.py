import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# view graph here -> "https://pixe.la/v1/users/nquartey/graphs/graph1.html"
USERNAME = "nquartey"
GRAPH_ID = "graph1"
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
    "id": GRAPH_ID,
    "name": "5k graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

#Create a header so token can be used to authenticate user
headers = {
    "X-USER-TOKEN": TOKEN_KEY
}

today = datetime.now()

graph_placement_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
placement_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}

#update graph point
update_endpoint = f"{graph_endpoint}/graph1/{today.strftime('%Y%m%d')}"
update_config = {
    "quantity": "4.3"
}
#
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

#delete graph point
delete_endpoint = f"{graph_endpoint}/graph1/{today.strftime('%Y%m%d')}"

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)

