def find_longest(str):
    spl = str.split(" ")
    longest = 0

    for x in spl:
        if len(x) > longest:
            longest = len(x)
    return longest
