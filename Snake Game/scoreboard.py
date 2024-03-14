from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.save_high_score()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.write(f"score: {self.score} High Score {self.high_score }", align="center", font=("Arial", 10, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} High Score {self.high_score }", align="center", font=("Arial", 10, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
  
    def save_high_score(self):
        with open("data.txt", "r") as file:
            content = file.read()
            return int(content)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

