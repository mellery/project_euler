limit = 100000
ans = 0
for i in range(0,limit):
    pan = ""
    for n in range(1,limit):
        pan = pan + str(i*n)
        if len(pan) == 9:
            temp = "".join(sorted(str(pan)))
            if temp == "123456789":
                print(pan)
                if int(pan) > ans:
                    ans = int(pan)

        if len(pan) >= 9:
            break

print(ans)


