

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

from euler_common import eratosthenes

def problem10(limit):
    primes = eratosthenes(limit)
    return sum(primes)

print(problem10(2000000))
