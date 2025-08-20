# The points P(x1, y1) and Q(x2, y2) are plotted at integer co-ordinates and are joined to the 
# origin, O(0, 0), to form triangle OPQ.
#
# There are exactly fourteen triangles containing a right angle that can be formed when each 
# co-ordinate lies between 0 and 2 inclusive; that is,0 ≤ x1, y1, x2, y2 ≤ 2.
#
# Given that the coordinates lie between 0 and 50 inclusive, how many right triangles can be 
# formed?

LIMIT = 50
count_O = 0
count_P = 0

# Right angle at the origin (count each unordered pair once)
for x1 in range(LIMIT + 1):
    for y1 in range(LIMIT + 1):
        if x1 == 0 and y1 == 0:
            continue
        for x2 in range(LIMIT + 1):
            for y2 in range(LIMIT + 1):
                if x2 == 0 and y2 == 0:
                    continue
                if x1 == x2 and y1 == y2:
                    continue
                if x1 * x2 + y1 * y2 == 0:
                    if (x1, y1) < (x2, y2):
                        count_O += 1

# Right angle at P
for x1 in range(LIMIT + 1):
    for y1 in range(LIMIT + 1):
        if x1 == 0 and y1 == 0:
            continue
        # The direction vector perpendicular to OP is (y1, -x1)
        # Q = (x1 + k*y1, y1 - k*x1)
        # k must be chosen so that Q is in bounds and not equal to O or P
        gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
        g = gcd(x1, y1)
        dx = y1 // g
        dy = -x1 // g
        k = 1
        while True:
            x2 = x1 + dx * k
            y2 = y1 + dy * k
            if 0 <= x2 <= LIMIT and 0 <= y2 <= LIMIT:
                count_P += 1
                k += 1
            else:
                break

print(count_O + 2 * count_P)