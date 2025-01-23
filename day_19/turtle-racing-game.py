from turtle import Turtle, Screen
import random

def create_turtle(index: int, x: int, y: int):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x, y)
    return turtle

screen = Screen()
screen.setup(500, 400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
random.shuffle(colors)
y_positions = [-125, -75, -25, 25, 75, 125]
x_coordinate = -240
turtles = []
has_winner = False

for turtle_index in range(6):
    new_turtle = create_turtle(index=turtle_index, x=x_coordinate, y=y_positions[turtle_index])
    turtles.append(new_turtle)

while not has_winner:
    for t in turtles:
        if t.xcor() > 220:
            has_winner = True
            winning_color = t.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        distance = random.randint(1, 10)
        t.forward(distance)

screen.exitonclick()
