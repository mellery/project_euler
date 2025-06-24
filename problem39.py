import math

def count_right_triangles(p):
    """Count integer right triangles with perimeter p"""
    count = 0
    # For a + b + c = p and a² + b² = c²
    # Substitute c = p - a - b into a² + b² = c²
    # This gives: a² + b² = (p - a - b)²
    # Simplifying: 2ab = p² - 2p(a + b)
    # Rearranging: b = p(p - 2a) / (2(p - a))
    
    for a in range(1, p // 3):  # a < b < c, so a < p/3
        numerator = p * (p - 2 * a)
        denominator = 2 * (p - a)
        
        if numerator % denominator == 0:
            b = numerator // denominator
            if b > a:  # Ensure a < b
                c = p - a - b
                if c > b and a*a + b*b == c*c:  # Verify it's a right triangle
                    count += 1
    
    return count

limit = 1000
max_count = 0
best_p = 0

for p in range(12, limit + 1):  # Minimum perimeter for integer right triangle is 12 (3,4,5)
    count = count_right_triangles(p)
    if count > max_count:
        max_count = count
        best_p = p

print(best_p)
