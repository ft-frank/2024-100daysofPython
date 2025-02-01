import requests

url = "https://api.themoviedb.org/3/search/movie?query=Dune&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMjZiNjQ3MDU1NjUyYzhiMTMwNTllNjY4NGQ0ZGFhMSIsInN1YiI6IjY2MTIwYjViMzU2YTcxMDE3ZDI0Yzk0NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.k6TQe9_FpSLNxuoqWW_ReRbL8QfixE5XFW3QgcI4__Y"
}

response = requests.get(url, headers=headers)

print(response.text)

