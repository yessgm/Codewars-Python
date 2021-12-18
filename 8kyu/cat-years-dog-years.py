def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [human_years, 15, 15]
    elif human_years == 2:
        return [human_years, 24, 24]
    return [human_years, 24 + (human_years-2)*4, 24 + (human_years-2)*5]
