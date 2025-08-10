import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_states = []

data = pandas.read_csv("50_states.csv")
temp_list = data.state.to_list()

while correct_states < 50:
    answer_state = screen.textinput(f"Guess the State {correct_states}/50", "Enter a state name")
    if answer_state.capitalize() in temp_list:
        correct_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        guessed_state = data[data.state == answer_state.capitalize()]
        t.goto(guessed_state.x.item(), guessed_state.y.item())
        t.write(guessed_state.state.item())

        print(answer_state.capitalize())




turtle.mainloop()