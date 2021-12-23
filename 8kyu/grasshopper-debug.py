def weather_info(temp):
    c = convert(temp)
    if (c > 0):
        return (str(c) + " is above freezing temperature")
    else:
        return (str(c) + " is freezing temperature")

def convert(temperature):
    celsius = (temperature - 32) * (5/9)
    return celsius
