def incrementer(nums):
    index = 1
    new_nums = []
    for x in nums:
        if x + index < 10:
            new_nums.append(x + index)
        else:
            new_nums.append((x + index)%10)
        index += 1
    return new_nums


# ORRR

def incrementer(nums):
    return [(n + i) % 10 for i, n in enumerate(nums, 1)]
