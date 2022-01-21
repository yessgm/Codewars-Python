def tennis_game_points(score):
    calls = {
        "love" : 0,
        "15" : 1,
        "30" : 2,
        "40" : 3,
    }
    p1, p2 = score.split("-")
    return calls[p1] + calls[p2] if p2 != "all" else 2*calls[p1]
