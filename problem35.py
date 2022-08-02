from euler_common import eratosthenes

#limit = 100
limit = 1000000

primes = eratosthenes(limit)

circ = []
print(len(primes))
for p in primes:
    temp = list(str(p))
    if '2' not in temp and '0' not in temp and '5' not in temp and '4' not in temp and '6' not in temp and '8' not in temp or p < 10:
        all_primes = True
        for i in range(0,len(temp)):
            n = int("".join(temp[i:])+"".join(temp[0:i]))
            if n not in primes:
                all_primes = False
        if all_primes == True:
            print(p)
            circ.append(p)
print(len(circ))


