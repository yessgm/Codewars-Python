def each_cons(lst, n):
    megarray = []
    for i in range(len(lst)-n-1):
        megarray.append([lst[i + x] for x in range(n)])
    return megarray
