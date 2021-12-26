def bar_triang(pointA, pointB, pointC):
    xO = round(((pointA[0] + pointB[0] + pointC[0])/3), 4)
    yO = round((pointA[1] + pointB[1] + pointC[1])/3, 4)
    return [xO, yO] 
