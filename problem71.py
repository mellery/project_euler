limit = 1000000
#limit = 8

val = 3/7
fracs = []
rat = {}
for d in range(1,limit+1):
    print(d)
    for n in range(((3*d)//7)-1,d):
        #print(f"{n}/{d}",n/d)
        if n/d > val:
            break
        if n/d not in fracs:
            fracs.append(n/d)
            rat[n/d] = f"{n}/{d}"
fracs = sorted(fracs)
#print(fracs)
for f in fracs:
    if f < 3/7:
        print(rat[f])