def sum_triangular_numbers(n):
    total, a = 0,0
    for i in range(n):
        a += i+1
        total += a
    return total
    
