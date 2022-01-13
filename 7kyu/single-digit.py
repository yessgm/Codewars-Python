def single_digit(n):
    binary = bin(n)[2:]
    sum = binary.count('1')
    while len(str(sum)) != 1:
        binary = bin(sum)[2:]
        sum = binary.count('1')
    return sum if len(str(n)) != 1 else n

# Better:

def single_digit(n):
    while n > 9:
        n = bin(n).count("1")
    return n
