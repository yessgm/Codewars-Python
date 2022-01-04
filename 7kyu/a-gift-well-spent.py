def buy(x,arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == x:
                return [i, j]
    return None
