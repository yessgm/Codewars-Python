def descending_order(num):

    numbers = []

    for digit in str(num):
        numbers.append(digit)

    return int(''.join(sorted(numbers, reverse=True)))
