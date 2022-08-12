import time
import itertools
from euler_common import is_prime
from euler_common import eratosthenes

import itertools

def check_combos(primes, new_val):
    all_prime = True
    for p in primes:
        n = int(str(p) + str(new_val))
        if is_prime(n) == False:
            all_prime = False
        n = int(str(new_val) + str(p))
        if is_prime(n) == False:
            all_prime = False
    return all_prime
    
def find_sets(primes, setsize):
    sets = []
    for comb in itertools.combinations(primes,setsize):
        pairs = itertools.combinations(comb,2)
        all_prime = True
        for p in pairs:
            n = int(str(p[0]) + str(p[1]))
            if is_prime(n) == False:
                all_prime = False
            n = int(str(p[1]) + str(p[0]))
            if is_prime(n) == False:
                all_prime = False

        if all_prime == True:
            sets.append(list(comb))

    return sets


primes = eratosthenes(10000)
primes.remove(2)
primes.remove(5)
ans = max(primes)

setsize = 2
prime_pairs = []
prime_three = []
prime_four = []
prime_five = []

print(len(primes))

start = time.time()
prime_pairs = find_sets(primes, setsize)
for n in prime_pairs:
    for p in [x for x in primes if x > max(n)]:
        if check_combos(n,p):
            temp = list(n)
            temp.append(p)
            #print(temp)
            prime_three.append(temp)
            
for n in prime_three:
    for p in [x for x in primes if x > max(n)]:
        if check_combos(n,p):
            temp = list(n)
            temp.append(p)
            #print(temp)
            prime_four.append(temp)

for n in prime_four:
    for p in [x for x in primes if x > max(n)]:
        if check_combos(n,p):
            temp = list(n)
            temp.append(p)
            print(temp)
            print(sum(temp))
            prime_five.append(temp)

end = time.time()
print(end-start)