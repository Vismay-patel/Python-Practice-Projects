from turtle import Turtle

class Player():
    def __init__(self):
        self.segments = self.create_player()


    def create_player(self, x, y, write_text):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x, y)
        new_segment.write(f"{write_text}", align="center", font=("Arial",8,"normal"))

