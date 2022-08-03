from euler_common import is_prime
from euler_common import eratosthenes

i = 3

#while (i < 34):
while (1):
    if (is_prime(i) == False):
        #print(i)
        primes = eratosthenes(i)
        valid = False
        for p in primes:
            if valid == True:
                break
            for n in range(0,i-p+1):
                if i == p + 2*n*n:
                    valid = True
                    print(i,"=",p,"+",2*n*n)
                    break
                    
        if valid == False:
            print(i)
            break

        #print("---")
    i = i + 2