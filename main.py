import turtle
from turtle import Turtle, Screen
import random

# import colorgram

# RGB_colour_list = []

# colours = colorgram.extract('image.jpg', 30)

# for colour in colours:
#    r = colour.rgb.r
#    g = colour.rgb.g
#    b = colour.rgb.b
#    new_colour = (r, g, b)
#    RGB_colour_list.append(new_colour)

# print(RGB_colour_list)

# start from here

colour_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
                   (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
                   (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166),
                   (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188),
                   (34, 151, 210), (65, 66, 56)]

scout = Turtle()
scout.penup()
scout.hideturtle()
scout.setposition(-225, -225)
turtle.colormode(255)
y_coordinate = -225


for _ in range(10):
    for _ in range(10):
        scout.pencolor(random.choice(colour_list))
        scout.dot(20)
        scout.forward(50)
    y_coordinate += 50
    scout.setposition(-225, y_coordinate)


screen = Screen()
screen.exitonclick()
