from math import sqrt
limit = 1000
ans = 0
p_ans = 0
for p in range(0,limit+1):
    count = 0
    for a in range(1,p):
        for b in range(a,p):
            if a+b+sqrt(a*a+b*b) == p:
                print(p,"=",a,b,sqrt(a*a+b*b))
                count = count + 1
    if count > ans:
        ans = count
        p_ans = p
print(p_ans)
