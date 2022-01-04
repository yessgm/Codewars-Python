def pair_zeros(arr):
    zeroCount = 0
    newArr = []
    for i in range(len(arr)):
        if arr[i] == 0:
            zeroCount += 1
            if zeroCount%2 == 1 :
                newArr.append(arr[i])
        else:
            newArr.append(arr[i])

    return newArr
