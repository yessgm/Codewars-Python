def find_multiples(integer, limit):
    multiples = []
    for i in range(integer, limit+1, integer):
        multiples.append(i)
    return multiples

# Or:
# def find_multiples(integer, limit):
#     return list(range(integer, limit+1, integer))
