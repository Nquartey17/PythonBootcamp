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


angles = [0,90,180,270]
turtle.pensize(10)
#increase/decrease animation speed
turtle.speed("fastest")

#Random walk
for _ in range(100):
    turtle.color(random_color())
    turtle.setheading(random.choice(angles))
    turtle.forward(50)


screen.exitonclick()