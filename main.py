from turtle import Screen

import time
from car_manager import CarManager
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=800,height=600)
screen.title("Turtle Crossing Game.")
screen.tracer(0)
screen.bgcolor("white")

game_is_on=True
#creating the player
from player import Player
player=Player()
#creating  a car manager instance
car_manager=CarManager()
#listening events.
screen.listen()
screen.onkey(player.move,"Up")
#creating scoreBoard instance
scoreboard=ScoreBoard()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    #checking if player is able to make it across road.
    if(player.ycor()>250):
        scoreboard.game_win()
        game_is_on=False
    #detecting crash with car.
    for car in car_manager.all_cars:
        if(player.distance(car)<=20):
            scoreboard.game_lose()
            game_is_on=False

screen.exitonclick()