def sum_array(arr=[]):
    if arr == None:
        return 0
    if  arr == [] or len(arr) < 3:
        return 0
    return sum(sorted(arr)[1:len(arr)-1])
