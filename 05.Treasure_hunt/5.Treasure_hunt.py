print(''' 
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == "right":
    print("You entered into a hole. Game over!!")
if choice1 == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    choice2 = input('Type "wait" to wait for a boat to pickup or type "swim" to swim across\n').lower()
    if choice2 == "swim":
        print("You got killed by a crocodile. Game over!!")
    if choice2 == "wait":
        print("You arrive to an island unharmed. There is a building and has three doors.")
        print("One red, one blue and one green. One of it has a Treasure.")
        choice3 = input('Which color do you choose? "red" or "blue" or "green"\n').lower()
        if choice3 == "red":
            print("You got burnt in a fire. Game over!!")
        if choice3 == "blue":
            print("You got drowned in the water. Game over!!")
        if choice3 == "green":
            print("Congratulations!! You found the Treasure....")
