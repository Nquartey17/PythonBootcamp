from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_start = True

snake = Snake()

while game_start:
    screen.update()
    time.sleep(0.1) #

    snake.move()

screen.exitonclick()