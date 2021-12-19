def integrate(coefficient, exponent):
    coefficient = coefficient / (exponent+1)
    coefficient = round(coefficient)
    return "{coefficient}x^".format(coefficient = coefficient) + str(exponent+1)
