def is_isogram(string):

    unique = ''

    for char in string:
        if char.lower() in unique:
            return False
        else:
            unique += char.lower()

    return True
