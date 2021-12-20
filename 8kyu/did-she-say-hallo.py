def calculate_age(birth, current):
    if birth == current:
        return "You were born this very year!"
    elif birth-current ==1:
        return "You will be born in 1 year."
    elif current < birth:
        return "You will be born in " + str(birth-current) + " years."
    elif current-birth ==1:
        return "You are 1 year old."
    else:
        return "You are " + str(current-birth) + " years old."
