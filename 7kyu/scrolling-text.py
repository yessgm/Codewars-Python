def scrolling_text(text):
    text = text.upper()
    return [ text[i:] + text[:i] for i in range(len(text)) ]
