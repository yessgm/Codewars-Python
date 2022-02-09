def scale(strng, k, v):
    
    if strng == '':
        return ''
    
    strng = strng.split('\n')   
    scale = []
    
    for word in strng:
        new_word = ""
        for char in word:
            new_word += char*k
        for i in range(v):
            scale.append(new_word)  
    
    return '\n'.join(scale)