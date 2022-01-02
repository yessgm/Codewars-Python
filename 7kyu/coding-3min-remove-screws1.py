def sc(s):
    switch = 0
    if len(s) > 1:
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                switch += 1
    return len(s) + len(s) -1 + (switch*5)
