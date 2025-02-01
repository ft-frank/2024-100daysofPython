import flask
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods = ["POST"])
def login():
    username = request.form['username']
    pass_w = request.form['password']
    return f"<h1> Name: {username} <br> Password: {pass_w} </h1>"




app.run(debug=True)