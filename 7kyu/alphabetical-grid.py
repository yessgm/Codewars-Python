def grid(N):
    if N < 0 : return None
    abc = 'abcdefghijklmnopqrstuvwxyz' * 8
    val = []
    for i in range(N):
        arr = list(abc[i: N+i])
        out = ' '.join(arr)
        val.append(out)
    return '\n'.join(val)
