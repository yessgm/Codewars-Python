def noonerize(numbers):
    try:
        n1, n2 = str(numbers[0]), str(numbers[1])
        n1, n2 = f"{n2[0]}{n1[1:]}", f"{n1[0]}{n2[1:]}"
        n1, n2 = int(n1), int(n2)
        return abs(n1-n2)
    except:
        return "invalid array"
