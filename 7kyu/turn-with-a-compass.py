def direction(facing, turn):
    compass = {'N':0, 'NE':45, 'E':90, 'SE':135, 'S':180, 'SW':225, 'W':270, 'NW':315}
    
    start = compass[facing]
    end = start + turn
    direction = ''
    
    if end >= 360:
        while end >= 360:
            end -= 360
    elif end < 0: 
        while end < 0:
            end += 360
            
    for key, value in compass.items():
        if end == value:
            return key

#ORRRR

DIRECTIONS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

def direction(facing, turn):
    return DIRECTIONS[(turn // 45 + DIRECTIONS.index(facing)) % 8]