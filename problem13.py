def problem13(input):
    ans = 0

    file1 = open(input, 'r')
    lines = file1.readlines()

    values = []
    for l in lines:
        values.append(int(l.strip()))
    return(str(sum(values))[0:10])

print(problem13("./input/problem13.txt"))