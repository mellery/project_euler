def problem29(a_limit,b_limit):
    distinct = []
    for a in range(2,a_limit+1):
        for b in range(2,b_limit+1):
            if a**b not in distinct:
                distinct.append(a**b)
    print(len(distinct))

#problem29(5,5)
problem29(100,100)
