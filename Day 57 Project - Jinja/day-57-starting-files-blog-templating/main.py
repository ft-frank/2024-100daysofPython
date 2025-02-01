import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    print (response.json())
    return render_template("index.html", posts = response.json())

@app.route('/blog/<num>')
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    print(response.json())
    return render_template("post.html", posts=response.json(), num = int(num) - 1)


if __name__ == "__main__":
    app.run()
