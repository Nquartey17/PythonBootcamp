import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = False

red = Turtle(shape="turtle")
orange = Turtle(shape="turtle")
yellow = Turtle(shape="turtle")
green = Turtle(shape="turtle")
blue = Turtle(shape="turtle")
purple = Turtle(shape="turtle")

all_turtles = [red, orange, yellow, green, blue, purple]

def initialize_turtle(turtle,color, y):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=-230, y=y)

initialize_turtle(red,"red", -100)
initialize_turtle(orange,"orange", -70)
initialize_turtle(yellow,"yellow", -40)
initialize_turtle(green,"green", -10)
initialize_turtle(blue,"blue", 20)
initialize_turtle(purple,"purple", 50)

if user_bet:
    is_race_on = True

    while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've bet correctly, {winning_color} won the race")
                else:
                    print(f"You've bet incorrectly, {winning_color} won the race")

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
