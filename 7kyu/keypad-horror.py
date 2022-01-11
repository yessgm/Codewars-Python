def computer_to_phone(numbers):
    pairs = {
        7:1,
        8:2,
        9:3,
        4:4,
        5:5,
        6:6,
        1:7,
        2:8,
        3:9,
        0:0
    }

    telephone = ""
    for digit in numbers:
        telephone += str(pairs[int(digit)])
    return telephone
