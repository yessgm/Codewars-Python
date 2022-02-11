def riders(stations):
    riders, traveled = 1, 0
    
    for dist in stations:
        if traveled + dist > 100:
            riders += 1
            traveled = dist
        else:
            traveled += dist
    
    return riders