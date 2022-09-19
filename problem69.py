from euler_common import prime_factors

def phi(n):
    p = n
    for factor in prime_factors(n):
        p -= p // factor
    return p

ans = 0
ans_n = 0

limit = 1000000
for n in range(2,limit+1):
    p = phi(n)

    if n/p > ans:
        ans = n/p
        ans_n = n 
        print(ans_n,ans)

print(ans_n,ans)