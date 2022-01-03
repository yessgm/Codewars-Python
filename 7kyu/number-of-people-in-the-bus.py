def number(bus_stops):
    ppl_left = 0
    for stop in bus_stops:
        ppl_left += stop[0]
        ppl_left -= stop[1]
    return ppl_left
