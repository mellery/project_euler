from euler_common import eratosthenes
from euler_common import is_prime
from itertools import combinations

def problem51():
    #primes = eratosthenes(1000000)
    primes = eratosthenes(1000000)

    ans = 0
    anscount = 0

    for p in primes:
        #print("---")
        #print(p)
        pstr = str(p)
        for i in range(1,len(pstr)+1):
            minans = 1000000
            masks = list(combinations(range(len(pstr)),i))
            for m in masks:
                count = 0
                subs = []
                #print(m)
                if len(m) > 0:
                    for i in range(0,10):
                        temp = pstr
                        for d in m:
                            temp = temp[:d] + str(i) + temp[d+1:]                    
                        
                        if is_prime(int(temp)) and len(str(int(temp)))==len(pstr):
                            subs.append(int(temp))
                            if int(temp) < minans:
                                minans = int(temp)
                            count = count + 1
                #print(m,"count",count)
                
                if count >= anscount and p in subs:
                    #print("new",p,count,m)
                    #print(subs)
                    anscount = count
                    if count == 8:
                        return minans
print(problem51())

