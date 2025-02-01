import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

exit_the_game = False
data = pandas.read_csv("50_states.csv")
correct = []
total = 50
while not exit_the_game and len(correct) < 50:
    answer = screen.textinput(title=f"{len(correct)}/{total} Correct", prompt="What's another state name?")
    if answer is None or answer.lower() == "exit":
        exit_the_game = True
        states = data["state"].tolist()
        learn = set(states) - set(correct)
        pandas.DataFrame(learn).to_csv("learn.csv")
    else:
        result = data[data["state"] == answer.title()]
        if len(result) > 0 and not answer in correct:
            correct.append(answer.title())
            state = Turtle()
            state.hideturtle()
            state.penup()
            state.goto(int(result.x.iloc[0]), int(result.y.iloc[0]))
            state.write(answer)