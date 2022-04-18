import turtle
from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

border = Turtle()
border.hideturtle()
border.penup()
border.goto(-300, 300)
border.pendown()
border.pensize(10)
for _ in range(0, 4):
    border.color("white")
    border.forward(600)
    border.right(90)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()


    #Detect collision with wall

    if snake.head.xcor()>290 or snake.head.xcor() <-290 or snake.head.ycor() <-290 or snake.head.ycor()>290:
        scoreboard.reset()
        snake.reset()
        # game_is_on = False
        # scoreboard.game_over()

    # Detect collision with tail

    for segment in snake.segments[1:]:
         if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()







screen.exitonclick()
