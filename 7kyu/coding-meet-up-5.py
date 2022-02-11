def count_languages(lst): 
    language = [el['language'] for el in lst]
    return {i: language.count(i) for i in language}