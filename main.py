from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

name = input("What is your name?: ")
bid = input("What's your bid'?: $")

bidders = {}

def new_bidder():
  bidders[name] = bid

other_bidders = input("Are there any other bidders'? Type 'yes' or 'no'.\n")

while other_bidders == "yes":
  new_bidder()
  clear()
  name = input("What is your name?: ")
  bid = input("What's your bid'?: $")
  other_bidders = input("Are there any other bidders'? Type 'yes' or 'no'.\n")
if other_bidders == "no":
  other_bidders = "no"
  clear()
  new_bidder()
  winner_bid = 0
  winner = ""
  for key in bidders:
    if int(bidders[key]) > winner_bid:
      winner_bid = int(bidders[key])
      winner = key
  print(f"The winner is {winner} with a bid of {winner_bid}.")