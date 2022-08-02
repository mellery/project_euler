from euler_common import factors, is_prime

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def problem3(limit):
    ans = 0
    vals = factors(limit)
    for v in vals:
        if(is_prime(v)):
            if v > ans:
                ans = v
    return ans


#print(problem3(13195))
print(problem3(600851475143))