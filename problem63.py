valid = []
for a in range(1,100):
    for b in range(1,100):
        temp = a**b
        if len(str(temp)) == b:
            #print(temp,a,b)
            valid.append(temp)
print(len(valid))