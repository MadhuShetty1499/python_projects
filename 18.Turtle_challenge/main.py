from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")

# # Draw a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# # Draw a Dashed line
# for _ in range(10):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


# # Draw different shapes
# total = 360
# shapes = [
#     {"triangle": 3},
#     {"square": 4},
#     {"pentagon": 5},
#     {"hexagon": 6},
#     {"heptagon": 7},
#     {"octagon": 8},
#     {"nanogon": 9},
#     {"decagon": 10}
# ]
#
# colors = ["navy", "cyan", "medium aquamarine", "dark green", "khaki", "burlywood", "firebrick", "orange red", "light pink", "green yellow"]
#
# for shape in shapes:
#     value = list(shape.values())[0]
#     tim.color(random.choice(colors))
#     for _ in range(value):
#         tim.forward(100)
#         tim.right(total/value)

# # Generating random colors
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#
# # Draw a random walk
# tim.pensize(5)
# angles = [0, 90, 180, 270]
# tim.speed("fastest")
# for _ in range(200):
#     tim.pencolor(random_colors())
#     tim.forward(20)
#     tim.setheading(random.choice(angles))

# Draw a Spyrograph
tim.speed("fastest")

def draw_spyrograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spyrograph(5)























screen.exitonclick()