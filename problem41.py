from itertools import permutations

from euler_common import eratosthenes
from euler_common import is_prime

#primes = eratosthenes(1000000000)

#print("done")
#for p in primes:
#    temp = "".join(sorted(str(p)))

limit = 10

ans = 0

for i in range(1,limit):
    digits = ""
    for d in range(1,i+1):
        digits = digits+str(d)
    
    perms = [''.join(p) for p in permutations(digits)]
    for p in perms:
        if is_prime(int(p)):
            print(p)
            if int(p) > ans:
                ans = int(p)
print(ans)