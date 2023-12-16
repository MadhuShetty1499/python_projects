# Rock Paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
list = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if player > 2:
  print("You typed an Invalid number. You lose.")
else:
  print(list[player])
  rand_number = random.randint(0,2)
  print(f"Computer choose:")
  print(list[rand_number])
  if player == rand_number:
    print("It's a tie.")
  elif player == 0 and rand_number == 2:
    print("You win.")
  elif player == 1 and rand_number == 0:
    print("You win.")
  elif player == 2 and rand_number == 1:
    print("You win.")
  else:
    print("You lose.")