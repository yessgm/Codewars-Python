import math
def square_area(A):
    # arc length in radians is pi0
    radius = A / math.pi
    return round((radius**2)*4, 2)
