def first_non_consecutive(arr):
    non_con = 0
    for i in range(len(arr)-1):
        if arr[i]+1 != arr[i+1]:
            return arr[i+1]
    return None
