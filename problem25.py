
def problem25(limit):
    a = 1
    b = 1
    index = 3
    while len(str(a+b)) < limit:
        temp = b
        b = a + b
        a = temp
        index = index + 1
    
    return index

print(problem25(1000))
        