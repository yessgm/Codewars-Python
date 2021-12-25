def whoseMove(lastPlayer, win):
    return lastPlayer if win else 'white' if lastPlayer == 'black' else 'black'
