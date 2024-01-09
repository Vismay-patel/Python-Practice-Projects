# import colorgram

# colors = colorgram.extract('dot.jpg', 30)

# list_of_color = []


# for c in colors:
#     list_of_color.append(c.rgb[:])

# print(list_of_color)

# colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]

# import turtle as turtle
# from turtle import Turtle, Screen
# import random

# screen = Screen()
# screen.setworldcoordinates(-10, -10, screen.window_width(), screen.window_height())

# tim = Turtle()
# turtle.colormode(255)
# tim.color("red")

# for i in range(1, 101):
#     tim.speed(5)
#     tim.dot(30,  random.choice(colors))
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()
#     if i % 10 == 0:
#         tim.speed(0)
#         tim.penup()
#         tim.left(90)
#         tim.forward(50)
#         tim.right(90)
#         tim.backward(500)
    

# screen.exitonclick()

from turtle import Turtle,Screen,colormode
import random
 
color_list = [(230, 238, 246), (235, 245, 240), (200, 157, 115), (43, 110, 146), (134, 172, 193), (226, 208, 113),
              (134, 84, 67), (148, 65, 85), (198, 140, 153), (193, 83, 102), (182, 159, 51), (150, 178, 164),
              (191, 98, 83), (68, 114, 94), (227, 170, 182), (36, 51, 68), (225, 177, 168), (45, 157, 186),
              (60, 47, 41), (155, 205, 218), (49, 56, 94), (22, 90, 76), (129, 38, 59), (58, 44, 52), (33, 60, 53),
              (97, 146, 125), (173, 203, 189), (178, 188, 212)]
 
tim = Turtle()
colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()
 
for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        tim.goto(x,y)
        tim.dot(20, random.choice(color_list))
 
screen = Screen()
screen.exitonclick()