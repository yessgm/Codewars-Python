def is_vow(inp):
    vowels = {
        97: "a",
        101: "e",
        105: "i",
        111: "o",
        117: "u"
    }
    for i in range(len(inp)):
        if inp[i] in vowels.keys():
            inp[i] = vowels[inp[i]]
    return inp

# More efficiently:
# def is_vow(inp):
#     return [chr(n) if chr(n) in "aeiou" else n for n in inp]
