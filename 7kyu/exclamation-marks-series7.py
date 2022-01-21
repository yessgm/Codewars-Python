def remove(s):
    stringy = s.split(' ')
    new_s = []
    for hi in stringy:
        if hi.count('!')!=1:
            new_s.append(hi)

    return ' '.join(new_s)
