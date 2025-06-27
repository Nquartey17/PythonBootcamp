from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(position)
            self.snake_body.append(turtle)

    def move(self):
        for segment_number in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_number-1].xcor() #second to last position
            new_y = self.snake_body[segment_number - 1].ycor()
            self.snake_body[segment_number].goto(new_x, new_y) # last segment

        self.head.forward(MOVE_DISTANCE) #move the head of the snake

# prevent the snake from turning in on itself by preventing it from going in the opposite of current direction
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)