import requests
from bs4 import BeautifulSoup

# Using an archived version, the current version is denied
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

#get h3 with class title
movies = soup.find_all(name="h3", class_="title")
# print(movies)

movies_titles = [movie.getText() for movie in movies]
ordered_movies = movies_titles[::-1]

#encoding added because text contains special characters
with open("movies.txt", mode="w", encoding='utf-8') as file:
    for movie in ordered_movies:
        file.write(f"{movie}\n")