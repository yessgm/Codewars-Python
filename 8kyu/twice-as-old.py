def twice_as_old(dad_years_old, son_years_old):
    son = son_years_old
    dad = dad_years_old
    years = 0

    if son_years_old > (dad_years_old/2):
        while son != (dad/2):
            son -= 1
            dad -= 1
            years +=1
    else:
        while son != (dad/2):
            son += 1
            dad += 1
            years +=1

# Much faster solution:
# def twice_as_old(dad_years_old, son_years_old):
#     return abs(dad_years_old - 2*son_years_old)
