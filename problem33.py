ans = []
for a in range(10,100):
    for b in range(10,100):
        if a/b < 1:
            astr = str(a)
            bstr = str(b)
            if astr[0] == bstr[1] and int(bstr[0]) != 0:
                if int(astr[1])/int(bstr[0]) == a/b:
                    print(a,"/",b,"=",a/b)
                    ans.append(a/b)
            if astr[1] == bstr[0] and int(bstr[1]) != 0:
                if int(astr[0])/int(bstr[1]) == a/b:
                    print(a,"/",b,"=",a/b)
                    ans.append(a/b)

temp = ans[0]
for a in ans[1::]:
    temp = temp * a
print(1/temp)