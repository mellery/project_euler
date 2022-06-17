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
