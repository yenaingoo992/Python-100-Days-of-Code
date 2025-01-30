from turtle import Turtle
import random

COLORS = ["green", "yellow", "red", "orange", "blue"]
STARTING_POSITION  = range(-280, 250)
STEP = 10

class CarManager:

    def __init__(self):
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 260)
            car.setheading(180)
            car.goto(300, random_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(10)

        # self.reset_position()
    # def reset_position(self):
    #     self.x_position = random.choice([300, 310, 320, 330, 340])
    #     self.y_position = random.choice(STARTING_POSITION)
    #     self.goto(x=self.x_position, y=self.y_position)
    #
    # def move(self):
    #     if self.xcor() < -320:
    #         self.reset_position()
    #     self.forward(STEP)