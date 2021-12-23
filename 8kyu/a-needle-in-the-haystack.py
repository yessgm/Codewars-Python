def find_needle(haystack):
    needle = "needle"
    if needle in haystack:
        return f"found the needle at position {haystack.index(needle)}"
