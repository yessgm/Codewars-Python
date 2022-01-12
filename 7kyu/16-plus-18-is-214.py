def add(num1, num2):
    if num1 > num2:
        num2 = str(num2).zfill(len(str(num1)))
        num1 = str(num1)
    else:
        num1 = str(num1).zfill(len((str(num2))))
        num2 = str(num2)
    return int(''.join([str(int(num1[i]) + int(num2[j])) for i in range(len(num1)) for j in range(len(num2)) if i == j]))
