def find_short(s):
    counts = [len(word) for word in s.split()]
    return min(counts)