def name_shuffler(str_):
    str = str_.split(" ")
    str[0], str[1] = str[1], str[0]
    return " ".join(str)
