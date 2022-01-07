def solve(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] in new_arr:
            new_arr.remove(arr[i])
            new_arr.append(arr[i])
        else:
            new_arr.append(arr[i])
    return new_arr
