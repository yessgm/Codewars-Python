def get_number_from_string(string):
    numbers = ""
    for x in string:
        if x.isnumeric():
            numbers += x
    return int(numbers)
