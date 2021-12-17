def abbrev_name(name):
    name = name.upper()
    print(name)
    first = name[0]
    i = 0
    while name[i] != ' ':
        i += 1
    last = name[i+1]
    return first + '.' + last

    # more efficient way:
    # def abbrevName(name):
    # return '.'.join(w[0] for w in name.split()).upper()
