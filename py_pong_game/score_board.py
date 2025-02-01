from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.left_score, move= False, align= "center", font=("Courier", 30, "normal"))
        self.goto(100, 250)
        self.write(self.right_score, move=False, align="center", font=("Courier", 30, "normal"))

    def l_score(self):
        self.left_score += 1
        self.update_score()

    def r_score(self):
        self.right_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,50)
        self.write("Game Over", move=False, align="center", font=("Times New Roman", 20, "normal"))
        self.goto(0, 0)
        winner = ""
        if self.left_score > self.right_score:
            winner = "Player One"
        else:
            winner = "Player Two"
        self.write(f"{winner} won!", move=False, align="center", font=("Times New Roman", 30, "normal"))