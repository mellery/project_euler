from euler_common import factors
#We can see that 28 is the first triangle number to have over five divisors.

#What is the value of the first triangle number to have over five hundred divisors?

def problem12(limit):
    i = 1
    t = 0
    while (1):
        t = t + i
        if len(factors(t)) > limit:
            return(t)
        i = i + 1


#print(problem12(5))
print(problem12(500))
