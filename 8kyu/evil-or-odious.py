def evil(n):
    binary = bin(n)[2:]
    ones = binary.count("1")
    return "It's Evil!" if ones%2==0 else "It's Odious!"
