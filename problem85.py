'''By counting carefully it can be seen that a rectangular grid measuring by

contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.'''

target = 2_000_000
closest = None
min_diff = float('inf')

for m in range(1, 2000):
    for n in range(1, 2000):
        rects = (m * (m + 1) // 2) * (n * (n + 1) // 2)
        diff = abs(rects - target)
        if diff < min_diff:
            min_diff = diff
            closest = (m, n, rects)
        if rects > target:
            break

area = closest[0] * closest[1]
print(area)