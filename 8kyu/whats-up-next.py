def next_item(xs, item):
    it = iter(xs)
    for x in it:
        if x == item:
            break
    return next(it, None)
