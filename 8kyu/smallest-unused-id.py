def next_id(arr):
    if arr == []:
        return 0
    for i in range(max(arr)):
        if i not in arr:
            return i
    return max(arr) + 1
