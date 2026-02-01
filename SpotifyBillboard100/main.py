import requests
from bs4 import BeautifulSoup

# Billboard pro needed to see previous years on website
# Project incomplete, Spotify developer create app button unavailable
year = input("What year do you want to travel to? Enter format as YYYY-MM-DD: ")

url = "https://www.billboard.com/charts/hot-100/" + year
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"}

response = requests.get(url, headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
songs = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in songs]
print(song_names)

