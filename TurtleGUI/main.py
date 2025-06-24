import turtle
from turtle import Turtle, Screen
import random

turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("red")
turtle.shape("classic")
turtle.color()

#screen color mode needs to be set to 255 to work
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r,g,b)
    return my_tuple


#increase/decrease animation speed
turtle.speed("fastest")

# Setting the radius of the circle
radius = 100

def create_circle(spacing):
    for _ in range(int(360 / spacing)):
        turtle.color(random_color())
        turtle.circle(radius)
        turtle.setheading(turtle.heading() + 10)

create_circle(10)

screen.exitonclick()