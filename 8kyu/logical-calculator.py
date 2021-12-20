def logical_calc(array, op):
    logical = {
        "AND" : lambda a,b: a and b,
        "OR" : lambda a,b: a or b,
        "XOR" : lambda a,b: a != b
    }
    bool = True
    for i in range(len(array)-1):
        bool = logical[op](array[i], array[i+1])
    return bool
