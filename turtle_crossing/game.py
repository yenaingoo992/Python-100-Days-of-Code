import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from score_board import ScoreBoard

screen = Screen()
car_manager = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
score_board = ScoreBoard()
game_speed = 0.1
player = Player()
screen.listen()

screen.onkey(player.move,"Up")

is_game_over = False
while not is_game_over:
    time.sleep(game_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            is_game_over = True

    # detect player passed the reach line
    if player.is_at_finish_line():
        game_speed *= 0.9
        score_board.next_level()
        player.reset_position()

score_board.game_over()
screen.exitonclick()