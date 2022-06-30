def collatz(n):
    count = 1
    while (n != 1):
        count = count + 1
        if (n % 2 == 0):
            n = n/2
        else:
            n = 3*n + 1
    return count

def problem14(limit):
    max_len = 0
    ans = 0
    n = 1
    while (n < limit): 
        temp = collatz(n)
        if temp > max_len:
            max_len = temp
            ans = n
        n = n + 1
        #print(n,temp)
    return ans

#print(problem14(13))
print(problem14(1000000))
