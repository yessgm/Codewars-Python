def count_sheep(n):
    counting = ""
    if n == 0:
        return counting
    for i in range(n):
        counting += str(i+1) + " sheep..."
    return counting
