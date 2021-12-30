def each_cons(lst, n):
    mas = []
    for i in range(len(lst)-n+1):
        mas.append(lst[i:i+n])
    return mas
