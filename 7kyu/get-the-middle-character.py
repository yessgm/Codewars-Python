def get_middle(s):
    a = len(s)
    if len(s) == 1:
        return s
    elif len(s) % 2 == 0:
        return s[int(a/2) - 1] + s[int(a/2)]
    else:
        return s[int(a/2)]
