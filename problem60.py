from euler_common import is_prime

def can_form_pair(a, b):
    """Check if two primes can form a pair (both concatenations are prime)"""
    # Check both concatenations
    a_str, b_str = str(a), str(b)
    ab = int(a_str + b_str)
    ba = int(b_str + a_str)
    return is_prime(ab) and is_prime(ba)

def find_prime_set(target_size, limit=8500):
    """Find a set of primes where all pairs can be concatenated to form primes"""
    
    # Generate primes, excluding 2 and 5 (they cause issues with concatenation)
    # Also exclude primes ending in 3 when paired with primes ending in 7 (creates multiples of 10)
    primes = []
    for n in range(3, limit):
        if n != 5 and is_prime(n):
            # Skip some primes that are less likely to form valid pairs
            if n % 10 in [1, 3, 7, 9]:  # Only consider primes ending in these digits
                primes.append(n)
    
    # Build compatibility graph
    compatible = {}
    for i, p1 in enumerate(primes):
        compatible[p1] = []
        for p2 in primes[i+1:]:
            if can_form_pair(p1, p2):
                compatible[p1].append(p2)
                if p2 not in compatible:
                    compatible[p2] = []
                compatible[p2].append(p1)
    
    # Recursive search for cliques of given size
    def find_clique(current_set, candidates, target):
        if len(current_set) == target:
            return current_set
        
        if not candidates:
            return None
            
        for i, prime in enumerate(candidates):
            # Check if this prime is compatible with all primes in current set
            if all(prime in compatible.get(p, []) or p in compatible.get(prime, []) 
                   for p in current_set):
                
                # Recursively search with this prime added
                new_candidates = [p for p in candidates[i+1:] 
                                if p in compatible.get(prime, [])]
                
                result = find_clique(current_set + [prime], new_candidates, target)
                if result:
                    return result
        
        return None
    
    # Start search
    for start_prime in primes:
        if start_prime in compatible:
            result = find_clique([start_prime], compatible[start_prime], target_size)
            if result:
                return result
    
    return None

# Find the first set of 5 primes
result = find_prime_set(5)
if result:
    print(sum(result))
else:
    print("No solution found")