def to_freud(sentence):
    if sentence == "":
        return ""
    words = len(sentence.split(" "))
    new_sentence = ["sex"]*words
    return " ".join(new_sentence)
