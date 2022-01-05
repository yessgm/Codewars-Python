def pyramid(balls):
    levels = 0
    balls_needed = 0
    while balls > balls_needed:
        levels += 1
        balls_needed += 1
        balls -= balls_needed
    return levels
