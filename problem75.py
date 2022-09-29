from euler_common import gcd
from math import sqrt
ans = 0
limit = 1500000

triangles = {}
 
ans = 0
mlimit = int(sqrt(limit / 2))
 
for m in range(2, mlimit):
    for n in range(1, m):
        if (((n + m) % 2) == 1 and gcd(n, m) == 1):
            a = m * m + n * n
            b = m * m - n * n
            c = 2 * m * n
            p = a + b + c
            
            while(p <= limit):
                if p not in triangles:
                    triangles[p] = 0
                triangles[p] = triangles[p]+1
                if (triangles[p] == 1):
                    ans = ans + 1
                if (triangles[p] == 2):
                    ans = ans - 1
                p += a+b+c
print(ans)