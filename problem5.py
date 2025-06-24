#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from euler_common import lcm

def problem5(limit):
    result = 1
    for i in range(1, limit + 1):
        result = lcm(result, i)
    return result

#print(problem5(10))
print(problem5(20))