def multi_table(number):
    table = []
    for i in range(1, 11):
        table.append(str(i) + " * " + str(number) + " = "+ str(i*number))
    return "\n".join(table)
        
