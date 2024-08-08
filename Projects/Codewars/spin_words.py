def spin_words(sentence):

    return " ".join([x[::-1] if len(x) >=5 else x for x in sentence.split(" ")])


    words = sentence.split()
    result = []
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)

print(spin_words("Hi! to CodeWars"))
