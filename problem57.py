from fractions import Fraction
from unittest import result
temp = 1
sub = 1/2
p = 1
q = 1
ans = 0
limit = 1000
for i in range(0,limit):
    res = temp + sub
    n = Fraction(res).limit_denominator().numerator
    d = Fraction(res).limit_denominator().denominator
    p1 = (p + 2*q)
    q1 = (p+q)
    if len(str(p1)) > len(str(q1)):
        ans = ans + 1
        print(res, Fraction(res).limit_denominator(), n, d)
    sub = 1/(2+sub)
    p = p1
    q = q1

print(ans)