from euler_common import phi
limit = 1000000
#limit = 8

ans = 0
#fracs_str = {}
for d in range(2,limit+1):
    print(d)
    ans = ans + phi(d)
print(ans)
    