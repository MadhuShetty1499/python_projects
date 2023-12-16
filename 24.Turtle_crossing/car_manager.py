from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
DISTANCE = [-240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100,
            120, 140, 160, 180, 200, 220, 240]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.generate_cars()

    def generate_cars(self):
        self.penup()
        self.x = 300
        self.y = random.choice(DISTANCE)
        self.goto(self.x, self.y)
        self.setheading(180)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

