from flask import Flask, render_template
import random
import datetime
import requests

random_number = random.randint(1, 10 )
current_year = datetime.datetime.now().year





app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("indexx.html", num = random_number, year = current_year)

@app.route("/guess/<input>")
def guess(input):
    name = input.capitalize()
    gender_info = eval(requests.get(f"https://api.genderize.io?name={name}").text)
    age_info = eval(requests.get(f"https://api.agify.io?name= {name}").text)
    gender = gender_info["gender"]
    age = age_info["age"]
    return render_template("guess.html", gender = gender, age = age, name = name )



if __name__ == "__main__":
    app.run()


