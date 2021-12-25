def add_length(str):
    str = str.split(' ')
    length = [None] * len(str)
    index = 0
    for x in str:
        length[index] = x + f" {len(x)}"
        index += 1
    return length
