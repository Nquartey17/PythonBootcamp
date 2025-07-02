from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

BOUNDS = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_start = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen() # listen for keep press
screen.onkey(snake.up, "Up") # case-sensitive
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_start:
    screen.update()
    time.sleep(0.1) # refresh screen after this duration
    snake.move()

    # Collision dectection
    # if snake head is within 15 pixels of the food
    if snake.head.distance(food) < 15:
        food.move_food()
        snake.extend()
        scoreboard.increase_score()

    # Detect wall collision
    if snake.head.xcor() > BOUNDS or snake.head.xcor() < -BOUNDS or snake.head.ycor() > BOUNDS or snake.head.ycor() < -BOUNDS:
        scoreboard.reset()
        snake.reset()

    # Collision with body
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()