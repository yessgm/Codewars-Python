def ones_complement(binary_number):
    complement = {'1':'0', '0':'1'}
    comp = ''
    
    for n in binary_number:
        comp += complement[n]

    return comp