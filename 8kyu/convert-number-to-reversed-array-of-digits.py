def digitize(n):
    n = str(n)
    n.split()
    n = n[::-1]
    return [int(n[i]) for i in range(len(n))]

# Faster:
# def digitize(n):
#     return [int(x) for x in str(n)[::-1]]
