points = {'kata': 5, 'Petes kata': 10, 'life': 0, 'eating': 1}

def paul(x):
    score = sum(map(points.get, x))
    return (
        'Super happy!' if score < 40 else
        'Happy!' if score < 70 else
        'Sad!' if score < 100 else
        'Miserable!'
    )

# And....
def paul(x):
    points = {'life': 0, 'eating': 1, 'kata': 5, 'Petes kata': 10}
    misery = sum(map(points.get, x))
    return ['Miserable!', 'Sad!', 'Happy!', 'Super happy!']\
            [(misery<40)+(misery<70)+(misery<100)]
