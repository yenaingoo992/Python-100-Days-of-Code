import turtle as t
import random

def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return red, green, blue

def draw_dash(turtle: t.Turtle, end: int):
    stop = int(end / 10)
    for i in range(0, stop):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

def draw(turtle: t.Turtle, length: int, num_of_side: int):
    angle = 360 / num_of_side
    print(angle)
    for i in range(num_of_side):
        turtle.right(angle)
        turtle.forward(length)

def drunkard_walk(turtle: t.Turtle, steps: int, step_length: int):
    directions = [0, 90, 180, 270]
    for s in range(steps):
        head = random.choice(directions)
        turtle.color(random_color())
        turtle.setheading(head)
        turtle.forward(step_length)

def spirograph(turtle: t.Turtle, gap: int):
    for c in range(int(360/gap)):
        turtle.color(random_color())
        turtle.circle(100)
        current_heading = turtle.heading()
        turtle.setheading(current_heading + gap)


timmy = t.Turtle()
t.colormode(255)
timmy.shape("circle")
timmy.width(1) # width of the pen size
# draw_dash(timmy, 100)
# for side in range(3, 11):
#     draw(timmy, 100, side)
timmy.hideturtle()
timmy.speed("fastest")
# drunkard_walk(timmy, 1500, 20)
spirograph(timmy, 10)

screen = t.Screen()
screen.exitonclick()