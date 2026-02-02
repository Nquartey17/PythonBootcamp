import requests
from bs4 import BeautifulSoup

#Fake URL for practice
url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
price = soup.find(class_="a-offscreen").get_text()

print(price.split("$")[1])