import random

def play_game():
    player_attempts = 0
    cpu_number = random.randint(1, 100)
    while True:
        try:
            user_choice = int(input("Please enter a number between 1-100: "))
            if user_choice < 1 or user_choice > 100:
                print("Please enter a number within the valid range (1-100).")

            player_attempts += 1

            if (user_choice == cpu_number):
                print(f"Congratulations! You've guessed the number in {player_attempts} attempts.")
                break
            elif user_choice > cpu_number:
                print("Too high. Try again")
            else:
                print("Too low. Try again")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play_again():
    return input("Would you like to play again (y/n): ").lower().startswith('y')


if __name__ == '__main__':
    while True:
        play_game()
        if not play_again():
            print("Thanks for playing")
            break
