from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")
def move_turtle():
    turtle.forward(100)
    turtle.left(90)

move_turtle()
move_turtle()
move_turtle()
move_turtle()


screen = Screen()
screen.exitonclick()