from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 0
        self.y_move = 0
        self.move_speed = 0.1
        self.starting_direction()

    def starting_direction(self):
        self.x_move = random.randint(5, 10) * random.choice((-1, 1))
        self.y_move = random.randint(5, 10) * random.choice((-1, 1))

    def reset(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.starting_direction()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def horizontal_bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def vertical_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9