import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_start = True

starting_positions = [(0,0),(-20,0),(-40,0)]

snake_body = []

for position in starting_positions:
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(position)
    snake_body.append(turtle)

while game_start:
    screen.update()
    time.sleep(0.1)

    for segment_number in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[segment_number-1].xcor() #second to last position
        new_y = snake_body[segment_number - 1].ycor()
        snake_body[segment_number].goto(new_x, new_y) # last segment

    snake_body[0].forward(20) #move the head of the snake


screen.exitonclick()