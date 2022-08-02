#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would 
# be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
#it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def sum_proper_divisors(n):
    divisors = []
    for i in range(1,n):
        if n%i==0:
            divisors.append(i)
    return(sum(divisors))

def is_deficient(n):
    if sum_proper_divisors(n) < n:
        return True
    return False

def is_abunant(n):
    if sum_proper_divisors(n) > n:
        return True
    return False

def is_perfect(n):
    if sum_proper_divisors(n) == n:
        return True
    return False

def problem23(limit):
    abudant = []
    
    for i in range(1,limit):
        if is_abunant(i):
            abudant.append(i)
    
    ans = 0
    for i in range(1,limit,2):
        found = False
        for a in abudant:
            for b in abudant:
                if a+b == i:
                    found = True
                    break
                elif a+b > i:
                    break
        if found == False:
            ans = ans + i
            print(i)
    return ans


print(problem23(28123))