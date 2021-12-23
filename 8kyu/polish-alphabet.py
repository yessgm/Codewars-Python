def correct_polish_letters(st):
    translation = ""
    diacritics = {
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ź": "z",
        "ż": "z"
    }
    for i in st:
        if i in diacritics:
            translation += diacritics[i]
        else:
            translation += i
    return translation
