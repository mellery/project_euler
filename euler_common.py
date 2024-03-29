from math import sqrt
from functools import reduce
from functools import cache

def eratosthenes(n):
    m = n+1
    numbers = [True] * m 
    for i in range(2, int(n**0.5 + 1)):
        if numbers[i]:
            for j in range(i*i, m, i):
                numbers[j] = False
    primes = []
    for i in range(2, m):
        if numbers[i]:
            primes.append(i)
    return primes

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b/gcd(a, b)

def hcf(a, b):
    while(b):
        a, b = b, a % b
    return a

def phi(n):
    p = n
    for factor in prime_factors(n):
        p -= p // factor
    return p

def factors(n):    
    return set(reduce(list.__add__, 
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def prime_factors(n):
    temp = set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    factors = set()
    for t in temp:
        if is_prime(t) == True:
            factors.add(t)
    return factors
    

@cache
def is_prime(n):
    prime_flag = 0
  
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

def triangle(n):
    return sum([i for i in range(1,n+1)])

def get_digit(number, n):
    return number // 10**n % 10