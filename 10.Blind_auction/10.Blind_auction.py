from Blind_auction_art import logo
def clear_console():
  print('\n' * 100)
print(logo)
print("Welcome to the secret auction program")
while True:
  name = input("What is your name?: ")
  bid = input("What's your bid? $")
  bid = int(bid)
  new_dict = {}
  new_dict[name] = bid
  bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if bidders == "no":
    break
  else:
    clear_console()
    continue

highest_bid = 0
for bidder in new_dict:
  bid_amount = new_dict[bidder]
  if bid_amount > highest_bid:
    highest_bid = bid_amount
    winner = bidder
clear_console()
print(f"The winner is {winner} with a bid of ${highest_bid}")
