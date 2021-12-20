def multiple_of_index(arr):
    return [arr[i] for i in range(1,len(arr)) if arr[i]%i==0]
