from euler_common import is_palindrome

def reverse_and_add(a):
    return a + int(str(a)[::-1])

ans = 0
limit = 10000
for x in range(0,limit):
    is_lychrel = True
    temp = x
    for i in range(0,50):
        temp = reverse_and_add(temp)
        if is_palindrome(temp):
            ans = ans + 1
            is_lychrel = False
            break
    if is_lychrel == True:
        print(x)

print(limit - ans)