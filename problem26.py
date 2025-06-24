from euler_common import prime_factors
def problem26(limit):
    ans = 0
    ans_d = 0
    for d in range(2,limit+1):
        digits = []
        
        n = 1
        digit = d
        digits.append(n%d)
        while 1:
            digit = (digits[-1]*10)%d

            if digit not in digits:
                digits.append(digit)
            else:
                break
        if len(digits) > ans:
            ans = len(digits)
            ans_d = d

    return ans_d

print(problem26(1000))