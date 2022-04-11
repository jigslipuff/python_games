from turtle import Turtle
from ball import Ball
class Paddles(Turtle):
    def __init__(self,paddle_pos,color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(paddle_pos)
        self.color(color)

    def move_right(self):
        if self.xcor() < 250:
            self.forward(30)

    def move_left(self):
        if self.xcor() > -250:
            self.backward(30)




