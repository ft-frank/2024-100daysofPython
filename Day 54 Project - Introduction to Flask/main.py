from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style = 'text-align: center'>Hello, World!</h1>" \
           "<p> This is a paragraph </p>" \
            "<img src = 'the'/>"

@app.route("/username/<name>")
def greet(name):
    return f"<p> Wassup {name} </p>"




def bold_decorator(function):
    def bolder_function(*args, **kwargs):
        result = function()
        return f"<b>{result}</b>"
    return bolder_function
def emphasis_decorator(function):
    def emphasis_function(*args, **kwargs):
        result = function()
        return f"<em>{result}</em>"
    return emphasis_function
def underline_decorator(function):
    def underline_function(*args, **kwargs):
        result = function()
        return f"<u>{result}</u>"
    return underline_function


@app.route("/bye")
@bold_decorator
@underline_decorator
@emphasis_decorator
def bye():
    return "Bye!"



if __name__ == "__main__":
    app.run()

