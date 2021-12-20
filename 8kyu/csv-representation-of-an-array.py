def to_csv_text(array):
    string = ""
    for i in array:
        for j in i:
            string = string + (str(j)) + ","
        string = string[:-1]
        string = string + "\n"
    string = string[:-1]
    return string
