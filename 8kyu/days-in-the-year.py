def year_days(year):
    days = 365
    if year%4 == 0:
        days = 366
    if year%100 == 0:
        days = 365
        if year%400 == 0:
            days = 366
    return f"{year} has {days} days"
