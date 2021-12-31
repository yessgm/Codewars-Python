def pillars(num_pill, dist, width):
    return dist * 100 * (num_pill - 1) + width * (num_pill - 2) * (num_pill > 1)
