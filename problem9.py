#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math

def problem9(limit):
    for a in range(1, limit // 3):
        for b in range(a, (limit - a) // 2):
            c = limit - a - b
            if a*a + b*b == c*c:
                return a*b*c
    return None

print(problem9(1000))
