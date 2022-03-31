from turtle import Turtle
add_position = []


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 310)
        self.color("white")
        self.get_score = self.write(f"SCORE: {self.score}", align="center", font=("Arial", 12, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.get_score = self.write(f"SCORE: {self.score}", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.get_score = self.write("GAME OVER", align="center", font=("Arial", 12, "normal"))

    def increase_speed(self):
        if self.score >= 5:
            return 0.01




