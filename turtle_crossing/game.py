import random
import time
from turtle import Screen
from car import Car
from player import Player
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score_board = ScoreBoard()
game_speed = 0.1
player = Player()
screen.listen()

cars = []

screen.onkey(player.move,"Up")

is_game_over = False
while not is_game_over:
    time.sleep(game_speed)
    screen.update()

    if len(cars) < 40:
        if random.choice(range(1,101)) % 7 == 0:
            cars.append(Car())

    for car in cars:
        car.move()

    for car in cars:
        if car.distance(player) <= 25:
            is_game_over = True

    if player.ycor() > 260:
        game_speed *= 0.9
        for car in cars:
            car.hideturtle()
            car.clear()
        cars = []
        score_board.next_level()
        player.reset_position()

score_board.game_over()
screen.exitonclick()