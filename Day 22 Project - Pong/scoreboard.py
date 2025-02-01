from turtle import Turtle, Screen
screen = Screen()
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0
        self.score()

    def score1(self):
        self.score_1 += 1
    def score2(self):
        self.score_2 += 1

    def score(self):
            screen.tracer(0)
            self.clear()
            self.goto(200,275)
            self.write(self.score_1, False, 'center', font=('Arial', 16, 'normal'))
            self.goto(-200,275)
            self.write(self.score_2, False, 'center', font=('Arial', 16, 'normal'))
            screen.update()



