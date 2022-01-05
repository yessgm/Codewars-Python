def disemvowel(string):
    disemvowel = ""
    for char in string:
        if char not in "aeiouAEIOU":
            disemvowel += char
    return disemvowel

# ORR
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
