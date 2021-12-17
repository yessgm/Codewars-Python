def square_sum(numbers):
    squares = [numbers[i]**2 for i in range(len(numbers))]
    return sum(squares)

# Faster:
# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)
