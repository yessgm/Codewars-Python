units = {"kg": 1, "g": 1e-3, "mg": 1e-6, "μg": 1e-9, "lb": 0.453592,
         "m": 1, "cm": 1e-2, "mm": 1e-3, "μm": 1e-6, "ft": 0.3048,
         "G": 6.67e-11}

def solution(v, u):
    m1, m2, r = (v[i] * units[u[i]] for i in range(3))
    return units["G"] * m1 * m2 / r**2
