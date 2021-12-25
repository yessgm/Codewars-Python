def contamination(text, char):
    if text == "" or char == "":
        return ""
    bug = ""
    for x in text:
        bug += char
    return bug
