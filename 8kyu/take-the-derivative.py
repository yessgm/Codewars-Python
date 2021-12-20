def derive(coefficient, exponent):
    coeff = str(coefficient*exponent)
    exp = str(exponent-1)
    return coeff + "x^" + exp

# Or:
# def derive(coefficient, exponent):
#     return f'{coefficient * exponent}x^{exponent - 1}'
