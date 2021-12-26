def lowercase_count(strng):
    lower = 0
    for x in strng:
        if x.islower():
            lower += 1
    return lower
