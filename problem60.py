from euler_common import is_prime

def can_form_pair(a, b):
    """Check if two primes can form a pair (both concatenations are prime)"""
    # Check a+b and b+a
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    return is_prime(ab) and is_prime(ba)

def find_prime_set(target_size, limit=10000):
    """Find a set of primes where all pairs can be concatenated to form primes"""
    
    # Generate primes, excluding 2 and 5 (they cause issues with concatenation)
    primes = []
    for n in range(3, limit):
        if n != 5 and is_prime(n):
            primes.append(n)
    
    # Build graph of prime pairs
    compatible = {}
    for i, p1 in enumerate(primes):
        compatible[p1] = []
        for j, p2 in enumerate(primes[i+1:], i+1):
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