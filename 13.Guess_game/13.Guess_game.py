# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from Guess_game_art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
level = input("Choose a difficulty level: Easy (e) or Hard (h): ")
if level == "e":
    print("You have chosen the Easy Level.")
    print("You have 10 guesses to guess the number between 1 and 100.")
    guesses = 10
elif level == "h":
    print("You have chosen the Hard Level.")
    print("You have 5 guesses to guess the number between 1 and 100.")
    guesses = 5
else:
    print(f"{level} is not a valid level. Please try again.")
print("I'm thinking of a number between 1 and 100.")

print("")
# Generate a random number between 1 and 100.
answer = random.randint(1, 100)

# Ask the player to submit a guess.

while guesses > 0:
    guess = int(input("Make a guess:"))
    if guess < answer:
        print("Too low.")
        guesses -= 1
        print(f"You have {guesses} guesses remaining.")
    elif guess > answer:
        print("Too high.")
        guesses -= 1
        print(f"You have {guesses} guesses remaining.")
    else:
        print(f"You got it! The answer was {answer}.")
        break
else:
    print(f"You ran out of guesses. The answer was {answer}. Game Over!!")
