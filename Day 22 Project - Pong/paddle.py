from turtle import Turtle, Screen

screen = Screen()


class Paddle:

    def __init__(self, player_num):
        self.player_num = player_num
        self.paddle = []
        self.create_paddle()
        # self.coordinates()


    def create_paddle(self):
        paddle = Turtle("square")
        paddle.color("white")
        paddle.shapesize(5, 1)
        paddle.penup()
        if self.player_num == 1:
            paddle.goto(365, 0)
        if self.player_num == 2:
            paddle.goto(-365, 0)
        self.paddle.append(paddle)
        # return (self.paddle[0].xcor(), self.paddle[0].ycor())

    def go_up(self):
        new_y = self.paddle[0].ycor() + 40
        self.paddle[0].goto(self.paddle[0].xcor(), new_y)

    def go_down(self):
        new_y = self.paddle[0].ycor() - 40
        self.paddle[0].goto(self.paddle[0].xcor(), new_y)

    def move(self):
        screen.listen()
        if self.player_num == 2:
            screen.onkeypress(self.go_up, "w")
            screen.onkeypress(self.go_down, "s")
        elif self.player_num == 1:
            screen.onkeypress(self.go_up, "Up")
            screen.onkeypress(self.go_down, "Down")

    def coordinates(self):
        return(self.paddle[0].xcor(), self.paddle[0].ycor())

