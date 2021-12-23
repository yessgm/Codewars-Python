def elevator(left, right, call):
    if abs(left-call) < abs(right-call):
        return "left"
    if abs(left-call) > abs(right-call) or abs(left-call) == abs(right-call):
        return "right"
