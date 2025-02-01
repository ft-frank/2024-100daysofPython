from turtle import Turtle, Screen
import random

# timmy.shape("turtle")
def shapes():
    timmy = Turtle()
    timmy.shapesize(1)
    def reposition():
        timmy.penup()
        timmy.setposition(20.00,200.00)
        timmy.pendown()


    def random_colour():
        r = random.random()
        g = random.random()
        b = random.random()
        random_color = (r, g, b)
        return random_color

    def draw_shapes():
        for n in range(3, 11):
            timmy.color(random_colour())
            angle = 360 / n
            for x in range(n):
             timmy.right(angle)
             timmy.forward(150)

    reposition()
    draw_shapes()

shapes()

screen = Screen()
screen.exitonclick()


