def uni_total(s):
    sum = 0
    for i in range(len(s)):
        sum += ord(s[i])
    return sum

# def uni_total(s):
#     return sum(ord(c) for c in s)
