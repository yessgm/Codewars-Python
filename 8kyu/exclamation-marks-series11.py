def replace_exclamation(s):
    for x in s:
        if x in "aeiouAEIOU":
            s = s.replace(x, "!")
    return s
