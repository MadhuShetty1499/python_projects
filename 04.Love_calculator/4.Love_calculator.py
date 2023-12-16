print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

Name1 = name1.upper()
Name2 = name2.upper()
'''
count1 = 0
count2 = 0
for i in Name1:
    if i == "T":
        count1 += 1
    if i == "R":
        count1 += 1
    if i == "U":
        count1 += 1
    if i == "E":
        count1 += 1
for i in Name2:
    if i == "T":
        count1 += 1
    if i == "R":
        count1 += 1
    if i == "U":
        count1 += 1
    if i == "E":
        count1 += 1
for i in Name1:
    if i == "L":
        count2 += 1
    if i == "O":
        count2 += 1
    if i == "V":
        count2 += 1
    if i == "E":
        count2 += 1
for i in Name2:
    if i == "L":
        count2 += 1
    if i == "O":
        count2 += 1
    if i == "V":
        count2 += 1
    if i == "E":
        count2 += 1
'''

combine_names = Name1 + Name2
t = combine_names.count("T")
r = combine_names.count("R")
u = combine_names.count("U")
e = combine_names.count("E")
L = combine_names.count("L")
O = combine_names.count("O")
V = combine_names.count("V")
E = combine_names.count("E")
first_digit = t + r + u + e
second_digit = L + O + V + E
score = int(str(first_digit) + str(second_digit))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")





