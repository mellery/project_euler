def problem18(input):
    ans = 0

    file1 = open(input, 'r')
    lines = file1.readlines()

    rows = []
    
    for l in lines:
        rows.append(l.split())

    for i in range(0,len(rows)):
        rows[i] = [int(x) for x in rows[i]]
    
    while len(rows) > 1:
        for x in range(0,len(rows[-2])):
            if (rows[-1][x] > rows[-1][x+1]):
                rows[-2][x] = rows[-2][x] + rows[-1][x]
            else:
                rows[-2][x] = rows[-2][x] + rows[-1][x+1]

        rows.pop()

    return rows[0][0]

print(problem18("./input/problem18.txt"))