from euler_common import is_palindrome

limit = 100
limit = 1000000
ans = 0
for i in range(0,limit):
    b = bin(i).replace('0b','')
    if is_palindrome(i) and is_palindrome(b):
        print(i,b)
        ans = ans + i
print(ans)