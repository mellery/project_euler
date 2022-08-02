from itertools import permutations

def problem24(limit):
    values = [''.join(p) for p in permutations(limit)]
    values.sort()
    print(values[1000000-1])


problem24('0123456789')
