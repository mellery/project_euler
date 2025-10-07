"""Project Euler 100: Arranged probability

Find the number of blue discs B in the first arrangement where total discs T > 1e12
and probability of drawing two blue discs is 1/2. Uses Pell-type recurrence.
"""

def solve(limit=10**12):
    # Recurrence derived from Pell: starting from known solution (B, T) = (1,1)
    # but practical recurrence uses (B_next, T_next) = (3B + 2T - 2, 4B + 3T - 3)
    B, T = 1, 1
    while True:
        B, T = 3 * B + 2 * T - 2, 4 * B + 3 * T - 3
        if T > limit:
            return B


if __name__ == '__main__':
    print(solve())
