from turtle import Turtle

STARTING_POSITION = (0, -280)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move(self):
        self.forward(10)

    def reset_position(self):
        self.goto(STARTING_POSITION)