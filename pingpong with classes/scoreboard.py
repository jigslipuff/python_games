from turtle import Turtle, Screen

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.ai_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 50)
        self.write(self.ai_score, align="center", font=("Courier", 50, "normal"))
        self.goto(0, -130)
        self.write(self.user_score, align="center", font=("Courier", 50, "normal"))

    def add_user_score(self):
        self.user_score += 1
        self.update_scoreboard()

    def add_ai_score(self):
        self.ai_score += 1
        self.update_scoreboard()


