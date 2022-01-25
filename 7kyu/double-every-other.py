def double_every_other(lst):
    return [lst[i]*2 if i%2==1 else lst[i] for i in range(len(lst))]
