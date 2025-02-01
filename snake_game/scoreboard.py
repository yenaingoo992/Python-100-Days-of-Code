from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Times New Roman', 16, 'bold')


def get_high_score():
    with open("data.txt") as file:
        data = file.read()
        return data

def update_high_score(score: str):
    with open("data.txt", mode="w") as file:
        file.write(score)

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(get_high_score())
        self.color('PeachPuff')
        self.penup()
        self.hideturtle()
        self.goto(170, 260)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            update_high_score(str(self.high_score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(move=False, align=ALIGNMENT, arg=f"Score : {self.score} High Score : {self.high_score}", font=FONT)
