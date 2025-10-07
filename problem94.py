"""Project Euler 94: Almost equilateral triangles

Find all almost equilateral triangles with integral side lengths and integral area
such that the perimeter does not exceed one billion. Sum their perimeters.

This uses Pell-type recurrences derived from solving the Diophantine conditions.
"""

"""Solver for Project Euler 94: almost-equilateral integer-area triangles."""

def solve(limit=10**9):
    """Return sum of perimeters of all almost-equilateral integer-area
    triangles with perimeter <= limit.
    """
    total = 0

    # We generate solutions from the Pell recurrence. Two families exist:
    # for sides (a,a,a+1) and (a,a,a-1). Known minimal solutions seed the
    # recurrence; multiplying by (2+sqrt(3)) generates further solutions.

    # Use integer recurrence on (x,y) where x + y*sqrt(3) multiplies by (2+sqrt(3)).
    x, y = 2, 1  # fundamental solution of x^2 - 3*y^2 = 1 is (2,1)

    # We'll produce u + v*sqrt(3) = (2+sqrt(3))^k for k>=1
    while True:
        # compute candidate a values for both cases
        # For (a,a,a+1): a = (2*x - 1) // 3 when divisible
        if (2 * x - 1) % 3 == 0:
            a = (2 * x - 1) // 3
            if a > 1:
                p = 3 * a + 1
                if p <= limit:
                    total += p
        # For (a,a,a-1): a = (2*x + 1) // 3 when divisible
        if (2 * x + 1) % 3 == 0:
            a = (2 * x + 1) // 3
            if a > 1:
                p = 3 * a - 1
                if p <= limit:
                    total += p

        # step: multiply (x + y*sqrt(3)) by (2 + sqrt(3))
        x, y = 2 * x + 3 * y, x + 2 * y

        # termination heuristic: smallest perimeter from x will grow roughly
        # like O(x), so if 3*((2*x-1)//3)+1 > limit we can break; to be safe
        # break when 3*((2*x-1)//3)+1 exceeds limit and likewise for +1 case.
        # Check lower bound estimate using x directly.
        if 3 * ((2 * x - 1) // 3) + 1 > limit and 3 * ((2 * x + 1) // 3) - 1 > limit:
            break

    return total


if __name__ == '__main__':
    print(solve())
