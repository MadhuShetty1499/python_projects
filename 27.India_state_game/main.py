from turtle import Turtle, Screen
import pandas

tim = Turtle()
screen = Screen()
screen.setup(width=700, height=700)
screen.title("India States Game")
image = "blank_image.gif"
screen.addshape(image)
tim.shape(image)
tim.penup()
correct_states = []

states = pandas.read_csv("27_india_states.csv")

while len(correct_states) < len(states):
    answer_state = screen.textinput(title=f"{len(correct_states)}/28 States correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        states_only = states.state.values
        missed_states = [state for state in states_only if state not in correct_states]
        df = pandas.DataFrame(missed_states)
        df.to_csv("missed_states.csv")
        break

    elif answer_state in states["state"].values:
        if answer_state in correct_states:
            print(f"You already guessed {answer_state}. Try another state!")
        else:
            t = Turtle()
            correct_states.append(answer_state)
            state_data = states[states.state == answer_state]
            t.hideturtle()
            t.penup()
            t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            t.write(state_data.state.item(), align="center", font=("Arial", 8, "normal"))
