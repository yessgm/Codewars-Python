def duplicate_elements(m, n):
    flag = False
    for num in m:
        if num in n:
            flag = True
    return flag


# ORRR

def duplicate_elements(m, n):
    return bool(set(m).intersection(n))
