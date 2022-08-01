from euler_common import eratosthenes

limit = 1000000
primes = eratosthenes(limit)
t = []
for p in primes:
    trunctable = True
    if p > 10:
        #print(p)
        temp = str(p)
        for i in range(1,len(temp)):
            l = temp[i::]
            r = temp[0:len(temp)-i]
            if int(l) not in primes:
                trunctable = False
            if int(r) not in primes:
                trunctable = False
        if trunctable == True:
            t.append(p)
            print(p)
print(len(t))
print(sum(t))