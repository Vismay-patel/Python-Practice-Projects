from turtle import Turtle, Screen, home
import random

screen = Screen()
screen.setworldcoordinates(-400, -400, 400, 400)

user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-375, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            
            race_on = False

            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. Because {winning_color} won the race")
            else:
                print(f"You've lost, because {winning_color} has won the race.")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
