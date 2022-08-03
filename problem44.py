import sys
from math import sqrt

def pentagonal(n):
    return int(n*(3*n-1)/2)

def is_pentagonal(x):
    return (1+sqrt(24*x+1))%6 == 0
    
limit = 5000

p = []

for i in range(1,limit+1):
    p.append(pentagonal(i))

for a in p:
    for b in p:
        if (is_pentagonal(a+b) and is_pentagonal(abs(a-b))):
            print(abs(a-b))