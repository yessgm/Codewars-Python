def triple_trouble(one, two, three):
    triple = ""
    for i in range(len(one)):
        triple += one[i]
        triple += two[i]
        triple += three[i]
    return triple
