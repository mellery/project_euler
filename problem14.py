from functools import lru_cache

@lru_cache(maxsize=None)
def collatz(n):
    count = 1
    original = n
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return count

def problem14(limit):
    max_len = 0
    ans = 0
    
    for n in range(1, limit):
        temp = collatz(n)
        if temp > max_len:
            max_len = temp
            ans = n
    
    return ans

#print(problem14(13))
print(problem14(1000000))
