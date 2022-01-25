def sum_of_minimums(numbers):
    sum = 0
    for arr in numbers:
        sum += min(arr)
    return sum
