import itertools

def is_perm(a,b):
    a_sorted = ''.join(sorted(str(a)))
    b_sorted = ''.join(sorted(str(b)))
    return a_sorted == b_sorted

cubes = []

limit = 10000

for i in range(1,limit):
    cubed = i**3
    cubes.append(cubed)

for i in range(1,limit):
    temp = i**3
    perms = [temp]
    for c in cubes:
        if temp != c and is_perm(temp,c):
            perms.append(c)
    if len(perms) > 4:
        print(i,sorted(perms))
        break