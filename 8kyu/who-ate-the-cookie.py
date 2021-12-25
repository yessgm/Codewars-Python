def cookie(x):
    person = ""
    if type(x) == float or type(x) == int:
        person = "Monica"
    elif type(x) == str:
        person = "Zach"
    else:
        person = "the dog"
    return f"Who ate the last cookie? It was {person}!"
