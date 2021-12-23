def array_madness(a,b):
    sum_squ = 0
    sum_cub = 0
    for x in a:
        sum_squ += x**2
    for y in b:
        sum_cub += y**3
    return sum_squ > sum_cub

# Faster:
# def array_madness(a,b):
    # return sum(x ** 2 for x in a) > sum(x **3 for x in b)
