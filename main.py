import time
from cars import Car
from turtle import Screen
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

game_is_on = True
screen.listen()
screen.onkey(player.turtle_walk, "Up")

count = 0
car_list = []

while game_is_on:
    count += 1
    time.sleep(0.3)
    for i in range(0, len(car_list)):
        car_list[i].move(scoreboard.level)
        if car_list[i].check_run_over(player):
            scoreboard.game_over()
            game_is_on = False
    screen.update()

    if count % 5 == 0:
        car = Car()
        car_list.append(car)
        if player.is_at_finishline():
            scoreboard.add_point()

game_is_on = False

screen.exitonclick()
