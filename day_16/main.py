from turtle import Turtle, Screen
from prettytable import PrettyTable

def draw_hexagon(t):
    t.forward(100)
    t.left(45)
    t.forward(100)
    t.left(45)
    t.forward(100)
    t.left(45)
    t.forward(100)
    t.left(45)
    t.forward(100)
    t.left(45)
    t.forward(100)
    t.left(45)
    t.forward(100)
    t.left(45)
    t.forward(100)
    t.left(45)

screen = Screen()
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkTurquoise")
draw_hexagon(timmy)

screen.exitonclick()