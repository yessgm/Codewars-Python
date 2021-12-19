def two_highest(arg1):
    arg2 = []
    while arg1 != [] and len(arg2)<2:
        max_val = max(arg1)
        arg2.append(max_val)
        while max_val in arg1:
            arg1.remove(max_val)
    return arg2
