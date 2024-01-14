from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.new_food_position()

    def new_food_position(self):
        random_x = random.choice(range(-280, 280, 20))
        random_y = random.choice(range(-280, 280, 20))
        self.goto(random_x, random_y)