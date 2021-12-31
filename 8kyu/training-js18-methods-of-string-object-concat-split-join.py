def split_and_merge(string, separator):
    chars = list(string)
    joined = separator.join(chars)

    return joined.replace(f" {separator}", " ").replace(f"{separator} ", " ")
