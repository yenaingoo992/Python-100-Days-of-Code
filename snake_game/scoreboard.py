from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Times New Roman', 16, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('PeachPuff')
        self.penup()
        self.hideturtle()
        self.goto(230, 260)
        self.refresh()

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.color("gold")
        self.write(move=False, align=ALIGNMENT, arg=f"Game Over", font=FONT)

    def refresh(self):
        self.clear()
        self.write(move=False, align=ALIGNMENT, arg=f"Score : {self.score}", font=FONT)
