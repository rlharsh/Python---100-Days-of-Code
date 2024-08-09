import os
from random import choice
from art import logo, vs
from game_data import data

def format_data(account: dict) -> str:
    celeb_name = account["name"]
    celeb_desc = account["description"]
    celeb_coun = account["country"]

    return(f"{celeb_name}, a {celeb_desc}, from {celeb_coun}")

def check_answer(user_guess: str, a_followers: int, b_followers: int) -> bool:
    if user_guess == "a":
        return a_followers > b_followers
    elif user_guess == "b":
        return b_followers > a_followers

# Setup variables
game_running = True
player_score = 0
account_a = None
account_b = choice(data)

# Display game heading
os.system("clear")
print(logo)

while game_running:

    # Setup revolving choices
    account_a = account_b
    account_b = choice(data)

    if account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_data(account=account_a)}.")
    print(f"{vs}")
    print(f"Against B: {format_data(account=account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    user_correct = check_answer(user_guess=guess, a_followers=account_a["follower_count"], b_followers=account_b["follower_count"])
    if user_correct:
        player_score += 1
        print(f"You're right! Current score {player_score}.")
    else:
        game_running = False

print(f"Total guessed correct {player_score}.")
