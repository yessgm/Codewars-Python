def flip(d, a):
    a.sort()
    return a if d == 'R' else a[::-1]
