def comes_after(st, l):
    after = ''

    for i in range(len(st)-1):
        if st[i].lower() == l.lower() and st[i+1].isalpha():
            after += st[i+1]

    return after
