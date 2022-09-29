from euler_common import eratosthenes
primes = eratosthenes(100)

L, target = 5000, 11
while True:
    ways = [1] + [0]*target
    for p in primes:
        for i in range(p, target+1):
            ways[i] += ways[i-p]
    if ways[target] > L: 
        break    
    target += 1

print(target)