def determine_time(arr):
    time = 0
    for stop in arr:
        time += int(stop[0:2]) + (float(stop[3:5])/60) + (float(stop[6:8])/3600)
    return True if time <= 24 else False
