"""Project Euler 99: Compare large exponentials

Find the line number (1-based) in input/0099_base_exp.txt whose base^exponent
is largest. We compare using exponent * log(base).
"""

import math
from pathlib import Path


def solve(path='input/0099_base_exp.txt'):
    best_line = None
    best_value = -1.0
    for i, line in enumerate(Path(path).read_text().strip().splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split(','))
        val = b * math.log(a)
        if val > best_value:
            best_value = val
            best_line = i
    return best_line


if __name__ == '__main__':
    print(solve())
