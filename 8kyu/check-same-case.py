def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    return 1 if (a.isupper() and b.isupper()) or (a.islower() and b.islower())  else 0
