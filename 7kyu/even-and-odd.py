def even_and_odd(n):
    NE = ""
    NO = ""
    
    for d in str(n):
        if int(d)%2 == 0:
            NE += d
        else:
            NO += d
    
    if NE == "":
        NE = 0
    if NO == "":
        NO = 0
    
    return (int(NE), int(NO))