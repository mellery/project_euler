from euler_common import eratosthenes

limit = 1000000
primes = eratosthenes(limit)
prime_set = set(primes)  # O(1) lookup instead of O(n)

max_length = 0
result_prime = 0

# For each starting position
for start in range(len(primes)):
    current_sum = 0
    
    # Build consecutive sum starting from 'start'
    for end in range(start, len(primes)):
        current_sum += primes[end]
        
        # If sum exceeds limit, no point continuing
        if current_sum >= limit:
            break
            
        # If we have a longer sequence and the sum is prime
        sequence_length = end - start + 1
        if sequence_length > max_length and current_sum in prime_set:
            max_length = sequence_length
            result_prime = current_sum

print(result_prime)