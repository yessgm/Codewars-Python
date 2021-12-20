def first(seq, n=1):
    if n > len(seq):
        return seq
    return [seq[i] for i in range(n)] if n >0 else []
