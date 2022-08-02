#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

def problem11(input, n):
    max_product = 0

    file1 = open(input, 'r')
    lines = file1.readlines()

    table = []
    for l in lines:
        row = l.strip().split(' ')
        row = [int(i) for i in row]
        table.append(row)

    size = len(table)

    # -
    for r in range(0,size):
        for c in range(0,size+1-n):
            product = table[r][c]*table[r][c+1]*table[r][c+2]*table[r][c+3]
            if product > max_product:
                max_product = product

    # |
    for c in range(0,size):
        for r in range(0,size+1-n):
            product = table[r][c]*table[r+1][c]*table[r+2][c]*table[r+3][c]
            if product > max_product:
                max_product = product
    # \
    for r in range(0,size+1-n):
        for c in range(0,size+1-n):
            product = table[r][c]*table[r+1][c+1]*table[r+2][c+2]*table[r+3][c+3]
            if product > max_product:
                max_product = product

    # /
    for r in range(0,size+1-n):
        for c in range(n,size):
            product = table[r][c]*table[r+1][c-1]*table[r+2][c-2]*table[r+3][c-3]
            if product > max_product:
                max_product = product

    return max_product

input = "input\problem11.txt"
print(problem11(input, 4))