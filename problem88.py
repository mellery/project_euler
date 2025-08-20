# A natural number, n, that can be written as the sum and product of a given set of at least two 
# natural numbers, is called a product-sum number:

# n = a_1 + a_2 + ... + a_k = a_1 * a_2 * ... * a_k

# For example,6 = 1 + 2 + 3 = 1 * 2 * 3.

# For a given set of size, k, we shall call the smallest with this property a minimal product-sum 
# number. The minimal product-sum numbers for sets of size, 2, 3, 4, 5, and 6 are as follows.

# k = 

# Hence for 2 <= k <6, the sum of all the minimal product-sum numbers is 4 + 6 + 8 + 12 = 30; note 
# that 8 is only counted once in the sum.

# In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

# What is the sum of all the minimal product-sum numbers for 2 <= k < 12000?

LIMIT = 12000
max_n = 2 * LIMIT
min_ps = [max_n] * (LIMIT + 1)

def search(prod, summ, factors, start):
    k = factors + (prod - summ)
    if k > LIMIT:
        return
    if prod < min_ps[k]:
        min_ps[k] = prod
    for i in range(start, max_n // prod + 1):
        search(prod * i, summ + i, factors + 1, i)

search(1, 1, 1, 2)

# Get unique minimal product-sum numbers for 2 <= k < LIMIT
result = sum(set(min_ps[2:]))
print(result)