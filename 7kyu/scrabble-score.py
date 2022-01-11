def scrabble_score(st):
    st = st.upper()
    score = 0
    points = {
        0 : [""],
        1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2 : ["D", "G"],
        3 : ["B", "C", "M", "P"],
        4 : ["F", "H", "V", "W", "Y"],
        5 : ["K"],
        8 : ["J", "X"],
        10 : ["Q", "Z"]
    }

    for key, value in points.items():
        for char in value:
            for letter in st:
                if letter == char:
                    score += key
    return score

## Original Plan but didn't know syntax:
def scrabble_score(st): 
    values = {
        **dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1),
        **dict.fromkeys(['D', 'G'], 2),
        **dict.fromkeys(['B', 'C', 'M', 'P'], 3),
        **dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4),
        **dict.fromkeys(['K'], 5),
        **dict.fromkeys(['J', 'X'], 8),
        **dict.fromkeys(['Q', 'Z'], 10)}

    score = 0

    for char in st:
        score += values.get(char.upper(), 0)

    return score
