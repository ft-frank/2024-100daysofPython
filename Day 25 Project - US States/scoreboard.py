from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)


    def score(self, score):
        self.clear()
        self.write(f"No. of States guessed: {score}", False, "center")