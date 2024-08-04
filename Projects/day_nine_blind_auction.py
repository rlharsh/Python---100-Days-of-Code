import os
from auction_art import logo as art

os.system("clearRonald")
current_bids = {}
print(art)

while True:
    print("Welcome to the secret auction program.")
    user_name = input("What is your name?: ")
    user_bids = int(input("What is your bid?: $"))

    current_bids[user_name] = user_bids
    continue_application = input("Are there other users who wish to bid (y/n)?: ").lower()
    if continue_application == "n":
        break
    os.system("clear")

current_winner = {}
current_winning_bid = 0
for key in current_bids:
    if current_bids[key] > current_winning_bid:
        current_winning_bid = current_bids[key]
        current_winner = {
            "winner": key,
            "amount": current_bids[key]
        }

print(f"The winner is {current_winner["winner"]} with a bid of ${current_winner["amount"]}.")
