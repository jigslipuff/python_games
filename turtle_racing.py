#todo build a turtle race

from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=550, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Choose from \nRED,ORANGE,YELLOW,GREEN,BLUE,PURPLE")

colors = ["red", "orange", "black", "green", "blue", "purple"]
all_turtles = []
y_positions = -100

turtle_text = Turtle()
turtle_text.hideturtle()
turtle_text.penup()
turtle_text.goto(x=-75,y=-175)
turtle_text.write(f"You chose:{user_bet}" )

f_line = Turtle()
f_line.hideturtle()
f_line.penup()
f_line.goto(x=250,y = 175)
f_line.pendown()
f_line.pensize(10)
f_line.right(90)
f_line.forward(350)

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions)
    all_turtles.append(new_turtle)
    y_positions += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                turtle_text.clear()
                turtle_text.write("You've won")
            else:
                turtle_text.clear()
                turtle_text.write(f"You lose. The winner is {winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)





screen.exitonclick()