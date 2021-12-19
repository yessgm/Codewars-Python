def enough(cap, on, wait):
    if on + wait <= cap:
        return 0
    return on + wait - cap

# Alternatively:
# def enough(cap, on, wait):
#     return wait + on - cap if wait + on > cap else 0
