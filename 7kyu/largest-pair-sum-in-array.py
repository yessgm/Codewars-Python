def largest_pair_sum(numbers):
    numbers = sorted(numbers)
    return numbers[-1] + numbers[-2]
