def animals(heads, legs):
    chickens = heads * 2 - legs / 2
    cows = heads - chickens
    if chickens < 0 or cows < 0 or chickens != int(chickens):
        return "No solutions"
    return (chickens, cows)
