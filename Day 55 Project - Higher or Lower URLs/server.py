from flask import Flask
import random

app = Flask(__name__)
number = random.randint(1, 14)
print(number)


@app.route("/")
def home_page():
    return '<h1> Guess a number between 0 and 14 </h1>' \
           '<img src = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDR0OGpiYWZ0amY3a253NjRwMWNueDRwYzZ5dndhenc5aXQ1N2YwdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/as7kxQw0lrTwjRujhH/giphy-downsized-large.gif">'


@app.route(f"/{number}")
def correct():
    return '<h1> CORRECT </h1>'
@app.route(f"/<guess>")
def check(guess):
    if int(guess)> 14:
        return '<h1> WAY TOO FLIPPEN HIGH</h1>'
    elif int(guess) == number:
            return '<h1> CORRECT </h1>'
    elif int(guess) < number:
        return '<h1> TOO LOW </h1>'
    elif int(guess) > number:
        return '<h1> TOO HIGH </h1>'


if __name__ == "__main__":
    app.run()
