import flask
from flask import Flask
import requests
import smtplib

app = Flask(__name__)

@app.route("/")
def home_page():
    blog_url = "https://api.npoint.io/44bea34c126565f25c9b"
    response = requests.get(blog_url)

    return flask.render_template("index.html", posts = response.json())

@app.route("/<num>")
def blog(num):
    blog_url = "https://api.npoint.io/44bea34c126565f25c9b"
    response = requests.get(blog_url)
    return flask.render_template("post.html", posts = response.json(), num = int(num) - 1)

@app.route('/contact')
def contact_page():
    return flask.render_template("contact.html")

@app.route('/about')
def about_page():
    return flask.render_template("about.html")

@app.route("/form-entry", methods = ["Post"])
def receive_data():
    MY_EMAIL = "frank.imagination@gmail.com"
    MY_PASSWORD = "owrtiweonmoglxjh"
    name = flask.request.form["name"]
    phone = flask.request.form["phone"]
    email = flask.request.form["email"]
    message = flask.request.form["message"]
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg=f"Subject:Inquiry\n\nName: {name}\nEmail:{email}\nPhone:{phone}\n\nMessage:{message}"
        )
    return f"<h1> CHECK UR EMAIL TO CHECK IF MESSAGE HAS BEEN SUCCESSFULLY SENT </h1>"


app.run(debug= True)