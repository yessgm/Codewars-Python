def wrap(height, width, length):
    a, b, c = sorted([height, width, length])
    return 4*a + 2*c + 2*b + 20
