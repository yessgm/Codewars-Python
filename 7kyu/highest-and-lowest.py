def high_and_low(numbers):
    numbers = numbers.split(' ')
    nums = []
    for num in numbers:
        nums.append(int(num))

    return str(max(nums)) + ' ' + str(min(nums))


# Better
def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))
