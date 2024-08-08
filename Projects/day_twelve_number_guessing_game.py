import random
import os

# Constants
NUMBERS = [x for x in range(1, 101)]

# Globals
system_selected_number = -1
system_game_running = False
player_current_lives = -1
player_current_guess = -1
player_difficulty_selected = False
player_current_difficulty = 'hard'

def get_random_number() -> int:
    return random.choice(NUMBERS)

def get_player_guess() -> int:
    """
    get_player_guess Receives and processes input from the player.


    Returns:
        int: The integer value received from the player 1-100
    """
    while True:
        try:
            guess = int(input("Make a guess: "))
            if guess > 0 and guess <= 100:
                return guess
            else:
                print("You must select a valid number from 1-100")
                get_player_guess()
        except ValueError:
            print("You must select a valid number from 1-100")


def process_player_guess(guess: int) -> int:
    """
    process_player_guess Processes a number given by the player, and notifies of results.

    Args:
        guess (int): The integer given by the player.

    Returns:
        int: The new number of lives the player has.
    """
    global system_selected_number

    if guess < system_selected_number:
        print("Too low.")
        return player_current_lives - 1
    elif guess > system_selected_number:
        print("Too high.")
        return player_current_lives - 1
    elif guess == system_selected_number:
        print(f"You got it! The answer was {system_selected_number}.")

while True:
    os.system("clear")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    while not player_difficulty_selected:
        difficulty_choice = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty_choice == "easy" or difficulty_choice == "hard":
            player_current_difficulty = difficulty_choice
            player_difficulty_selected = True  ## player has chosen a difficulty

            # set the lives of the player.
            if player_current_difficulty == "easy":
                player_current_lives = 10
            else:
                player_current_lives = 5
            break

    # set the game to running
    system_game_running = True

    # set the current number
    system_selected_number = get_random_number()

    while system_game_running:
        # game start banner
        print(f"You have {player_current_lives} attempts remaining to guess the number.")

        # get the player guess
        player_current_guess = get_player_guess()

        # process the player guess
        player_current_lives = process_player_guess(player_current_guess)

        # verify if the game is over
        if player_current_guess == system_selected_number or player_current_lives <= 0:
            system_game_running = False

    # trap the break
    if not system_game_running:
        play_again = input("Would you like to play again 'yes' or 'no': ").lower()
        if play_again != 'yes':
            break
        else:
            system_selected_number = -1
            system_game_running = False
            player_current_lives = -1
            player_current_guess = -1
            player_difficulty_selected = False
            player_current_difficulty = 'hard'
