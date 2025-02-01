from turtle import Turtle, Screen
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280
screen = Screen()

class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.speed("fastest")
        self.penup()
        self.goto(STARTING_POSITION)
        self.PACE = 30
        self.setheading(90)

    def north(self):
        self.setheading(90)
        self.forward(self.PACE)

    def east(self):
        self.setheading(0)
        self.forward(self.PACE)

    def west(self):
        self.setheading(180)
        self.forward(self.PACE)
    
    def south(self):
        self.setheading(270)
        self.forward(self.PACE)

    def move(self):
        screen.listen()
        screen.onkeypress(self.north, "w")
        screen.onkeypress(self.east, "d")
        screen.onkeypress(self.west, "a")
        screen.onkeypress(self.south, "s")
    
    def reset_pos(self):
        self.goto(STARTING_POSITION)





