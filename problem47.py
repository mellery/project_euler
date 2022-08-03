from euler_common import prime_factors

i = 1
l = 4
while(1):
    if len(prime_factors(i)) == l and len(prime_factors(i+1)) == l and len(prime_factors(i+2)) == l and len(prime_factors(i+3)) == l:
        print(i)
        break
    i = i + 1