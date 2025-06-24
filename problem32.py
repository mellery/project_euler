def is_pandigital(a, b, c):
    """Check if a, b, c together use digits 1-9 exactly once"""
    digits = str(a) + str(b) + str(c)
    return len(digits) == 9 and set(digits) == set('123456789')

prods = set()

# Case 1: 1-digit × 4-digit = 4-digit (e.g., 2 × 1963 = 3926)
for a in range(1, 10):
    for b in range(1000, 10000):
        c = a * b
        if c >= 10000:
            break
        if is_pandigital(a, b, c):
            prods.add(c)

# Case 2: 2-digit × 3-digit = 4-digit (e.g., 39 × 186 = 7254)
for a in range(10, 100):
    for b in range(100, 1000):
        c = a * b
        if c >= 10000:
            break
        if is_pandigital(a, b, c):
            prods.add(c)

print(sum(prods))
    
