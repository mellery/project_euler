# The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power 
# is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:
# 28 = 2^2 + 2^3 + 2^4
# 33 = 2^2 + 3^3 + 2^4
# 49 = 7^2 + 2^3 + 2^4
# 50 = 5^2 + 3^3 + 2^4
# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, 
# and prime fourth power?

import math

LIMIT = 50_000_000

def primes_up_to(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# Find upper bounds for each power
max_p2 = int(LIMIT ** 0.5) + 1
max_p3 = int(LIMIT ** (1/3)) + 1
max_p4 = int(LIMIT ** 0.25) + 1

primes2 = [p**2 for p in primes_up_to(max_p2)]
primes3 = [p**3 for p in primes_up_to(max_p3)]
primes4 = [p**4 for p in primes_up_to(max_p4)]

results = set()

for a in primes2:
    if a >= LIMIT:
        break
    for b in primes3:
        if a + b >= LIMIT:
            break
        for c in primes4:
            s = a + b + c
            if s < LIMIT:
                results.add(s)
            else:
                break

print(len(results))

