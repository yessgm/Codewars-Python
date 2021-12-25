import functools
def calculator(x,y,op):
    if type(x) != int or type(y) != int:
        return "unknown value"

    operations = {
        '+' : lambda a,b: a + b,
        '-' : lambda a,b: a - b,
        '*' : lambda a,b: a * b,
        '/' : lambda a,b: a / b
    }
    return operations[op](x,y) if op in operations else "unknown value"
