from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("22.Snake_game/data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("22.Snake_game/data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score_board()
