import math
def square_or_square_root(arr):
    squares = []
    for num in arr:
        if math.sqrt(num) == round(math.sqrt(num)):
            squares.append(math.sqrt(num))
        else:
            squares.append(num**2)
    return squares
