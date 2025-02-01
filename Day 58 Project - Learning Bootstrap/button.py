from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def card():
    return render_template("button.html")

app.run()