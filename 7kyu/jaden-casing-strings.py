def to_jaden_case(string):
    words = string.split(' ')
    return ' '.join(word[0].upper()+word[1:] for word in words)