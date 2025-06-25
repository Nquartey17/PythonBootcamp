from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
turtle.speed("fastest")

def move_forward():
    turtle.forward(25)

def move_backward():
    turtle.backward(25)

def turn_left():
    turtle.left(25)

def turn_right():
    turtle.right(25)

def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
