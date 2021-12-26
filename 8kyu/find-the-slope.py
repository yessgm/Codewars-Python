def find_slope(points):
    while points[2] - points[0] != 0:
        slope = round((points[3]-points[1])/(points[2]-points[0]))
        return str(slope)
    return "undefined"
