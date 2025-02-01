from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shapesize(1)
timmy.pensize(15)
timmy.speed(7)


def random_colour():
    r = random.random()
    g = random.random()
    b = random.random()
    random_color = (r, g, b)
    return random_color

def random_walk():
    for step in range(200):
        timmy.pencolor(random_colour())
        direction = random.randint(1,4)
        timmy.right(90 * direction)
        timmy.forward(30)


random_walk()


screen = Screen()
screen.exitonclick()


