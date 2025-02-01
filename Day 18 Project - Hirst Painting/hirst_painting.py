from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shapesize(1)
timmy.penup()

screen = Screen()
screen.colormode(255)





color_list = [(52, 93, 125), (222, 202, 136), (169, 153, 41), (137, 31, 22), (132, 162, 185), (200, 91, 70), (48, 122, 88), (65, 47, 41), (14, 101, 73), (147, 178, 147), (235, 175, 165), (162, 142, 157), (109, 73, 77), (18, 85, 89), (184, 205, 173), (56, 46, 49), (149, 18, 22), (38, 61, 75), (49, 65, 80), (86, 145, 129), (184, 86, 89), (109, 126, 151), (178, 191, 209), (218, 176, 181)]

def random_colour():
    return random.choice(color_list)



def hirst(reset=0):
    for x in range(10):
        timmy.teleport(-225, -225 + reset)
        reset += 50
        for y in range(10):
            timmy.dot(20, random_colour())
            timmy.forward(50)
    timmy.hideturtle()




hirst()


screen.exitonclick()


