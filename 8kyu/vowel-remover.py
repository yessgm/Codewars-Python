def shortcut( s ):
    vowels = ["a", "e", "i", "o", "u"]
    s2 = ""
    for i in range(len(s)):
        if s[i] not in vowels:
            s2 = s2 + s[i]
    return s2


# Better:

# def shortcut(s):
#     return ''.join(c for c in s if c not in 'aeiou')
