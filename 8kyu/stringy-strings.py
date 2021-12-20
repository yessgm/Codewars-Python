def stringy(size):
    stringy = ''
    for i in range(size):
        if i%2 == 0:
            stringy = stringy + "1"
        else:
            stringy = stringy + "0"
    return stringy
