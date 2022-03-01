def to_time(seconds):
    hr = seconds//3600
    min = (seconds%3600)//60
    return f'{hr} hour(s) and {min} minute(s)'