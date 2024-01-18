from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

l_paddle = Paddle(-410, 0)
r_paddle = Paddle(410, 0)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.xcor() > 380 and ball.distance(r_paddle) < 50 or ball.xcor() < -380 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        if ball.xcor() < -380 and ball.distance(l_paddle) < 50:
            ball.x_move += 2
            l_paddle.move_speed += 2
            r_paddle.move_speed += 2

    if ball.xcor() > 430:
        ball.reset_position()
        score.increase_score_left()
        print(f"Left Score: {score.l_score}")

    if ball.xcor() < -430:
        ball.reset_position()
        score.increase_score_right()
        print(f"Right Score: {score.r_score}")

    if score.l_score > 5 or score.r_score > 5:
        game_is_on = False
        score.game_over()
    
        



screen.exitonclick()