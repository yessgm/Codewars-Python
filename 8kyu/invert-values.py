def invert(lst):
    inverted = [lst[i] * -1 for i in range(len(lst))]
    return inverted

# Better way:
# def invert(lst):
#    return [-x for x in lst]
