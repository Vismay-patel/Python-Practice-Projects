from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
tim.color("red")


# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# for i in range(50):
#     tim.forward(i)
#     tim.penup()
#     tim.forward(i)
#     tim.pendown()
#     tim.right(20)


# for i in range(3, 11):
#     tim.color(random.random(),random.random(),random.random())
#     for j in range(i):
#         tim.forward(100)
#         tim.right(360/i)
# directions = [0, 90, 180, 270]
# tim.pensize(20)
# tim.speed(0)

# for _ in range(200):
#     tim.color(random.random(),random.random(),random.random())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

tim.speed(0)
# tim.circle(100, 360, 200)
# tim.forward(10)
# tim.circle(100, 360, 200)


for i in range(90):
    tim.color(random.random(),random.random(),random.random())
    tim.left(4)
    tim.circle(100)

screen = Screen()
screen.exitonclick()