alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, method=True):
    """caesar Either encrypts or decrypts a user message.

    Args:
        text (string): The message to be encrypted or decrypted.
        shift (integer): The amount of characters to shift message by.
        method (bool, optional): True for encrypt, False to decrypt. Defaults to True.
    """
    output_string = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = 0
            if method:
                new_index = (index + shift) % len(alphabet)
            else:
                new_index = (index - shift) % len(alphabet)
            output_string += alphabet[new_index]
        else:
            output_string += letter

    print(f"The text is equal to {output_string}.")

text = ""
shift = 0
while True:
    user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'quit' to quit:\n").lower()

    if user_choice.startswith('e') or user_choice.startswith('d'):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text=text, shift=shift, method=user_choice.startswith('e'))
    elif user_choice.startswith('q'):
        break
    else:
        print("Select a valid option.")
