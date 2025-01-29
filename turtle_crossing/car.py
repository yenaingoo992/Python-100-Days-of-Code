from turtle import Turtle
import random

COLORS = ["green", "yellow", "red", "orange", "blue"]
STARTING_POSITION  = range(-280, 250)
STEP = 10

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape("square")
        self.x_position = 0
        self.y_position = 0
        self.setheading(180)
        self.reset_position()

    def reset_position(self):
        self.x_position = random.choice([300, 310, 320, 330, 340])
        self.y_position = random.choice(STARTING_POSITION)
        self.goto(x=self.x_position, y=self.y_position)

    def move(self):
        if self.xcor() < -320:
            self.reset_position()
        self.forward(STEP)