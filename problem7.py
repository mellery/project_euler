#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10,001st prime number?

from euler_common import eratosthenes

def problem7(limit):
    primes = eratosthenes(limit*limit)
    print(len(primes))
    if len(primes) >= limit:
        return(primes[limit-1])

#print(problem7(6))
print(problem7(10001))