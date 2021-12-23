def is_opposite(s1,s2):
    if s1 == "" or s2 == "":
        return False
    for i in range(len(s1)):
        if s1[i].isupper() == s2[i].isupper():
            return False
    return True
