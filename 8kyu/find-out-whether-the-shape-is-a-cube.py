import math
def cube_checker(volume, side):
    if volume <= 0 or side <= 0:
        return False
    check = math.sqrt(volume/side)
    return check - round(check) == 0
