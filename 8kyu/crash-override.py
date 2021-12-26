def alias_gen(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    while f_name[0] in FIRST_NAME and l_name[0] in SURNAME:
        return f"{FIRST_NAME[f_name[0]]} {SURNAME[l_name[0]]}"
    return "Your name must start with a letter from A - Z."
