from euler_common import is_prime

def is_truncatable_prime(n):
    """Check if n is a truncatable prime (both left and right truncations are prime)"""
    if not is_prime(n) or n < 10:
        return False
    
    s = str(n)
    
    # Check right truncations (remove digits from right)
    for i in range(1, len(s)):
        if not is_prime(int(s[:i])):
            return False
    
    # Check left truncations (remove digits from left)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False
    
    return True

def can_be_truncatable(n):
    """Quick filter: truncatable primes can only contain digits 1,2,3,5,7,9"""
    s = str(n)
    # First digit can be 2,3,5,7 (must be prime)
    # Middle digits can be 1,3,7,9 (even digits and 5 would create composite truncations)
    # Last digit can be 3,7 (must be prime and odd, excluding 5)
    
    if len(s) == 1:
        return False
    
    # First digit must be prime
    if s[0] not in '2357':
        return False
    
    # Last digit must be 3 or 7 (prime and not 2 or 5)
    if s[-1] not in '37':
        return False
    
    # Middle digits cannot be 0,2,4,5,6,8 as they would create composites
    for i in range(1, len(s)-1):
        if s[i] not in '1379':
            return False
    
    return True

truncatable_primes = []
n = 11  # Start from 11 (first 2-digit number, since single digits don't count)

# Problem states there are exactly 11 truncatable primes
while len(truncatable_primes) < 11:
    if can_be_truncatable(n) and is_truncatable_prime(n):
        truncatable_primes.append(n)
    n += 1

print(sum(truncatable_primes))