from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def score_track(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 25, "normal"))



