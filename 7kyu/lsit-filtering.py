def filter_list(l):
    nums = []
    for item in l:
        if type(item) == int:
            nums.append(item)

    return nums
