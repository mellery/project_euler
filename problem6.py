#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_the_squares(limit):
    ans = 0
    for x in range(1,limit+1):
        ans = ans + (x*x)
    return ans

def square_of_the_sums(limit):
    ans = 0
    for x in range(1,limit+1):
        ans = ans + x
    return (ans*ans)

def problem6(limit):
    a = sum_of_the_squares(limit)
    b = square_of_the_sums(limit)
    print(b,a)
    return b-a

#print(problem6(10))
print(problem6(100))