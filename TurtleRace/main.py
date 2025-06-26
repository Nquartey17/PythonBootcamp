from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

red = Turtle(shape="turtle")
orange = Turtle(shape="turtle")
yellow = Turtle(shape="turtle")
green = Turtle(shape="turtle")
blue = Turtle(shape="turtle")
purple = Turtle(shape="turtle")

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

screen.exitonclick()
