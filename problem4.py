

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def problem4(limit):
    ans = 0
    for i in range(0,limit):
        for j in range(0,limit):
            a = str(i*j)
            b = a[::-1]
            if (a == b):
                if i*j > ans:
                    ans = i*j
    return ans

#print(problem4(100))
print(problem4(1000))
