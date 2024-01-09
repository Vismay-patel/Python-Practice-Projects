from turtle import Turtle, Screen, home

tim = Turtle()

screen = Screen()

def move_forwards():
    tim.forward(20)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clear_screen():
    tim.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="c", fun=clear_screen)
screen.exitonclick()