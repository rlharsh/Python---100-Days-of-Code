import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

def generate_password(password_length):
    generated_password = ""
    for x in range(password_length):
        char_type = random.getrandbits(2)
        if char_type == 0:
            char = random.choice(alphabet)
            upper = random.getrandbits(1)
            if upper:
                char = char.upper()
            generated_password += char
        elif char_type == 1:
            char = random.choice(numbers)
            generated_password += str(char)
        elif char_type == 2:
            char = random.choice(symbols)
            generated_password += char

    print(generated_password)


if __name__ == '__main__':
    while True:
        try:
            password_length = int(input("Please enter a length of a password to generate: "))
            generate_password(password_length)
            break
        except ValueError:
            print("Enter a valid number.")
