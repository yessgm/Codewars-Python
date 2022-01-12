def rpsls(pl1, pl2):
    # Your Magnificent Code here
    win_dict = {"scissors": ("paper", "lizard"),
                "paper": ("rock", "spock"),
                "rock": ("lizard", "scissors"),
                "lizard": ("spock", "paper"),
                "spock": ("scissors", "rock")}
    if pl2 in win_dict[pl1]:
        return "Player 1 Won!"
    elif pl1 in win_dict[pl2]:
        return "Player 2 Won!"
    elif pl1 == pl2:
        return "Draw!"
