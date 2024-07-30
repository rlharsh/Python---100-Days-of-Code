from random import shuffle

def scramble(word):
    if len(word) < 3:
        return word

    middle = list(word[1: -1])
    shuffle(middle)

    return word[0] + ''.join(middle) + word[-1]


if __name__ == '__main__':
    str_val = input("Enter a word to scramble: ")
    print(scramble(str_val))
