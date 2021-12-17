def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []

    positives = 0
    sum = 0
    for i in range(len(arr)):
        if arr[i]>0:
            positives +=1
        else:
            sum += arr[i]

    return [positives, sum]

    # Alternative:
    # def count_positives_sum_negatives(arr):
    # pos = sum(1 for x in arr if x > 0)
    # neg = sum(x for x in arr if x < 0)
    # return [pos, neg] if len(arr) else []
