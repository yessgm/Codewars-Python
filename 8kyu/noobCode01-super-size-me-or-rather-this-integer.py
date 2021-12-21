def super_size(n):
    n_str = str(n)
    n_sorted = sorted(n_str, reverse=True)
    output_str = "" #empty string
    for num in n_sorted:
        output_str = output_str + num
    return int(output_str)
