import turtle
from turtle import Turtle, Screen

turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("red")
turtle.shape("classic")

# Function for turtle to move in dashed line
def move_turtle(spaces):
    for _ in range(spaces):
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
        turtle.forward(10)


move_turtle(50)
screen = Screen()
screen.exitonclick()