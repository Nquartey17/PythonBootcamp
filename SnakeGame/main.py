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

screen.listen() # listen for keep press
screen.onkey(snake.up, "Up") # case-sensitive
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_start:
    screen.update()
    time.sleep(0.1) # refresh screen after this duration

    snake.move()

screen.exitonclick()