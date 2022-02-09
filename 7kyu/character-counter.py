def validate_word(word):
    word = word.lower()
    occ = word.count(word[0])
    for c in word:
        if word.count(c) != occ:
            return False
    return True