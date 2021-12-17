def how_much_i_love_you(nb_petals):
    if nb_petals%6 == 5:
        return "madly"
    if nb_petals%6 == 4:
        return "passionately"
    if nb_petals%6 == 3:
        return "a lot"
    if nb_petals%6 == 2:
        return "a little"
    if nb_petals%6 == 1:
        return "I love you"
    if nb_petals%6 == 0:
        return "not at all"

    # Faster solution:

    # def how_much_i_love_you(nb_petals):
    # words = {1: 'I love you', 2: 'a little', 3: 'a lot', 4: 'passionately',
    #         5: 'madly', 0: 'not at all'}
    # return words[nb_petals%6]
