from euler_common import eratosthenes, phi_sieve, is_permutation

def solve_problem70():
    """Find n < 10^7 where n/phi(n) is minimized and n and phi(n) are permutations"""
    limit = 10000000
    
    # Use sieve to compute all phi values efficiently
    phi_values = phi_sieve(limit)
    
    min_ratio = float('inf')
    result = 0
    
    # Focus on numbers that are products of two large primes close to sqrt(limit)
    # This is because n/phi(n) is minimized when n has few prime factors
    primes = eratosthenes(int(limit**0.5) + 1000)
    
    # Check products of two primes near sqrt(limit)
    sqrt_limit = int(limit**0.5)
    for i, p1 in enumerate(primes):
        if p1 < sqrt_limit // 2:
            continue
        if p1 > sqrt_limit * 2:
            break
            
        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            n = p1 * p2
            
            if n >= limit:
                break
                
            # For product of two primes: phi(p1 * p2) = (p1-1) * (p2-1)
            phi_n = (p1 - 1) * (p2 - 1)
            
            if is_permutation(n, phi_n):
                ratio = n / phi_n
                if ratio < min_ratio:
                    min_ratio = ratio
                    result = n
    
    # Also check some other promising candidates using the sieve
    # Numbers close to products of two primes might also work
    for n in range(2000000, min(4000000, limit)):
        phi_n = phi_values[n]
        if is_permutation(n, phi_n):
            ratio = n / phi_n
            if ratio < min_ratio:
                min_ratio = ratio
                result = n
    
    return result

result = solve_problem70()
print(result)