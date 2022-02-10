def maskify(cc): 
    return '#'*(len(cc)-4) + cc[-4:] if len(cc) > 4 else cc