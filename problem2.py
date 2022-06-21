
def fib(limit):
    fibs = []
    fibs.append(1)
    fibs.append(1)
    while (fibs[-1] < limit):
        fibs.append(fibs[-1] + fibs[-2])

    print(fibs)

    return fibs

fibs = fib(4000000)

sum = 0

for i in fibs:
    if (i%2 == 0):
        sum = sum + i
print(sum)
