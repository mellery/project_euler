from itertools import permutations, product
import math


def valid_results(digits):
    """Return set of positive integers obtainable from digits using + - * / and parentheses."""
    ops = [lambda x, y: x + y,
           lambda x, y: x - y,
           lambda x, y: x * y,
           lambda x, y: x / y if y != 0 else None]

    results = set()

    # All permutations of the 4 digits
    for nums in permutations(digits):
        a, b, c, d = map(float, nums)
        # All choices of 3 operators
        for op_idx in product(range(4), repeat=3):
            f1, f2, f3 = (ops[i] for i in op_idx)

            # five parenthesizations for binary operator associativity
            vals = []

            # ((a b) c) d
            try:
                r1 = f1(a, b)
                if r1 is not None:
                    r2 = f2(r1, c)
                    if r2 is not None:
                        r3 = f3(r2, d)
                        if r3 is not None and abs(r3 - round(r3)) < 1e-9:
                            if r3 > 0 and abs(r3 - round(r3)) < 1e-9:
                                results.add(int(round(r3)))
            except Exception:
                pass

            # (a (b c)) d
            try:
                r1 = f2(b, c)
                if r1 is not None:
                    r2 = f1(a, r1)
                    if r2 is not None:
                        r3 = f3(r2, d)
                        if r3 is not None and abs(r3 - round(r3)) < 1e-9 and r3 > 0:
                            results.add(int(round(r3)))
            except Exception:
                pass

            # (a b) (c d)
            try:
                r1 = f1(a, b)
                r2 = f3(c, d)
                if r1 is not None and r2 is not None:
                    r3 = f2(r1, r2)
                    if r3 is not None and abs(r3 - round(r3)) < 1e-9 and r3 > 0:
                        results.add(int(round(r3)))
            except Exception:
                pass

            # a ((b c) d)
            try:
                r1 = f2(b, c)
                if r1 is not None:
                    r2 = f3(r1, d)
                    if r2 is not None:
                        r3 = f1(a, r2)
                        if r3 is not None and abs(r3 - round(r3)) < 1e-9 and r3 > 0:
                            results.add(int(round(r3)))
            except Exception:
                pass

            # a (b (c d))
            try:
                r1 = f3(c, d)
                if r1 is not None:
                    r2 = f2(b, r1)
                    if r2 is not None:
                        r3 = f1(a, r2)
                        if r3 is not None and abs(r3 - round(r3)) < 1e-9 and r3 > 0:
                            results.add(int(round(r3)))
            except Exception:
                pass

    return results


def longest_consecutive(seq):
    """Given a set of positive integers, return length of consecutive run starting at 1."""
    i = 1
    while True:
        if i not in seq:
            return i - 1
        i += 1


def solve():
    best_len = 0
    best_digits = None

    # choose 4 distinct digits from 1..9
    from itertools import combinations

    for digits in combinations(range(1, 10), 4):
        res = valid_results(digits)
        L = longest_consecutive(res)
        if L > best_len:
            best_len = L
            best_digits = digits

    # return concatenated digits as in problem statement
    return ''.join(str(d) for d in best_digits)


if __name__ == '__main__':
    print(solve())
