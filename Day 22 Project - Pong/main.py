from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# INITIALISATION OF SCREEN
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
scoreboard = Scoreboard()


# CREATION of Objects
paddle1 = Paddle(1)
paddle2 = Paddle(2)
ball = Ball()


#Lets paddles move freely of game

screen.listen()
paddle1.move()
paddle2.move()
#HIdden functions
score1= 0
score2 = 0


def play():
    play_round = True
    time.sleep(1)
    ball.reset()
    ball.reset_pos()

    while play_round:
        time.sleep(0.05)
        screen.update()
        ball.move()
        if paddle1.paddle[0].distance(ball.coordinates()) < 50 and ball.xcor() > 340:
            ball.x_bounce()
            ball.speedup()
        if paddle2.paddle[0].distance(ball.coordinates()) < 50 and ball.xcor() < -340:
            ball.x_bounce()
            ball.speedup()
        if ball.xcor() > 400:
            scoreboard.score2()
            scoreboard.score()
            play_round = False
        if ball.xcor() < -400:
            scoreboard.score1()
            scoreboard.score()
            play_round = False

    play()


play()





screen.exitonclick()