from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height = 800, width = 800)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a colour: ")
colors = ["orange", "blue", "red", "green", "purple"]
turtles_list = []

move = 0
num = 0
for colour in colors:
    num += 0
    tim = "timmy"
    tim += str(num)
    tim = Turtle(shape = "turtle")
    tim.speed("fast")
    tim.color(colour)
    move += 60
    tim.teleport(x = -380, y = -150 + move)
    turtles_list.append(tim)
race_on = True
while race_on == True:

    for turtles in turtles_list:
        movement = random.randint(1, 20)
        turtles.forward(movement)
        if turtles.xcor() > 400:
            winner = turtles.color()[1]
            if winner == user_bet.lower():
                print(f"You've won! The winning colour was {winner}!")
            else:
                print(f"Unfortunately you've lost. The winning colour was {winner} and your bet was {user_bet} :(")
            race_on = False
            exit()










screen.exitonclick()