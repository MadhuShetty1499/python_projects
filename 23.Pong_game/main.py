from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
score_board = Score()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
print(ball.xcor())
screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses out
    if ball.xcor() > 390:
        ball.reset_position()
        score_board.l_point()

    # Detect when left paddle misses out
    if ball.xcor() < -390:
        ball.reset_position()
        score_board.r_point()


screen.exitonclick()
