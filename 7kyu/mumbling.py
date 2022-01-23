def accum(s):

    letters = []

    for i in range(len(s)):
        letters.append(s[i].upper() + s[i].lower()*i)

    return '-'.join(letters)


# Faster
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
