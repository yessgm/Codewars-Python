def char_freq(message):
    letters = {}
    for x in message:
        if x not in letters:
            letters[x] = message.count(x)
    return letters
