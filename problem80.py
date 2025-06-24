"""
Project Euler Problem 80: Square root digital expansion

It is well known that if the square root of a natural number is not an integer, 
then it is irrational. The decimal expansion of such square roots is infinite 
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of 
the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums 
of the first one hundred decimal digits for all the irrational square roots.
"""

from decimal import Decimal, getcontext
from euler_common import is_perfect_square, digit_sum

def get_square_root_digits(n, precision=100):
    """
    Get the first 'precision' decimal digits of sqrt(n)
    
    Args:
        n (int): Number to find square root of
        precision (int): Number of decimal digits to compute
    
    Returns:
        str: String of digits (without decimal point)
    """
    # Set precision high enough to get accurate results
    # We need extra precision to account for rounding errors
    getcontext().prec = precision + 50
    
    # Calculate square root with high precision
    sqrt_n = Decimal(n).sqrt()
    
    # Convert to string and extract digits
    sqrt_str = str(sqrt_n)
    
    # Remove the decimal point and take first precision+1 digits
    # (including the integer part)
    digits_only = sqrt_str.replace('.', '')
    
    # Return first precision digits
    return digits_only[:precision]

def solve_problem80():
    """
    Find the total of the digital sums of the first 100 decimal digits 
    for all irrational square roots of the first 100 natural numbers.
    
    Returns:
        int: Sum of all digital sums
    """
    total_sum = 0
    
    for n in range(1, 101):
        # Skip perfect squares (rational square roots)
        if not is_perfect_square(n):
            # Get first 100 digits of sqrt(n)
            digits = get_square_root_digits(n, 100)
            
            # Sum the digits
            total_sum += digit_sum(int(digits))
    
    return total_sum

# Main execution
if __name__ == "__main__":
    result = solve_problem80()
    print(result)