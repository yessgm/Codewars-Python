def max_redigit(num):
    if num >= 100 and num < 1000:
        stringy = sorted(list(str(num)), reverse = True)
        return int("".join(stringy))
    else:
        return None
