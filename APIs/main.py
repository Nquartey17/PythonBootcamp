import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() #Raise exception for error

data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)


# response code meanings: 1XX: processing request, 2XX: returning data, 3XX: no permission
# 4XX: User mistake/error, 5XX: server mistake/error

