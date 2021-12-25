def string_clean(s):
    for i in range(1,10):
        if str(i) in s:
            s = s.replace(str(i), "")
    for x in s:
        if x in "~#$%^&!@*():;\"'.,? "  or x.isalpha():
            continue
        else:
            s = s.replace(x, "")
    return s
