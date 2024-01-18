from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.move_speed = 20
        self.shape("square")
        self.speed(10)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + self.move_speed
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.move_speed
        self.goto(self.xcor(), new_y)

