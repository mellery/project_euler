from euler_common import is_prime
import math

def satisfies_goldbach_conjecture(n):
    """Check if odd composite n can be written as prime + 2*k²"""
    # For each possible k, check if n - 2*k² is prime
    k = 1
    while 2 * k * k < n:
        remainder = n - 2 * k * k
        if remainder > 0 and is_prime(remainder):
            return True
        k += 1
    return False

# Start from 9 (first odd composite that isn't 1)
n = 9

while True:
    if not is_prime(n):  # Only check odd composite numbers
        if not satisfies_goldbach_conjecture(n):
            print(n)
            break
    n += 2  # Only check odd numbers