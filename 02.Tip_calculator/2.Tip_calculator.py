# Project: Tip calculator

print("Welcome to the Tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? %"))
total_bill = bill * (1 + tip/100)
people = int(input("How many people to split the bill? "))
each = total_bill/people
final_bill = "{:.2f}".format(each)
print(f"Each person should pay: ${final_bill}")