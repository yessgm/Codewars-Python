def merge_arrays(arr1, arr2):
    arr = sorted(arr1 + arr2)
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr

# OR:
# def merge_arrays(arr1, arr2):
#     return sorted(set(arr1+arr2))
