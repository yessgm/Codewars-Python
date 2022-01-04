def sabb(s, val, happiness):
    total = val + happiness + sum(s.count(x) for x in 'SsAaBbTtIiCcLl')
    return "Sabbatical! Boom!" if total > 22 else "Back to your desk, boy."
