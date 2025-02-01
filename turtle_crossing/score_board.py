from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-260, y= 270)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level {self.level}", font=("Times New Roman", 18, "normal"), align= "center")

    def next_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", font=("Roboto", 20, "normal"), align="center")