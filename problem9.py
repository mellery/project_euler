#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def problem9(limit):
    for a in range(1,limit+1):
        for b in range(a,limit+1):
            for c in range(b,limit+1):
                if (a*a) + (b*b) == (c*c):
                    if (a+b+c) == 1000:
                        return(a*b*c)

print(problem9(1000))
