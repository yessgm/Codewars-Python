def remove(s):
    if s == "":
        return s
    return s[:-1] if s[-1] == "!" else s

def remove(s):
    return s[:-1] if s.endswith('!') else s
