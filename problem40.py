def champernowne(n):
    temp = ""
    i = 1
    while len(temp) <= n:
        temp = temp + str(i)
        i = i + 1
    return(int(temp[n-1]))

print(champernowne(1))
print(champernowne(10))
print(champernowne(100))
print(champernowne(1000))
print(champernowne(10000))
print(champernowne(100000))
print(champernowne(1000000))

print(champernowne(1)*champernowne(10)*champernowne(100)*champernowne(1000)*champernowne(10000)*champernowne(100000)*champernowne(1000000))