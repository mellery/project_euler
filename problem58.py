from euler_common import is_prime

def solve_problem58():
    """Find the side length of the spiral where the prime ratio drops below 10%"""
    
    # Start with the center (1) which is not prime
    total_diagonals = 1
    prime_count = 0
    
    # Current position and side length
    current_number = 1
    side_length = 1
    
    while True:
        side_length += 2  # Odd side lengths: 3, 5, 7, 9, ...
        
        # For each new layer, we add 4 corner values
        # The corners are at: current + gap, current + 2*gap, current + 3*gap, current + 4*gap
        # where gap = side_length - 1
        gap = side_length - 1
        
        # Check the four corners of this layer
        for corner in range(1, 5):
            current_number += gap
            total_diagonals += 1
            
            if is_prime(current_number):
                prime_count += 1
        
        # Check if prime ratio is below 10%
        prime_ratio = prime_count / total_diagonals
        if prime_ratio < 0.1:
            return side_length
        
        # Early termination if we're getting very large numbers
        if side_length > 100000:
            break
    
    return -1  # Should not reach here

result = solve_problem58()
print(result)
