def get_number_of_squares(n):
    sumOfSqu = 0
    index = 1
    while sumOfSqu < n:
        sumOfSqu += index ** 2
        index += 1
    return index - 2
