def no_boring_zeros(n):
    if n == 0:
        return n
    n = str(n)
    while n[-1] == '0':
        n = n[:-1]
    return int(n)
