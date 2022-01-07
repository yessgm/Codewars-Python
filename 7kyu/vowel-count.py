def get_count(sentence):
    return len([x for x in sentence if x in "aeiouAEIOU" ])

# ORRR

def getCount(s):
    return sum(c in 'aeiou' for c in s)
