def prev_mult_of_three(n):
    num = str(n)

    if int(num)>4:
        while int(num)%3 != 0:
            num = num[:len(num)-1]
            if num == '':
                return None

    return int(num) if int(num) >= 3 else None
