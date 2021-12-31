import math
def round_it(n):
    stringy = str(n).split(".")
    if len(stringy[0]) > len(stringy[1]):
        return math.floor(n)
    elif len(stringy[0]) == len(stringy[1]):
        return round(n)
    else:
        return math.ceil(n)
