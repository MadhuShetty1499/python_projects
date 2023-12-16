# # Extract colors from an image
# import colorgram
# def extract_colors(jpg, num_of_colors):
#     colors = colorgram.extract(jpg, num_of_colors)
#     rgb_list = []
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         rgb_list.append((r, g, b))
#     return rgb_list
#
# print(extract_colors("OIP.jpg", 30))

import random
from turtle import Turtle, Screen


color_list = [(160, 153, 148), (123, 104, 89), (214, 210, 205), (166, 155, 159), (219, 221, 225), (215, 209, 212),
              (52, 26, 14), (154, 165, 176), (14, 28, 49), (154, 169, 159), (125, 84, 95), (73, 99, 118),
              (210, 222, 214), (55, 17, 25), (79, 109, 90), (17, 37, 23), (151, 138, 81), (199, 196, 174),
              (151, 113, 122), (143, 120, 116), (115, 32, 44), (204, 184, 191), (118, 38, 26), (87, 73, 23),
              (186, 188, 203), (39, 80, 50), (180, 199, 186), (209, 183, 180), (105, 142, 122), (43, 58, 97)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")
tim.speed("fastest")
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
position = tim.pos()
x = position[0]
y = position[1]
for _ in range(10):
    for _ in range(10):
        tim.pendown()
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
    y += 50
    tim.setpos(x, y)



screen.exitonclick()