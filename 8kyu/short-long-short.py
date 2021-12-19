def solution(a, b):
    return a+b+a if len(b) > len(a) else b+a+b
