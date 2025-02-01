import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
player = Player()
screen.tracer(0)
cars = []


def create_cars(level):
    for a in range(250):
        car = CarManager(level)
        cars.append(car)

level = 1
scoreboard = Scoreboard()
create_cars(level)
game_is_on = True
while game_is_on:
    screen.update()
    scoreboard.score(level)
    player.move()
    for a in range(250):
        if cars[a].distance(player) < 20:
            game_is_on = False
        cars[a].move()
    if player.ycor() > 280:
        level += 1
        screen.clearscreen()
        screen.tracer(0)
        screen.listen()
        player = Player()
        cars.clear()
        create_cars(level)
        player.move()

screen.clearscreen()
scoreboard = Scoreboard()
scoreboard.game_over(level)





screen.exitonclick()
