LINES = "{0} of beer on the wall, {0} of beer.\nTake one down and pass it around, {1} of beer on the wall."
SONG = '\n'.join( LINES.format("{} bottles".format(n), "{} bottle".format(n-1)+"s"*(n!=2)) for n in range(99,1,-1) )
SONG += """
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall."""

def HQ9(code):
    return {'H': 'Hello World!', 'Q': 'Q', '9': SONG}.get(code, None)
