def solve_problem69():
    """Find n ≤ 1,000,000 for which n/φ(n) is maximum"""
    
    # Mathematical insight: n/φ(n) is maximized when n has many small prime factors
    # The ratio n/φ(n) = ∏(p/(p-1)) for all prime factors p of n
    # To maximize this, we want the product of small primes
    
    limit = 1000000
    
    # The smallest primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    
    # Find the largest product of consecutive primes starting from 2
    # that doesn't exceed the limit
    product = 1
    result = 1
    
    for prime in primes:
        new_product = product * prime
        if new_product > limit:
            break
        product = new_product
        result = product
    
    return result

# Direct mathematical solution
result = solve_problem69()
print(result)