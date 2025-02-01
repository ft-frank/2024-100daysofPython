from turtle import Turtle, Screen

from food import Food

from scoreboard import ScoreBoard

starting_position = [(-180, 0), (-160, 0), (-140, 0)]
Move_Distance = 20
screen = Screen()

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def north(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def south(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def west(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def east(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def turn(self):

        screen.onkeypress(self.north, "w")
        screen.onkeypress(self.west, "a")
        screen.onkeypress(self.south, "s")
        screen.onkeypress(self.east, "d")

    def create_snake(self):
        for pos in starting_position:
            blob = Turtle("square")
            blob.color("white")
            blob.speed("fastest")
            blob.penup()
            blob.goto(pos)
            self.segments.append(blob)

    def movement(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_ = self.segments[seg_num - 1].xcor()
            y_ = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_, y_)
        screen.listen()
        self.turn()
        self.segments[0].forward(Move_Distance)


    def add_segment(self):
        blob = Turtle("square", )
        blob.color("white")
        blob.speed("fastest")
        blob.penup()
        self.segments.append(blob)
        blob.showturtle()

    def collision(self,score_real):
        for a in range(len(self.segments) - 1, 0, -1):
            x = self.segments[a].xcor()
            y = self.segments[a].ycor()
            coordinates = (x, y)
            for b in range(len(self.segments) - 1, 0, -1):
                if b == a:
                    continue
                x = self.segments[b].xcor()
                y = self.segments[b].ycor()
                coordinates_2 = (x, y)
                if coordinates == coordinates_2:
                    return 1
                    # print("Game Over")
                    # print(f"Your score was {score_real}")
                    # exit()

    def reset_pos(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
