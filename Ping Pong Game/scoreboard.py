from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 35, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 35, "normal"))

    def increase_score_left(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_score_right(self):
        self.r_score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Final Score for Left: {self.l_score}, and for Right: {self.r_score}",  align="center", font=("Arial", 25, "normal"))