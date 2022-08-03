limit = 1000

ans = 0
for i in range(1,limit+1):
    ans = ans + i**i
print(str(ans)[-10::])

