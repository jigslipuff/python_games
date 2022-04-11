from turtle import Screen,Turtle
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

border = Turtle()
border.hideturtle()
border.color("white")
border.penup()
border.goto(-300,0)
border.pendown()
border.pensize(5)
border.speed(0)
border.forward(600)

"""BALL"""
ball = Ball()
"scoreboard"
scoreboard = Scoreboard()

paddle_user = Paddles((0, -350), "yellow")
paddle_ai = Paddles((0, 350), "blue")
screen.listen()
"""user player, uncomment the below lines so u can control it on ur own"""
# screen.onkeypress(fun=paddle_ai.move_left, key="a")
# screen.onkeypress(fun=paddle_ai.move_right, key="d")
# """ai player"""
screen.onkeypress(fun=paddle_user.move_left, key="Left")
screen.onkeypress(fun=paddle_user.move_right, key="Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # ball speed
    screen.update()
    ball.move()
    paddle_ai.goto(ball.xcor(), 350) #paddle is dependent on ball.xcor() remove to control it
    # paddle_user.goto(ball.xcor(),-350) #paddle is dependent on ball.xcor() remove to control it

    """detect collision with walls"""
    if ball.xcor() > 280 or ball.xcor() < - 280:
        ball.bounce_x()

    """detect collision with paddles"""
    if ball.distance(paddle_ai) < 50 and  ball.ycor() < 320 or ball.distance(paddle_user) < 50 and ball.ycor() <- 320:
        ball.bounce_y()
        print(ball.move_speed)


    """out of bounds for AI and user paddles"""
    """detect upper/ai paddle misses """
    if ball.ycor() >= 380:
        scoreboard.add_user_score()
        ball.reset_position()


    """detect  lower/user paddle misses """
    if ball.ycor() <= -380:
        scoreboard.add_ai_score()
        ball.reset_position()

        # print(ball.xcor(), ball.ycor())

screen.exitonclick()
