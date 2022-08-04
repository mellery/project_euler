from itertools import permutations

def problem52():
    i = 1
    while (1):
        perms = [''.join(p) for p in permutations(str(i))]
        if str(i*2) in perms and str(i*3) in perms and str(i*4) in perms and str(i*5) in perms and str(i*6) in perms:
            return(i)
        i = i + 1

print(problem52())
