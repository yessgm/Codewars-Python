def isValid(formula):
    if (1 in formula and 2 in formula) or (3 in formula and 4 in formula):
        return False
    if (5 in formula and 6 not in formula) or (5 not in formula and 6 in formula):
        return False
    if 7 not in formula and 8 not in formula:
        return False
    return True
