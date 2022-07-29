from cv2 import sort


prods = []
for a in range(1,9999):
    for b in range(a,9999):
        c = a * b
        temp = str(a)+str(b)+str(c)
        temp = "".join(sorted(temp))
        if temp == "123456789":
            print(a,"*",b,"=",c)
            if c not in prods:
                prods.append(c)
print(sum(prods))
    
