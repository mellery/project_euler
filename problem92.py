from euler_common import get_digit

leads_to_89 = {89}
leads_to_1 = {1}
memo = {}


def number_chain(n):
    chain = []
    while n not in leads_to_89 and n not in leads_to_1:
        if n in memo:
            n = memo[n]
            break
        chain.append(n)
        n = sum(int(d)**2 for d in str(n))
    result = 89 if n in leads_to_89 else 1
    for c in chain:
        memo[c] = result
    return result


target = 10000000
count = 0
for n in range(1, target):
    if number_chain(n) == 89:
        count += 1
print(count)
