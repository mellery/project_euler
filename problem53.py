from math import comb

count = 0
for n in range(1,100+1):
    for r in range(1,n):
        if comb(n,r) > 1000000:
            count = count + 1
print(count)