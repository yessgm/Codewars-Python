def collision(x1, y1, radius1, x2, y2, radius2):
    distance = (((x2-x1)**2) + ((y2-y1)**2))**0.5
    return distance <= radius1 + radius2
