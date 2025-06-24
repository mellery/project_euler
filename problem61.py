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

solutions = []

for perm in itertools.permutations(all_lists):
    for t in perm[0]:
        head1 = int(str(t)[:2])
        tail = int(str(t)[-2:])
        
        for s in perm[1]:
            head = int(str(s)[:2])
            if head == tail and s != t:  # Ensure no duplicate numbers
                tail = int(str(s)[-2:])
                
                for p in perm[2]:
                    head = int(str(p)[:2])
                    if head == tail and p not in [t, s]:
                        tail = int(str(p)[-2:])

                        for h in perm[3]:
                            head = int(str(h)[:2])
                            if head == tail and h not in [t, s, p]:
                                tail = int(str(h)[-2:])

                                for h2 in perm[4]:
                                    head = int(str(h2)[:2])
                                    if head == tail and h2 not in [t, s, p, h]:
                                        tail = int(str(h2)[-2:])

                                        for o in perm[5]:
                                            head = int(str(o)[:2])
                                            if head == tail and o not in [t, s, p, h, h2]:
                                                tail = int(str(o)[-2:])
                                                if head1 == tail:
                                                    # Found a valid cycle - check if all numbers are distinct
                                                    cycle_nums = [t, s, p, h, h2, o]
                                                    if len(set(cycle_nums)) == 6:  # All numbers are unique
                                                        solutions.append((cycle_nums, sum(cycle_nums)))

# Find all unique sums
if solutions:
    sums = [sol[1] for sol in solutions]
    # Count frequency of each sum
    sum_counts = {}
    for s in sums:
        sum_counts[s] = sum_counts.get(s, 0) + 1
    
    # Find the sum that appears exactly 6 times (one for each permutation of the same cycle)
    for sum_val, count in sum_counts.items():
        if count == 6:
            print(sum_val)
            break