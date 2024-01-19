from turtle import Screen
from player import Player
from cars import Cars
import time
from scoreboard import ScoreBoard

car_objects = []

screen = Screen()
def create_screen():
    screen.setup(width= 600, height=600)
    screen.bgcolor("white")
    screen.title("The Turtle Road Crossing Game")
    screen.tracer(0)

create_screen()

player = Player()
score = ScoreBoard()

screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")

car_objects = []

cars = Cars()
car_objects.append(cars)
sleep_time = 0.09

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)

    if car_objects == []:
        cars = Cars()
        car_objects.append(cars)

    if car_objects[-1].xcor() < 350:
        cars = Cars()
        car_objects.append(cars)
    
    if car_objects[0].xcor() < -320:
        del(car_objects[0])
        
    for i in car_objects:
        i.move()  
        
        if player.distance(i) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() > 300:
        score.increase_score()
        player.reset_player()
        sleep_time -= 0.01

    screen.update()



screen.exitonclick()