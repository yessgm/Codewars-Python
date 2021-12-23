def stairs_in_20(stairs):
    total = 0
    for x in stairs:
        for y in x:
            total += y
    return total * 20
