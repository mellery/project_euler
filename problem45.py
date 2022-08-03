from math import sqrt
def triangle(n):
    return int((0.5*n*(n+1)))

def is_pentagonal(x):
    return (1+sqrt(24*x+1))%6 == 0
    
def is_hexagonal(x):
    return ((-1+sqrt(1+8*x))//2) == 0

i = 286
while(1):
    if is_pentagonal(triangle(i)) and i%2 != 0:
        print(triangle(i))
        break
    i = i + 1