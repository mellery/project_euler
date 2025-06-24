from math import sqrt

def pentagonal(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(x):
    # For x to be pentagonal, (1 + sqrt(24*x + 1)) / 6 must be an integer
    discriminant = 24 * x + 1
    sqrt_disc = int(sqrt(discriminant))
    return sqrt_disc * sqrt_disc == discriminant and (1 + sqrt_disc) % 6 == 0

def solve_problem44():
    """Find pentagonal numbers Pj and Pk where Pj + Pk and |Pj - Pk| are both pentagonal"""
    
    # Generate pentagonal numbers incrementally
    pentagonals = set()
    n = 1
    
    while n <= 3000:  # Reduced limit based on mathematical analysis
        pn = pentagonal(n)
        pentagonals.add(pn)
        
        # For each new pentagonal number, check against existing ones
        for pm in list(pentagonals):
            if pm >= pn:
                continue
                
            # Check if sum and difference are both pentagonal
            sum_val = pn + pm
            diff_val = pn - pm
            
            if is_pentagonal(sum_val) and is_pentagonal(diff_val):
                return diff_val
        
        n += 1
    
    return None

result = solve_problem44()
print(result)