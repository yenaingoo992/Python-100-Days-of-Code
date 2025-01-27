from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_cor, y_cor)

    def up(self):
        if self.ycor() <= 220:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() >= -200:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
