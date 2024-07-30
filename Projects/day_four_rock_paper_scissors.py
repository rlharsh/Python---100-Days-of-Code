import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
game_winner_choices = ["Tie Game", "CPU Wins", "Player Wins", "Invalid Argument"]
user_choice = input("[R]ock, [P]aper, [S]cissors: ").lower()
user_choice_map = { "rock": 0, "paper": 1, "scissors": 2}
comp_choice = random.randint(0, 2)
game_winner = -1

if (user_choice == "rock"):
    if (comp_choice == 0):
        game_winner = 0
    elif (comp_choice == 1):
        game_winner = 1
    else:
        game_winner = 2
elif (user_choice == "paper"):
    if (comp_choice == 0):
        game_winner = 2
    elif (comp_choice == 1):
        game_winner = 0
    else:
        game_winner = 1
elif (user_choice == "scissors"):
    if (comp_choice == 0):
        game_winner = 1
    elif (comp_choice == 1):
        game_winner = 2
    else:
        game_winner = 0
else:
    game_winner = 3

if (game_winner != 3):
    print(f"Player chooses:\n{game_images[user_choice_map[user_choice]]}")
    print(f"CPU chooses:\n{game_images[comp_choice]}")
    print(f"{game_winner_choices[game_winner]}")
else:
    print(f"Error: {game_winner_choices[3]}")
