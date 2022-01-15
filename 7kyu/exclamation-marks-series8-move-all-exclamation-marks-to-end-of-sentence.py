def remove(s):
    num = s.count('!')
    return s.replace('!', '') + '!'*num

# OR
def remove(s):
    return s.replace('!','') + s.count('!') * '!'
