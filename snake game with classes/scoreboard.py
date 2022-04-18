from turtle import Turtle
add_position = []


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self. high_score = int(data.read())

        self.hideturtle()
        self.penup()
        self.goto(0, 310)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 12, "normal"))

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
        # self.goto(0,0)
        # self.get_score = self.write("GAME OVER", align="center", font=("Arial", 12, "normal"))

    def increase_speed(self):
        if self.score >= 5:
            return 0.01




