def fold_to(distance):
    folds = 0
    thick = 0.0001
    while thick < distance:
        thick *= 2
        folds += 1
    return folds if distance >= 0 else None
