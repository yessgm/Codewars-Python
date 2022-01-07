def square_digits(num):
    num = str(num)
    squared = ""
    for digit in num:
        squared += str(int(digit)**2)
    return int(squared)
