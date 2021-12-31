def spoonerize(words):
    words = words.split(" ")
    first, second = words[0], words[1]
    char1, char2 = first[0], second[0]
    first = char2 + first[1:]
    second = char1 + second[1:]

    return first + " " + second

print(spoonerize("pop corn"))

#ORRRR

def spoonerize(words):
    a, b = words.split()
    return f"{b[0]}{a[1:]} {a[0]}{b[1:]}"
