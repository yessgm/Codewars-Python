def longest(a1, a2):
    stringy = a1 + a2
    chars = set(list(stringy))
    print(chars)
    return "".join(sorted(chars))
