def cube_sum(n, m):
    return sum([i**3 for i in range(min(n,m)+1, max(n,m)+1)])
