geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    no_goose = []
    for i in range(len(birds)):
        if birds[i] not in geese:
            no_goose.append(birds[i])
    return no_goose

# Better:
# geese = {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}
#
# def goose_filter(birds):
#     return [bird for bird in birds if bird not in geese]
