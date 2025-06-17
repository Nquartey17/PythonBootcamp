import turtle
from turtle import Turtle, Screen

turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("red")
turtle.shape("classic")


def draw_shape(color,sides):
    turtle.color(color)
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(125)
        turtle.right(angle)

#triangle
draw_shape("red",3)

#square
draw_shape("blue",4)

#pentagon
draw_shape("green",5)

#hexagon
draw_shape("DarkGoldenrod",6)

#heptagon
draw_shape("tomato",7)

#octagon
draw_shape("black",8)

#nonagon
draw_shape("navy",9)

#decagon
draw_shape("deeppink4",10)


screen = Screen()
screen.exitonclick()