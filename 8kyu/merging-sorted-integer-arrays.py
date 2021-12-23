def merge_arrays(first, second):
    third = []
    for i in first:
        if i not in third:
            third.append(i)
    for i in second:
        if i not in third:
            third.append(i)
    return sorted(third)

def merge_arrays(a, b):
    return sorted(set(a + b))
