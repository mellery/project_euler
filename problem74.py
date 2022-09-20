from math import factorial
from functools import cache

@cache
def digit_factorial(n):
    temp = list(str(n))
    val = 0
    for t in temp:
        val = val + factorial(int(t))
    return val

limit = 1000000
ans = 0
for x in range(1,limit):
    value = x
    seen = [value]
    while(1):
        value = digit_factorial(value)
        if value in seen:
            break
        else:
            seen.append(value)
            #print(seen)
    #print(seen)
    if len(seen) == 60:
        print(x,len(seen))
        ans = ans + 1
print(ans)