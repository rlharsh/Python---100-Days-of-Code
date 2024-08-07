import random
import os
from artwork_blackjack import logo


def add_card(card_array: list) -> list:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_array.append(random.choice(cards))
    return card_array

def create_hand() -> list[int]:
    hand = []
    return add_card(add_card(hand))

def calculate_score(card_array: list) -> int:
    if sum(card_array) == 21 and len(card_array) == 2:
        return 0
    if 11 in card_array and sum(card_array) > 21:
        card_array.remove(11)
        card_array.append(1)
    return sum(card_array)


def compare(user_score, dealer_score) -> str:
    if user_score > 21 and dealer_score > 21:
        return "You went over. You lose! "
    if user_score == dealer_score:
        return "Draw!"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"


def player_wins(player_hand: list, dealer_hand: list) -> bool:
    return sum(player_hand) > sum(dealer_hand)

# Begin main game loop.
while True:
    player_score = 0
    dealer_score = 0
    player_won = False

    player_hand = create_hand()
    dealer_hand = create_hand()
    game_quit = False

    os.system("clear")
    print(logo)

    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_again != "y":
        game_quit = True
        break

    while not game_quit:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"\tYour cards: {player_hand}, current score: {player_score}")
        print(f"\tComputers first card: {dealer_hand[0]}")

        if player_score > 21:
            break

        new_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if new_card != 'y':
            break

        player_hand = add_card(card_array=player_hand)

    if game_quit:
        break

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")

    print(compare(player_score, dealer_score))

print("EXIT")
