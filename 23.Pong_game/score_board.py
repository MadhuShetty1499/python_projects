from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.border()


    def update_score(self):
        self.clear()
        self.goto(-180, 220)
        self.write(self.l_score, align="center", font=("Courier", 50, "bold"))
        self.goto(180, 220)
        self.write(self.r_score, align="center", font=("Courier", 50, "bold"))

    def border(self):
        self.penup()
        self.pensize(2)
        self.goto(0, -300)
        self.setheading(90)
        for _ in range(50):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def l_point(self):
        self.l_score += 1
        self.update_score()
        self.border()

    def r_point(self):
        self.r_score += 1
        self.update_score()
        self.border()