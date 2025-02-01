from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard


# Initialisation

scoreboard= ScoreBoard()
screen = Screen()
food = Food() #Creates Food for Snake!
snake = Snake() #Automatically creates snake segments
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#Execution
alive = True
score_real = 0

while alive:
    screen.update()
    time.sleep(0.1)
    # snake.collision(score_real)
    snake.movement()
    scoreboard.score(score_real)

    if snake.segments[0].distance(food.coordinates) < 20:
        score_real += 1
        food.ht()
        food = Food()
        snake.add_segment()

    if snake.segments[0].xcor() < -300 or snake.segments[0].xcor() > 300 or snake.segments[0].ycor() < -300 or snake.segments[0].ycor() > 300 or snake.collision(score_real) == 1:
        # print("Game Over")
        # print(f"Your score was {score_real}")w
        time.sleep(0.6)
        with open("high.txt", "r") as file:
            current = int(file.read())
        if current < score_real:
            with open("high.txt", "w") as file:
                file.write(str(score_real))
        score_real = 0
        snake.reset_pos()













screen.exitonclick()
