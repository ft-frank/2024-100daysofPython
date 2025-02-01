from turtle import Turtle


class ScoreBoard:

    def __init__(self):
        self.text = Turtle()
        self.text.ht()
        self.text.color("white")
        self.text.penup()
        self.high = 0

    def score(self, score):
        self.text.clear()
        self.text.goto(-50, 265)
        self.text.write(f"Score: {score}", False, 'center', font=('Arial', 16, 'normal'))
        self.text.goto(50, 265)
        with open("high.txt") as file:
            contents = file.read()
        self.text.write(f"High: {contents}", False, 'center', font=('Arial', 16, 'normal'))


