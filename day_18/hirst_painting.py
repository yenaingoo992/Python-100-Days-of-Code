import turtle as t
import random

rgb_colors = [(2, 13, 31), (52, 25, 17), (218, 127, 106), (10, 105, 159),
              (241, 213, 69), (149, 83, 39), (214, 87, 64), (164, 162, 32), (157, 7, 25), (156, 63, 102), (11, 63, 32),
              (96, 6, 20), (206, 74, 104), (12, 95, 56), (173, 135, 161), (1, 63, 145), (8, 173, 216), (156, 32, 23),
              (5, 212, 207), (9, 139, 86), (145, 227, 216), (122, 193, 148), (101, 219, 229), (221, 178, 217),
              (119, 167, 189), (252, 197, 0), (80, 135, 179), (31, 84, 92), (227, 175, 167), (184, 191, 202),
              (69, 72, 40)]

painter = t.Turtle()
t.colormode(255)
size = 15
painter.speed("fastest")
painter.hideturtle()
x = -225
y = -225

for row in range(0, 10):
    painter.teleport(x, y)
    for col in range(0, 10):
        painter.dot(size, random.choice(rgb_colors))
        painter.penup()
        painter.forward(50)
        painter.pendown()
    y += 50

screen = t.Screen()
screen.exitonclick()
