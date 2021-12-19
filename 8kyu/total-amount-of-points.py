def points(games):
    points = 0
    for x in games:
        if int(x[0]) > int(x[2]):
            points += 3
        elif int(x[0]) == int(x[2]):
            points +=1
    return points
            
