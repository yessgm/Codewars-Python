def divisible_by(numbers, divisor):
    divisors = []
    for i in numbers:
        if i%divisor==0:
            divisors.append(i)
    return divisors
