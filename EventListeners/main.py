from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward) #whe using function as an argument, don't add ()
#using keyword arguments for better clarity
screen.exitonclick()