from euler_common import phi_sieve

def solve_problem72():
    """Count proper fractions with denominator ≤ 1,000,000"""
    limit = 1000000
    
    # Use sieve to compute all phi values efficiently
    phi_values = phi_sieve(limit)
    
    # Sum phi(d) for d from 2 to limit
    # This gives the count of proper fractions with denominator ≤ limit
    total = sum(phi_values[2:limit+1])
    
    return total

result = solve_problem72()
print(result)
    