import itertools

def get_tri(limit):
    results = []
    i = 1
    while(1):
        n = i*(i+1)//2
        i = i + 1
        if n < limit:
            if n >= 1000:
                results.append(n)
        else:
            return results
        
def get_square(limit):
    results = []
    i = 1
    while(1):
        n = i*i
        i = i + 1
        if n < limit:
            if n >= 1000:
                results.append(n)
        else:
            return results

def get_pent(limit):
    results = []
    i = 1
    while(1):
        n = i*(3*i-1)//2
        i = i + 1
        if n < limit:
            if n >= 1000:
                results.append(n)
        else:
            return results

def get_hex(limit):
    results = []
    i = 1
    while(1):
        n = i*(2*i-1)
        i = i + 1
        if n < limit:
            if n >= 1000:
                results.append(n)
        else:
            return results

def get_hept(limit):
    results = []
    i = 1
    while(1):
        n = i*(5*i-3)//2
        i = i + 1
        if n < limit:
            if n >= 1000:
                results.append(n)
        else:
            return results

def get_oct(limit):
    results = []
    i = 1
    while(1):
        n = i*(3*i-2)
        i = i + 1
        if n < limit:
            if n >= 1000:
                results.append(n)
        else:
            return results

limit = 10000

tri_list = get_tri(limit)
square_list = get_square(limit)
pent_list = get_pent(limit)
hex_list = get_hex(limit)
hept_list = get_hept(limit)
oct_list = get_oct(limit)

all_lists = []
all_lists.append(tri_list)
all_lists.append(square_list)
all_lists.append(pent_list)
all_lists.append(hex_list)
all_lists.append(hept_list)
all_lists.append(oct_list)

#print(all_lists)

ans = dict()

for perm in itertools.permutations(all_lists):

    for t in perm[0]:
        head1 = int(str(t)[:2])
        tail = int(str(t)[-2:])
        
        for s in perm[1]:
            head = int(str(s)[:2])
            if head == tail:
                tail = int(str(s)[-2:])
                
                for p in perm[2]:
                    head = int(str(p)[:2])
                    if head == tail:
                        tail = int(str(p)[-2:])

                        for h in perm[3]:
                            head = int(str(h)[:2])
                            if head == tail:
                                tail = int(str(h)[-2:])

                                for h2 in perm[4]:
                                    head = int(str(h2)[:2])
                                    if head == tail:
                                        tail = int(str(h2)[-2:])
                                        #print(t,s,p,h,h2)

                                        for o in perm[5]:
                                            head = int(str(o)[:2])
                                            if head == tail:
                                                tail = int(str(o)[-2:])
                                                if head1 == tail:
                                                    temp = sum([t,s,p,h,h2,o])
                                                    if temp in ans:
                                                        ans[temp] = ans[temp] + 1
                                                    else:
                                                        ans[temp] = 1
                                                    print(t,s,p,h,h2,o, temp)
print(ans)

for k,v in ans.items():
    if v == 6:
        print(k)