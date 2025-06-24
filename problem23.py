#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would 
# be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
#it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def sum_proper_divisors(n):
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

def is_abundant(n):
    return sum_proper_divisors(n) > n

def problem23(limit):
    # Find all abundant numbers up to limit
    abundant = []
    for i in range(12, limit):  # Start from 12 as it's the smallest abundant number
        if is_abundant(i):
            abundant.append(i)
    
    # Mark all numbers that can be written as sum of two abundant numbers
    can_be_sum = [False] * limit
    
    for i, a in enumerate(abundant):
        for j in range(i, len(abundant)):
            b = abundant[j]
            if a + b >= limit:
                break
            can_be_sum[a + b] = True
    
    # Sum all numbers that cannot be written as sum of two abundant numbers
    total = 0
    for i in range(1, limit):
        if not can_be_sum[i]:
            total += i
    
    return total

print(problem23(28124))