import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")
movies = soup.select(".gallery .title")
movies_list = [movie.getText() for movie in movies]
movies_list.reverse()

with open("./movies.txt", mode="w", encoding="UTF-8") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
