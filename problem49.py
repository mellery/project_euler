from euler_common import eratosthenes
from itertools import permutations

temp = eratosthenes(10000)
primes = []
for t in temp:
    if t >= 1000:
        primes.append(t)

for p in primes:
    #print(p)
    temp = [''.join(p) for p in permutations(str(p))]
    
    if str(p+3330) in temp and str(p+3330*2) in temp and p+3330 in primes and p+3330*2 in primes:
        print(str(p)+str(p+3330)+str(p+3330*2))
    