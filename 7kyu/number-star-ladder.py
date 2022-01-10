def pattern(n):
    ladder = "1\n"
    for i in range(1,n):
        ladder += "1" + "*"*i + f"{i+1}" + "\n"
    return ladder[0:-1]
