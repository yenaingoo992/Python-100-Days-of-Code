from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Py-Pong")
screen.tracer(0)
screen.listen()
is_game_on = True

player_one = Paddle(x_cor=-360, y_cor=40)
player_two = Paddle(x_cor=360, y_cor=40)
ball = Ball()
score_board = ScoreBoard()

is_Up = True

screen.onkeypress(player_one.up, "w")
screen.onkeypress(player_one.down, "s")

screen.onkeypress(player_two.up, "Up")
screen.onkeypress(player_two.down, "Down")

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # detect collision with top or bottom wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.horizontal_bounce()

    # detect collision with paddle
    if ball.distance(player_one) < 50 and ball.xcor() < -335 or ball.distance(player_two) < 50 and ball.xcor() > 330:
        ball.vertical_bounce()

    # check right paddle has missed
    if ball.xcor() > 400:
        score_board.l_score()
        ball.reset()

    # check right paddle has missed
    if ball.xcor() < -400:
        score_board.r_score()
        ball.reset()

    if score_board.left_score == 3 or score_board.right_score == 3:
        is_game_on = False
        score_board.game_over()

screen.exitonclick()
