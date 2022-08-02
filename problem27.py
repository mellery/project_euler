from euler_common import is_prime

def quadratic_formula(n,a,b):
    return n*n + a*n + b

def problem27():
    best = 0
    best_ab = 0
    for a in range(-1000,1000+1):
        for b in range(-1000,1000+1):
            n = 0
            while 1:
                ans = quadratic_formula(n,a,b)
                if is_prime(ans):
                    #print(n,ans)
                    n = n + 1
                    continue
                else:
                    if (n > best):
                        print(n,a,b,a*b)
                        best = n
                        best_ab = a*b
                    break
    return best_ab
            

print(problem27())