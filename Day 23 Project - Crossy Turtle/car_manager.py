from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, level):
        super().__init__("square")
        self.shapesize(0.75, random.randint(2,3))
        self.penup()
        self.color(COLORS[random.randint(0, 5)])
        self.goto(random.randint(-320, 10000), random.randint(-230, 260))
        self.setheading(180)
        self.speed("slowest")
        self.move_dis = level * 0.5
        self.increment = 10
        print(self.move_dis)

    def move(self):
        self.forward(self.move_dis)

#BETTER WAY TO SPAWN THE CARS IS TO RANDOMLY GENERATE THEM AT THE BORDER EVERY SINGLE LOOP THEN IT WOULD BE
#iNFINITE


