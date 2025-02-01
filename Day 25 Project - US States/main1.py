import turtle
import pandas
import time
from scoreboard import Scoreboard
screen = turtle.Screen()
screen.title("US of A!")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(800, 600)
turtle.shape(image)
scoreboard = Scoreboard()

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []

t_end = time.time() + 60 * 10
while time.time() < t_end:
    answer_state = screen.textinput(title = 'Guess the state', prompt = "Guess a state")
    for state in state_list:
        if answer_state == state:
            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()
            state_in_data = data[data.state == answer_state]
            x = int(state_in_data.x.iloc[0])
            y = int(state_in_data.y.iloc[0])
            coordinates = (x, y)
            state_turtle.goto(coordinates)
            state_turtle.write(f"{answer_state}", False, "center")
            guessed_states.append(answer_state)
            scoreboard.score(len(guessed_states))

        elif answer_state == "end":
            missing_states = [state for state in state_list if state not in guessed_states]
            print(missing_states)
            screen.bye()

        if len(guessed_states) == 50:
            screen.bye()
            print("CONGRATULATIONS YOU CAUGHT THEM ALL")












screen.exitonclick()