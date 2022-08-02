limit = 100
limit = 1000000
ans = 0
for i in range(0,limit):
    b = bin(i).replace('0b','')
    if i == int(str(i)[::-1]) and b == b[::-1]:
        print(i,b)
        ans = ans + i
print(ans)