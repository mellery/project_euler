def sum_proper_divisors(n):
    """Efficiently compute sum of proper divisors using sqrt optimization"""
    if n <= 1:
        return 0
    
    divisor_sum = 1  # 1 is always a proper divisor
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid counting the square root twice
                divisor_sum += n // i
        i += 1
    return divisor_sum

def solve_problem21():
    """Find sum of all amicable numbers under 10000"""
    limit = 10000
    
    # Pre-compute sum of proper divisors for all numbers
    divisor_sums = {}
    for i in range(1, limit):
        divisor_sums[i] = sum_proper_divisors(i)
    
    amicable_numbers = set()
    
    for a in range(1, limit):
        b = divisor_sums[a]
        
        # Check if b is also under our limit and forms an amicable pair
        if b < limit and b != a and divisor_sums.get(b, 0) == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)
    
    return sum(amicable_numbers)

print(solve_problem21())