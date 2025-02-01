from turtle import Turtle, Screen
import time


screen = Screen()


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.speed("slow")
        self.penup()
        self.x_pace = 20
        self.y_pace = 20

    def y_bounce(self):
        self.y_pace *= -1.5
    def x_bounce(self):
        self.x_pace *= -1.5

    def speedup(self):
        self.x_pace += 5
        self.y_pace += 5

    def reset(self):
        self.x_pace = 5
        self.y_pace = 5

    def move(self):
        screen.update()
        new_x = self.xcor() + self.x_pace
        new_y = self.ycor() + self.y_pace
        self.goto(new_x, new_y)
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_bounce()

    def coordinates(self):
        return (self.xcor(), self.ycor())

    def reset_pos(self):
        self.goto(0, 0)
        self.x_pace *= -1

