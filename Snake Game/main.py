from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def reset_screen():
    screen.clear()
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

screen = Screen()
screen.setup(width=600, height=600)
reset_screen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()

    time.sleep(0.1)

    snake.move()
    
    if snake.walls():
        scoreboard.reset()
        snake.reset() 
        
    # Detect colision of snake with food
    if snake.head.distance(food) < 15:
        food.new_food_position()
        snake.add_piece()
        scoreboard.increase_score()
        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

