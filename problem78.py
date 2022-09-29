k = sum([[i*(3*i - 1)/2, i*(3*i - 1)/2 + i] for i in range(1, 250)], [])

p = [1]
sgn = [1, 1, -1, -1]
n = 0
m  = 1e6

while p[n]>0:    # expand generating function to calculate p(n)
    n += 1
    px, i = 0, 0
    while k[i] <= n:
        px += p[int(n - k[i])] * sgn[i%4]
        i += 1
    p.append(px % m)
print(n)