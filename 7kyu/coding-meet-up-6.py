def is_same_language(lst): 
    languages = []
    
    for dev in lst:
        languages.append(dev['language'])
        
    return len(set(languages)) == 1