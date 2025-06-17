import turtle
from turtle import Turtle, Screen
import random

turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("red")
turtle.shape("classic")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [0,90,180,270]
turtle.pensize(10)
#increase/decrease animation speed
turtle.speed("fastest")

#Random walk
for _ in range(100):
    turtle.color(random.choice(colors))
    turtle.setheading(random.choice(angles))
    turtle.forward(50)

screen = Screen()
screen.exitonclick()