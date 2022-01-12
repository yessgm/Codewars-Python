def baby_shark_lyrics():
    n = ['Baby shark','Mommy shark','Daddy shark', 'Grandma shark', 'Grandpa shark', "Let's go hunt"]
    c = ''
    for i in n:
        c += (f"{i}, doo doo doo doo doo doo\n")*3 + f'{i}!\n'
    return c + 'Run away,…'
