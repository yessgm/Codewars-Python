def small_enough(array, limit):
    flag = True
    for num in array:
        if num > limit:
            return False
    return True


# ORRRR

def small_enough(array, limit):
    return max(array)<=limit
