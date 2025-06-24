from math import gcd

def solve_problem71():
    """Find the fraction n/d < 3/7 with d ≤ 1,000,000 that is closest to 3/7"""
    
    limit = 1000000
    target = 3/7
    
    best_n = 0
    best_d = 1
    best_diff = target
    
    # For each denominator d, find the largest numerator n such that n/d < 3/7
    for d in range(1, limit + 1):
        # We want n/d < 3/7, so n < 3*d/7
        # The largest such n is floor((3*d - 1)/7)
        n = (3 * d - 1) // 7
        
        # Make sure n/d < 3/7 and gcd(n,d) = 1 (reduced form)
        if n > 0 and n * 7 < 3 * d and gcd(n, d) == 1:
            diff = target - n/d
            if diff < best_diff:
                best_diff = diff
                best_n = n
                best_d = d
    
    return best_n

# Alternative mathematical approach using Farey sequences properties
def solve_problem71_optimized():
    """Use mathematical properties to find the answer more efficiently"""
    
    # The fraction immediately to the left of 3/7 in the Farey sequence F_n
    # can be found using the mediant property
    
    # Start with the two fractions that 3/7 lies between in a coarse Farey sequence
    # We know 3/7 is between 2/5 and 1/2, but let's be more precise
    
    limit = 1000000
    
    # The fraction immediately to the left of a/b in the Farey sequence F_n
    # has the form (ka-1)/(kb) where k is the largest integer such that kb ≤ n
    
    # For 3/7, we want the largest k such that 7k ≤ 1000000
    k = limit // 7  # k = 142857
    
    # The candidate fraction is (3k-1)/(7k) = (3*142857-1)/(7*142857) = 428570/999999
    n = 3 * k - 1
    d = 7 * k
    
    # But we need d ≤ 1000000, and 7*142857 = 999999 ≤ 1000000, so this works
    # Also need to check if this is in reduced form
    
    if d <= limit:
        return n
    else:
        # If 7k > limit, try k-1
        k = k - 1
        n = 3 * k - 1
        d = 7 * k
        return n

# Use the optimized mathematical approach
result = solve_problem71_optimized()
print(result)