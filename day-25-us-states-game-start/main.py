import turtle
import pandas as pd
from turtle import Turtle

state_count = 0
given_answer = []
df = pd.read_csv("day-25-us-states-game-start/50_states.csv")
df['state'] = df['state'].str.lower()
states = df['state'].to_list()

screen = turtle.Screen()
screen.title("US state game")
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

def create_player(x, y, write_text):
    player = Turtle()
    player.penup()
    player.hideturtle()
    player.goto(x, y)
    player.write(f"{write_text}", align="center", font=("Arial",8,"normal"))


while state_count != 50:
    answer_state = screen.textinput(f"{state_count}/50 Correct States", "What's anothe state's name?").lower().strip()

    if answer_state in given_answer:
        continue
    elif answer_state == 'exit':
        break
    elif answer_state in states:
        x = df.loc[df['state'] == answer_state, 'x'].iloc[0]
        y = df.loc[df['state'] == answer_state, 'y'].iloc[0]
        create_player(x, y, write_text=answer_state)
        given_answer.append(answer_state)
        state_count += 1

states_to_learn = []

for state in states:
    if state not in given_answer:
        states_to_learn.append(state)

data_dict = {'name': states_to_learn}

new_df = pd.DataFrame(data_dict)
new_df.to_csv("day-25-us-states-game-start/states_to_learn.csv", index=False)