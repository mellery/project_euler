from math import factorial
#Find the sum of the digits in the number 100!

def problem20(n):
    temp = str(factorial(n))
    ans = 0
    for t in list(temp):
        ans = ans + int(t)
    return ans

#print(problem20(10))
print(problem20(100))