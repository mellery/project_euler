#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10,001st prime number?

from euler_common import is_prime

def problem7(limit):
    count = 0
    num = 2
    while count < limit:
        if is_prime(num):
            count += 1
            if count == limit:
                return num
        num += 1
    return None

#print(problem7(6))
print(problem7(10001))