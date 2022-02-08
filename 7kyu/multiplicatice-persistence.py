def per(n):
    
    mult = []
    
    while len(str(n))>1:
        prod = 1    
        for d in str(n):
            prod*=int(d)
        mult.append(prod)
        n = prod
    
    return mult