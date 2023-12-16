from turtle import Turtle, Screen
import random

screen = Screen()
w = 500
h = 400
screen.setup(width=w, height=h)
colors = ["red", "green", "orange", "blue", "yellow", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                                                          "Pick a color (red, green, orange, blue, yellow, purple)")
move = [10, 20, 30, 40, 50]
x = -(w/2 - 20)
y = -(h/2 - 57)

all_turtles = []
for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x, y)
    y += 57
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet.lower() == winner:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
