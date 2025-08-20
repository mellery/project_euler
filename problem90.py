# Each of the six faces on a cube has a different digit ( to ) written on it; the same is done to a 
# second cube. By placing the two cubes side-by-side in different positions we can form a variety of
# 2-digit numbers.

# For example, the square number 64 could be formed:

# In fact, by carefully choosing the digits on both cubes it is possible to display all of the square 
# numbers below one-hundred: 00, 01, 04, 09, 16, 25, 36, 49, 64, and 81.

# For example, one way this can be achieved is by placing {0,5,6,7,8,9} on one cube and {1,2,3,4,8,9}
# on the other cube.

# However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement 
# like {0,5,6,7,8,9} and {1,2,3,4,6,7} allows for all nine square numbers to be displayed; otherwise 
# it would be impossible to obtain 09.

# In determining a distinct arrangement we are interested in the digits on each cube, not the order.

# {1,2,3,4,5,6} is equivalent to {3,6,4,1,2,5}
# {1,2,3,4,5,6} is distinct from {1,2,3,4,5,9}

# But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both 
# represent the extended set for the purpose of forming 2-digit numbers.

# How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?

import itertools

# All two-digit squares below 100
squares = ['01', '04', '09', '16', '25', '36', '49', '64', '81']

# For 6/9 flipping, treat both as present if either is present
def extend(cube):
    cube = set(cube)
    if 6 in cube or 9 in cube:
        cube.add(6)
        cube.add(9)
    return cube

digits = list(range(10))
cube_combos = list(itertools.combinations(digits, 6))
cube_sets = [extend(cube) for cube in cube_combos]

count = 0
seen = set()

for i, cube1 in enumerate(cube_sets):
    for j, cube2 in enumerate(cube_sets):
        if j < i:
            continue  # avoid double-counting unordered pairs
        valid = True
        for sq in squares:
            d1, d2 = int(sq[0]), int(sq[1])
            if not ((d1 in cube1 and d2 in cube2) or (d2 in cube1 and d1 in cube2)):
                valid = False
                break
        if valid:
            # Use frozenset to ensure unordered uniqueness
            pair = frozenset([frozenset(cube_combos[i]), frozenset(cube_combos[j])])
            if pair not in seen:
                seen.add(pair)
                count += 1

print(count)
