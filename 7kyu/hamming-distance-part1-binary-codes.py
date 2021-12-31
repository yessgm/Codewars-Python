def hamming_distance(a, b):
    ham = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ham += 1
    return ham
