from euler_common import eratosthenes

#primes = eratosthenes(1000)
primes = eratosthenes(1000000)
print("primes")
ans = 0
ans_len = 0
for x in range(0,len(primes)):
    for y in range(x,len(primes)):
        if (sum(primes[x:y])) > max(primes):
            break
        if sum(primes[x:y]) in primes:
            if y-x > ans_len:
                ans_len = y-x
                ans = sum(primes[x:y])
            #print(sum(primes[x:y]),y-x)
print(ans,ans_len)