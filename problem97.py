"""Project Euler 97: Large non-Mersenne prime

Compute the last ten digits of 28433 * 2^7830457 + 1
"""

def solve():
    mod = 10**10
    res = (28433 * pow(2, 7830457, mod) + 1) % mod
    # format without leading zeros trimmed: print as integer
    return res


if __name__ == '__main__':
    print(solve())
