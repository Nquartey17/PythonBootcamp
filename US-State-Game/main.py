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

while len(correct_states) < 50:
    answer_state = screen.textinput(f"Guess the State {len(correct_states)}/50", "Enter a state name").title()

    if answer_state == "Exit":
        missing_states = []
        for state in temp_list:
            if state not in correct_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in temp_list:
        correct_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        guessed_state = data[data.state == answer_state]
        t.goto(guessed_state.x.item(), guessed_state.y.item())
        t.write(guessed_state.state.item())

        print(answer_state)

#states to learn csv
