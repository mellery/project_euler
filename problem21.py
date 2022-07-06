def sum_proper_divisors(n):
    divisors = []
    for i in range(1,n):
        if n%i==0:
            divisors.append(i)

    return sum(divisors)

def is_amicable(n):
    a = sum_proper_divisors(n)
    b = sum_proper_divisors(a)
    if n == b and a != b:
        print(a,n,b)
        return True
    return False

def problem21(limit):
    ans = 0
    for i in range(1,limit):
        if is_amicable(i):
            ans = ans + i
    return ans

print(problem21(10000))