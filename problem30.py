def problem30(p):
    i = 2
    values = []
    while (i < 1000000):
        i_str = str(i)
        i_list = list(i_str)
        temp = 0
        for x in i_list:
            temp = temp + int(x)**p
        if temp == i:
            print(i)
            values.append(i)
        i = i + 1
    return sum(values)

print(problem30(5))