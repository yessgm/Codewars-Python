import functools
def find_difference(a, b):
    vol1 = functools.reduce(lambda x, y: x*y, a)
    vol2 = functools.reduce(lambda x, y: x*y, b)
    return abs(vol1-vol2)
