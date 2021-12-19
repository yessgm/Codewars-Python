def is_uppercase(inp):
    bool = False
    for x in inp:
        if x.isalpha():
            bool = True
            return  inp.isupper()
    return True
