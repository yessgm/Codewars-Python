def explode(s):
    new_s = ""
    for num in s:
        new_s += num * int(num)
    return new_s

# Or One line:

def explode(s):
    return ''.join(c * int(c) for c in s)
