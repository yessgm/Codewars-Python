def expression_matter(a, b, c):
    sol = []
    sol.append(a * b * c)
    sol.append(a * b + c)
    sol.append(a + b + c)
    sol.append((a + b) * c)
    sol.append(a + (b * c))
    sol.append(a * (b + c))
    sol.append((a * b) + c)

    return max(sol)
