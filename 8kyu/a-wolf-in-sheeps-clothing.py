def warn_the_sheep(queue):
    queue.reverse()
    the_wolf_position = queue.index("wolf")
    if the_wolf_position == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        return "Oi! Sheep number " + str(the_wolf_position) + "! You are about to be eaten by a wolf!"
