#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 21000?

def problem16(n):
    temp = list(str(2**n))
    temp = list(map(int,temp))
    return sum(temp)



#print(problem16(15))
print(problem16(1000))
