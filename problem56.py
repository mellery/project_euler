ans = 0

for a in range(1,100):

    for b in range(1,100):
        x = a**b
        temp = sum(list(map(int,str(x))))
        if temp > ans:
            ans = temp
print(ans)