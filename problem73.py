from euler_common import hcf

limit = 12000
#limit = 8

a = 3
b = 2
ans = 0
fracs = []
rat = {}

for d in range(1,limit+1):
    print(d)
    for n in range(d//a+1,(d-1)//b+1):
        if hcf(n,d) == 1:
            ans = ans + 1
            
print(ans)