def remove_consecutive_duplicates(s):
    s = s.split()
    l = len(s)-1
    while l > 0:
        if s[l] == s[l-1]:
            s.pop(l)
        l -= 1

    return ' '.join(s)
