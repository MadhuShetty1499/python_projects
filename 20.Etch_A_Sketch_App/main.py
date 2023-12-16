import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def rotate_clockwise():
    tim.right(10)

def rotate_anticlockwise():
    tim.left(10)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_anticlockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()