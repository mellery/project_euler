"""Project Euler 95: Amicable chains

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""

def sum_proper_divisors(limit):
    spd = [0] * (limit + 1)
    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            spd[j] += i
    return spd


def solve(limit=10**6):
    spd = sum_proper_divisors(limit)

    visited_global = [False] * (limit + 1)
    best_len = 0
    best_min = None

    for i in range(2, limit + 1):
        if visited_global[i]:
            continue

        seq_index = {}
        seq = []
        n = i
        while True:
            if n <= 0 or n > limit:
                # chain escapes bounds
                for v in seq:
                    if v <= limit:
                        visited_global[v] = True
                break
            if n in seq_index:
                # found a cycle starting at seq_index[n]
                start = seq_index[n]
                cycle = seq[start:]
                # verify all elements in cycle are <= limit
                if all(1 <= x <= limit for x in cycle):
                    if len(cycle) > best_len:
                        best_len = len(cycle)
                        best_min = min(cycle)
                # mark all seen numbers as visited
                for v in seq:
                    if v <= limit:
                        visited_global[v] = True
                break
            if visited_global[n]:
                # hits previously processed chain
                for v in seq:
                    if v <= limit:
                        visited_global[v] = True
                break

            seq_index[n] = len(seq)
            seq.append(n)
            n = spd[n]

    return best_min


if __name__ == '__main__':
    print(solve())
