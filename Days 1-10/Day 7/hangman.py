import random
from hangman_words import word_list
from hangman_art import stages, logo

CHOSEN_WORD = random.choice(word_list)
WORD_LENGTH = len(CHOSEN_WORD)
lives = 6

display = []
for _ in range(WORD_LENGTH):
    display.append('_')

end_of_game = False

print(logo)

while not end_of_game:
    guess = input("Please input a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    for position in range(WORD_LENGTH):
        letter = CHOSEN_WORD[position]
        if letter == guess:
            display[position] = letter

    if not guess in CHOSEN_WORD:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You have lost, the correct word was {CHOSEN_WORD}.")

    if lives == 0:
        end_of_game = True

    print(stages[lives])
    print("".join(display))

    if "_" not in display:
        end_of_game = True
