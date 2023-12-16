from Higher_lower_data import data
from Higher_lower_art import logo, vs
import random

def check_answer(a, b):
    if a['follower_count'] > b['follower_count']:
        return 'a'
    else:
        return 'b'

def choice():
    X = random.randint(0, len(data) - 1)
    return X

game_over = False
right_guesses = 0
current_item = choice()
while not game_over:
    print(logo)

    A = current_item
    print(f"Compare A: {data[A]['name']}, a {data[A]['description']}, from {data[A]['country']}.")

    print(vs)

    B = choice()
    print(f"Against B: {data[B]['name']}, a {data[B]['description']}, from {data[B]['country']}.")

    answer = check_answer(data[A], data[B])
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if guess == answer:
        print("You're right!")
        right_guesses += 1
        current_item = B
    else:
        print("You're wrong.")
        game_over = True
    print(f"You have {right_guesses} right guesses so far.")