from turtle import Turtle
STARTING_POSITION = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_player()
        self.setheading(90)
        self.speed("fastest")
        
    def go_up(self):
        self.forward(10)

    def go_down(self):
        self.backward(10)

    def reset_player(self):
        self.goto(STARTING_POSITION)

