def DNA_strand(dna):
    dna_pair = {
        "A":"T",
        "T":"A",
        "C":"G",
        "G":"C"
    }
    return "".join((map(lambda c: dna_pair[c], dna)))
