import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

cars = []
game_is_on = True
loop = 0
sleep = 0.1
while game_is_on:
    time.sleep(sleep)
    screen.update()
    loop += 1
    if loop % 6 == 0:
        generate_cars = CarManager()
        cars.append(generate_cars)

    for car in cars:
        car.move()

    # Player level up
    if player.ycor() > 280:
        player.restart_position()
        score.increase_level()
        sleep *= 0.7


    # Detect collision with cars
    for car in cars:
        if player.distance(car) < 15:
            score.game_over()
            game_is_on = False


screen.exitonclick()
