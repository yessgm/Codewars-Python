def remove(s):
    while s[-1] == "!":
        s = s[:len(s)-1:]
    return s
