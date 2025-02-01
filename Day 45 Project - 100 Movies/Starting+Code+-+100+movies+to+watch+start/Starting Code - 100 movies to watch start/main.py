import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(f"{URL}")
page = response.text


soup = BeautifulSoup(page, "html.parser")
titles = soup.find_all(name = "h3", class_ = "title")
titles.reverse()
for title in titles:
    print(title.text)
