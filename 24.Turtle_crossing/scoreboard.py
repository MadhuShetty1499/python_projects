from turtle import Turtle


FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230, 270)
        self.level = 1
        self.update_score()


    def update_score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)
