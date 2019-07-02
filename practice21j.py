import requests

from bs4 import BeautifulSoup # External library for Parsing HTML Data.

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
tags = soup.find_all("td", class_="titleColumn")

for tag in tags:
    print(tag.text)
    print("====================")
