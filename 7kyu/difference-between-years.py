def how_many_years (date1,date2):
    year1 = int(date1[:4])
    year2 = int(date2[:4])
    return abs(year2 - year1)
