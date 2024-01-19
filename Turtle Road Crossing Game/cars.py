from turtle import Turtle
import random

color_list = ["yellow", "black", "blue", "green", "red", "grey", "brown", "pink"]
STARTING_MOVE_DISTANCE = 5

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.color(random.choice(color_list))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.goto(random.randint(320, 450), random.randint(-260, 280))

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        new_y = self.ycor()
        self.goto(new_x, new_y)

