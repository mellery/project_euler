from euler_common import prime_factors

def phi(n):
    p = n
    for factor in prime_factors(n):
        p -= p // factor
    return p

ans = 0
ans_n = 0

def is_permutation(a,b):
    if ''.join(sorted(str(a))) == ''.join(sorted(str(b))):
        return True
    return False

limit = 10000000
min_ans = limit
ans_n = 0
for n in range(2,limit+1):
    p = phi(n)
    if is_permutation(n,p):
        
        if n/p < min_ans:
            min_ans = n/p
            ans_n = n
            print(n,p,n/p)

print(ans_n,ans)