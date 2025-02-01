import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.speed("fastest")
screen = Screen()

def forwards():
    tim.forward(20)
def backwards():
    tim.backward(20)
def anti():
    tim.left(10)
def anti_anti():
    tim.right(10)
def clear():
    tim.clear()
    turtle.resetscreen()


screen.listen()

screen.onkeypress(forwards, "w")
screen.onkeypress(anti, "a")
screen.onkeypress(backwards, "s")
screen.onkeypress(anti_anti, "d")
screen.onkeypress(clear, "c")

screen.listen()


screen.exitonclick()