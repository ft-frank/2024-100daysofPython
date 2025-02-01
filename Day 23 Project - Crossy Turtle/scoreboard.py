from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()


    def score(self, level):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {level}", False, "center", ("Courier", 24, "normal"))


    def game_over(self, level):
        self.clear()
        self.goto(0,  0)
        self.write(f"GAME OVER", False, "center", ("Courier", 32, "normal"))
        self.goto (0, -40)
        self.write(f"final score:{level}", False, "center", ("Courier", 32, "normal"))