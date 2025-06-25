import colorgram, random
from turtle import Turtle, Screen

colors = colorgram.extract('image.jpg', 15)
colors_list = []
#
# for i in range(len(colors)):
#     color = colors[i]
#     rgb = color.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     rgb_color = (red,green,blue)
#     colors_list.append(rgb_color)
#
# print(colors_list)
pulled_colors = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73)]

turtle = Turtle()
turtle.shape('circle')
turtle.speed("fastest")
turtle.penup() # prevents lines from being shown.=
turtle.hideturtle() #prevents turtle from showing at the end of painting

screen = Screen()
screen.colormode(255)

#Set starting point so turtle doesn't go off the page
turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)

for _ in range(10):
    # change color and place dot first, then move
    turtle.dot(20,random.choice(pulled_colors))

    for _ in range(9):
        turtle.forward(50)
        turtle.dot(20,random.choice(pulled_colors))

    #move up a row and back to the starting point
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(450)
    #Face right again
    turtle.right(180)

screen.exitonclick()
