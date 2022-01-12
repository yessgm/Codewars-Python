def solution(string, ending):
    len = len(ending) # get how many letters to count
    reverse = string[::-1] # reverse string
    end = reverse[:len] # get only last letters
    return end[::-1] == ending # unreverse and compare

# ORRRR

def solution(string, ending):
    return string.endswith(ending)
