def red_knight(N, P):
    knightX = 0
    knightY = N

    while knightX != P:
        knightX += 2
        P += 1
        if knightY == 0:
            knightY = 1
        else:
            knightY = 0

    return ('White', knightX) if knightY == 0 else ('Black', knightX)
