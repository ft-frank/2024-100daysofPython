from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
page = response.text

soup = BeautifulSoup(page, "html.parser")

title = soup.find(name = "span", class_ = "titleline")
tag = title.text
link = soup.find(name = "a").get("href")
upvote = soup.find(name = "span", class_ = "score").text
print(tag)
print(link)
print(upvote)
