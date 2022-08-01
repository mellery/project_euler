from math import factorial

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: As 1! = 1 and 2! = 2 are not sums they are not included.
limit = factorial(9)*7
ans = 0
for i in range(3,limit):
    digits = list(str(i))
    temp = 0
    for d in digits:
        temp = temp + factorial(int(d))
    if temp == i:
        ans = ans + temp
print(ans)
